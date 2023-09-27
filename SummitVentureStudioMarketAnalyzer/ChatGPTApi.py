from WrenchCL import ChatGptSuperClass

class SvsChatGPTClass(ChatGptSuperClass):

    def __init__(self, text_body, endpoint = None, key = None):
        self.text_body = text_body
        
        self.keywords = None
        self.concepts = None
        self.summary = None

        self._function_generator()
        self._message_generator()

        # Super Class
        super().__init__(endpoint = endpoint, key = key)
        self.response_parser()

    def response_parser(self):
        self.keywords = self.response.get('Keywords')
        self.concepts = self.response.get('Concepts')
        self.summary = self.response.get('Summary')

    def _message_generator(self):
        self.message = [{"role": "system",
                         "content": """Given the below text generate five technical Keywords, three technical Concepts and a 200 word technical Summary.
                                    Do not use acronymns or proper nouns for either the concepts or the keywords.
                                    Return the answer as a python dictionary as {Keywords: list, Concepts: list, Summary: str}"""}]
        self.message.append({"role": "user",
                             "content": self.text_body})

    def _function_generator(self):
        self.function = [
            {
                "name": "text_analyser",
                "description": "Given a text generate five technical Keywords, three technical Concepts and a 300 word technical Summary",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "Text": {
                            "type": "string",
                            "description": "The text to be processed",
                        },
                    },
                    "required": ["Text"],
                },
            }
        ]

    def get_keywords(self):
        return list(self.keywords)

    def get_concepts(self):
        return list(self.concepts)

    def get_summary(self):
        return str(self.summary)