from pipeline.preprocessing import parse_text


class RelevanceModel:
    def __init__(self, classifier, processor):
        self.classifier = classifier
        self.processor = processor

    def parse_data(self, text):
        return parse_text([text], self.processor)

    def get_validity(self, text):
        embeddings = self.parse_data(text)
        return {
            "is_valid": str(self.classifier.predict(embeddings)[0])
        }
