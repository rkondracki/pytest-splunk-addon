class EventgenSample(object):
    """
    Object for one sample 
    """
    def __init__(self, sample, meta_data, tokens):
        self.tokens = [] # Rules 
        self.sourcetype = meta_data.get("sourcetype")
        self.source = meta_data.get("source")
        self.host = meta_data.get("source")
        self.ingestion_type = meta_data.get("ingestion_type")
        self.sample_text = str
        self.parsed_text = self.sample_text

    def tokenize(self):
        for each_token in self.tokens:
            self.parsed_text = each_token.apply(self.parsed_text)
