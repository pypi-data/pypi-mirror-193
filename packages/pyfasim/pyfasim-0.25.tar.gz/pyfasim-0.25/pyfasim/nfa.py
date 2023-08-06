from automata.fa.nfa import NFA
from .util import parse_fa, display, Image, Math, Latex, HTML, \
                 _auto_name, __diagram, __nfa_compseq
#dot = r'c:\Graphviz7.01\bin\dot.exe'

def __nfa_init(self, description=None, *, states=None, input_symbols=None,
                     transitions=None, initial_state=None,
                     final_states=None):
    """Initialize a complete NFA."""
    #print(f"description={description}")
    if description:
        name, states, input_symbols, transitions, initial_state, final_states = parse_fa(description, 'nfa')
        #print(f"name={name}")
        #self.name = name
        self.__dict__['name'] = name
    super(NFA, self).__init__(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states,
        _lambda_closures=self._compute_lambda_closures(states, transitions)
    )

NFA.__init__ = __nfa_init
NFA.diagram = __diagram
NFA.compseq = __nfa_compseq
#NFA.words_of_lengths = __words_of_lengths
#NFA.random_words = __random_words
#NFA.__getitem__ = __getitem

