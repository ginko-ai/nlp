class LanguageAnalyzer:
    def __init__(self):
        self.linguistic_patterns = {
            'distortions': ['mind_reading', 'lost_performative', 'cause_effect'],
            'generalizations': ['universal_quantifiers', 'modal_operators'],
            'deletions': ['nominalizations', 'unspecified_verbs', 'simple_deletions']
        }

        self.grammatical_elements = {
            'morphology': ['word_formation', 'inflection', 'derivation'],
            'syntax': ['sentence_structure', 'phrase_structure', 'word_order'],
            'semantics': ['meaning', 'context', 'reference'],
            'phonology': ['sound_patterns', 'intonation', 'stress'],
            'pragmatics': ['context_usage', 'implication', 'presupposition']
        }

    def analyze_linguistics(self, text):
        """Analyze text for linguistic patterns"""
        results = {
            'distortions': self._check_distortions(text),
            'generalizations': self._check_generalizations(text),
            'deletions': self._check_deletions(text)
        }
        return results

    def analyze_grammar(self, text):
        """Analyze text for grammatical elements"""
        results = {
            'morphology': self._analyze_morphology(text),
            'syntax': self._analyze_syntax(text),
            'semantics': self._analyze_semantics(text),
            'phonology': self._analyze_phonology(text),
            'pragmatics': self._analyze_pragmatics(text)
        }
        return results
        