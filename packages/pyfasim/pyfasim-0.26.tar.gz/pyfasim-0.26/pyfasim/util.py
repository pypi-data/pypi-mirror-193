from automata.fa.dfa import DFA
from IPython.display import display, Image, Math, Latex, HTML

counter = 0

def parse_fa(description, type="dfa"):
    global counter
    allow_partial = False
    lines = []
    for line in description.split('\n'):
        line = line.strip()
        if line == '' or line[0] == '#':
            continue
        lines.append(line)
    line = lines.pop(0)
    if line.startswith('name:'):
        _,name = line.split()
        line = lines.pop(0)
    else:
        name = f"{type}{counter}"
        counter += 1
    if line.startswith('states:'):
        states = set(line[7:].split())
    else:
        raise Exception("Expected states line..")
    if not states:
        raise Exception("Empty states list .. !?")
    line = lines.pop(0)
    if line.startswith('input_symbols:'):
        input_symbols = set(line[14:].split())
    else:
        raise Exception("Expected input_symbols line..")
    if not input_symbols:
        raise Exception("Empty input_symbols set .. !?")
    trans = lines.pop(0)
    if not trans == "transitions:":
        raise Exception(f"Expected transitions header line: {trans}")

    tlines = []
    initial_state_line = ""
    for _ in range(len(lines)):
        line = lines.pop(0)
        if 'initial_state:' in line:
            initial_state_line = line
            break
        tlines.append(line)
    if initial_state_line == "":
        raise Exception("Expected initial_state line..")

    delta = dict()
    for line in tlines:
        if type == "dfa":
            state, d = __parse_dfa_line(line)
        else:
            state, d = __parse_nfa_line(line, input_symbols)
        delta[state] = d

    _,initial_state = initial_state_line.split()

    line = lines.pop(0)
    if line.startswith('final_states:'):
        final_states = set(line[13:].split())
    else:
        raise Exception("Expected final_states line..")
    if type == 'dfa':
        return name, states, input_symbols, delta, initial_state, final_states, allow_partial
    else:
        return name, states, input_symbols, delta, initial_state, final_states

def __parse_dfa_line(line):
    items = line.replace(':', ' ').split()
    if len(items)%2 == 0:
        raise Exception(f"Invalid transitions line: {line}")
    state = items.pop(0)
    d = dict()
    for i in range(0, len(items), 2):
        symbol,kstate = items[i:i+2]
        d[symbol] = kstate
    return state, d

def __parse_nfa_line(line, input_symbols):
    d = dict()
    for s in input_symbols:
        d[s] = set()

    i = line.find(':')
    if i == -1:
        raise Exception(f"Invalid transitions line: {line}")
    state = line[:i].strip()
    for item in line[i+1:].split(","):
        item = item.strip()
        if item == "":
            break
        if not ":" in item:
            raise Exception(f"Invalid transitions line: {line}")
        k,v = item.split(":")
        if k == "epsilon":
            k = ''
        d[k] =  set(v.split())

    return state, d

def _auto_name(self, type):
    global counter
    name = f"{type}{counter}"
    self.__dict__['name'] = name
    counter += 1
    return name

def __diagram(self):
    pd = self.show_diagram()
    if hasattr(self, 'name'):
        name = self.name
    else:
        name = _auto_name(self, 'dfa')
    #pngfile = f"d:/cmfl/code/FA/{name}.png"
    pngfile = f"{name}.png"
    pd.write_png(pngfile)
    #pd.write_png(pngfile, prog=dot)
    display(Image(pngfile))

def __compseq(self, w):
    #print(f"input={w}")
    if isinstance(self, DFA):
        it = self.read_input_stepwise(w, ignore_rejection=True)
    else:
        it = self.read_input_stepwise(w)
    i = 0
    #s =  r"\mathbf{%s}" % (self.initial_state,)
    q = next(it)
    if isinstance(q, frozenset):
        q = ','.join(q)
    s =  r"\mathbf{%s}" % (q,)
    path = [q]
    while True:
        try:
            q = next(it)
            if isinstance(q,frozenset):
                q = ','.join(q)
            path.append(w[i])
            path.append(q)
            i += 1
        except Exception as e:
            #print(f"Exception={e}")
            break
    #print(f"path={path}")
    #if path[-1] in self.final_states:
    #    print(f"ACCEPTED: {w}")
    if w in self:
        print(f"ACCEPTED: {w}")
    else:
        print(f"REJECTED: {w}")
    _display_path(path)

def __nfa_compseq(self, w, limit=1):
    print(f"input={w}")
    if not w in self:
        print(f"REJECTED: {w}")
        return 0

    it = _nfa_computation_paths_iter(self, w)
    ctr = 0
    for i in range(limit):
        try:
            path = next(it)
            _display_path(path)
            ctr += 1
        except:
            break
    return ctr

def _display_path(path):
    n = len(path)
    s = ""
    for i in range(n):
        if i%2 == 0:
            q = path[i]
            s +=  r"\mathbf{%s}" % (q,)
        else:
            symbol = path[i]
            if symbol == "epsilon":
                symbol = r"$\varepsilon$"
            s += r"\xrightarrow{\;\textbf{%s}\;}" % (symbol,)

    display(HTML("<br/>"))
    display(Latex(f'${s}$'))
    #print(s)

def __words_of_lengths(self, n1, n2=None):
    W = list(self.words_of_length(n1))
    if n2 is None:
        return W
    for n in range(n1+1, n2+1):
        L = list(self.words_of_length(n))
        W.extend(L)
    return W

def __random_words(self, m, n=1):
    words = set()
    if n<1:
        return list()
    for i in range(0, 2**(m+1)):
        w = self.random_word(m)
        words.add(w)
        if len(words) == n:
            break
    return list(words)

def __getitem(self, subscript):
    if isinstance(subscript, slice):
        start, stop, step = subscript.start, subscript.stop, subscript.step
        if step is None:
            step = 1
        if step>0:
            sign=1
        else:
            sign=-1
        words = list()
        for i in range(start, stop+sign, step):
            words.extend(self.words_of_length(i))
    else:
        words = list(self.words_of_length(subscript))
    return words


def _nfa_computation_paths_iter(nfa, w):
    final_states = nfa.final_states
    initial_state = nfa.initial_state
    path0 = [initial_state]
    CurrentPaths = [path0]
    FinalPaths = []
    ctr = 0
    limit = len(w) * 100
    while True:
        ctr += 1
        if ctr>limit:
            print(f"Reached maximal iteration limit! limit={limit}")
            break
        if not CurrentPaths:
            break
        NextPaths = []
        for path in CurrentPaths:
            npaths, final = _nfa_proceed(nfa, path, w)
            if final:
                if path[-1] in final_states:
                    yield path
                #FinalPaths.append(path)
                continue
            NextPaths.extend(npaths)
        CurrentPaths = NextPaths
        #for p in C: print(p)
        #print(80 * '-')
        #time.sleep(0.25)

    #print(f"w={w}")
    #print(80 * '=')
    #for p in FinalPaths:
    #    print(p)
    #nfa.diagram()

def _nfa_proceed(nfa, path, w):
    cw = _nfa_current_word(path)
    u = w[len(cw):]
    if not u:
        return [], True
    char = u[0]
    currstate = path[-1]
    trans = nfa.transitions[currstate]
    npaths = []
    for symbol, end_states in trans.items():
        if symbol == char:
            npath = path + [char]
        elif not symbol:
            npath = path + ['epsilon']
        else:
            continue
        for end_state in end_states:
            p = npath + [end_state]
            if _has_eps_loop(p):
                continue
            npaths.append(p)
    return npaths, False

def _nfa_current_word(path):
    n = len(path)
    cw = ""
    for i in range(1,n,2):
        c = path[i]
        if c == 'epsilon':
            c = ''
        cw += c
    return cw

def _has_eps_loop(path):
    n = len(path)
    end = n-1
    start = n-1
    for i in range(n-2,-1,-1):
        if i%2 and path[i] != 'epsilon':
            start = i+1
            break
        elif i%2==0 and path[i]== path[end]:
            return True
    if start<end and path[start] == path[end]:
        return True
    return False
