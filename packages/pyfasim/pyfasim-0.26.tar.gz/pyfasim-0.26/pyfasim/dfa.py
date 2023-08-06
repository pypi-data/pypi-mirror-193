from automata.fa.dfa import DFA
from .util import parse_fa, display, Image, Math, Latex, HTML, \
                 _auto_name, __diagram, __compseq, \
                 __words_of_lengths, __random_words, __getitem
#dot = r'c:\Graphviz7.01\bin\dot.exe'

def __dfa_init(self, description=None, *, states=None, input_symbols=None,
                     transitions=None, initial_state=None,
                     final_states=None, allow_partial=False):
    """Initialize a complete DFA."""
    if description:
        name, states, input_symbols, transitions, initial_state, final_states, allow_partial = parse_fa(description, 'dfa')
        #print(f"name={name}")
        #self.name = name
        self.__dict__['name'] = name
    super(DFA, self).__init__(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states,
        allow_partial=allow_partial
    )
    object.__setattr__(self, '_word_cache', [])
    object.__setattr__(self, '_count_cache', [])
   
DFA.__init__ = __dfa_init
DFA.diagram = __diagram
DFA.compseq = __compseq
DFA.words_of_lengths = __words_of_lengths
DFA.random_words = __random_words
DFA.__getitem__ = __getitem


