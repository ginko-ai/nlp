class PromptVocabulary:
    """
    A class to manage and organize prompt engineering vocabulary
    """

    def __init__(self):
        self.analytical_verbs = {
            'analyze': 'detailed examination',
            'evaluate': 'assessment against criteria',
            'compare': 'systematic contrast',
            'examine': 'thorough investigation',
            'investigate': 'deep exploration'
        }

        self.transformative_verbs = {
            'transform': 'substantial change',
            'convert': 'specific transformation',
            'modify': 'targeted changes',
            'adapt': 'contextual adjustment',
            'restructure': 'fundamental reorganization'
        }

        self.directive_verbs = {
            'precisely': 'exactness',
            'specifically': 'detailed requirements',
            'thoroughly': 'comprehensive treatment',
            'systematically': 'structured approach',
            'effectively': 'desired outcome'
        }

    def get_verb_category(self, verb: str) -> str:
        """Returns the category of a given verb"""
        for category in [self.analytical_verbs, self.transformative_verbs,
                        self.directive_verbs]:
            if verb in category:
                return category[verb]
        return "Verb not found in vocabulary"

    def suggest_verbs(self, intent: str) -> list:
        """Suggests appropriate verbs based on intended outcome"""
        intent_mapping = {
            'analysis': self.analytical_verbs,
            'change': self.transformative_verbs,
            'instruction': self.directive_verbs
        }
        return list(intent_mapping.get(intent, {}).keys())