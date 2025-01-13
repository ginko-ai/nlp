class O1PromptSystem:
    def __init__(self):
        self.goal = Goal()
        self.return_format = ReturnFormat()
        self.warnings = Warnings()
        self.context = ContextDump()
        self.processor = PromptProcessor()

    def process_prompt(self, prompt_text):
        """Process prompt through o1 structure"""
        # Extract components
        goal = self.goal.extract(prompt_text)
        format_reqs = self.return_format.extract(prompt_text)
        warnings = self.warnings.extract(prompt_text)
        context = self.context.extract(prompt_text)

        # Process through system
        result = self.processor.process(
            goal=goal,
            format_reqs=format_reqs,
            warnings=warnings,
            context=context
        )

        return result

class Goal:
    def __init__(self):
        self.objective = None
        self.constraints = []
        self.success_criteria = []

    def extract(self, text):
        """Extract goal components from text"""
        return {
            'objective': self._find_objective(text),
            'constraints': self._find_constraints(text),
            'success_criteria': self._find_success_criteria(text)
        }

class ReturnFormat:
    def __init__(self):
        self.structure = None
        self.data_types = {}
        self.formatting_rules = []

    def extract(self, text):
        """Extract return format requirements"""
        return {
            'structure': self._parse_structure(text),
            'data_types': self._identify_data_types(text),
            'formatting': self._extract_formatting_rules(text)
        }

class Warnings:
    def __init__(self):
        self.validation_rules = []
        self.error_checks = []

    def extract(self, text):
        """Extract warning conditions"""
        return {
            'validation': self._parse_validation_rules(text),
            'error_checks': self._parse_error_checks(text)
        }

class ContextDump:
    def __init__(self):
        self.background = None
        self.user_state = {}
        self.history = []

    def extract(self, text):
        """Extract context information"""
        return {
            'background': self._parse_background(text),
            'user_state': self._parse_user_state(text),
            'history': self._parse_history(text)
        }