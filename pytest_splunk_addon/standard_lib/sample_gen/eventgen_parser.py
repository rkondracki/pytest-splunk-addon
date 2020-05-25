from eventgen_sample import EventgenSample
from concurrent.futures import ThreadPoolExecutor
import os
import re 
class EventgenParser(object):
    META_KEYS = ('source','sourcetype','host', 'ingestion_type')

    @classmethod
    def parse_eventgen(cls, addon_path):
        # Parse using App inspect 
        stanzas = []
        cls.addon_path = addon_path
        with ThreadPoolExecutor(10) as executor:
            yield from executor.map(cls.parse_sample, stanzas)

    @classmethod
    def parse_sample(cls, each_stanza):
        tokens = []
        options = []
        meta_data = {key:each_stanza[key] for key in cls.META_KEYS if key in each_stanza}
        for each_token in options:
            # Create list of dict
            # In one dict, all the property of token should be grouped
            token = {
                "replacement": str,
                "replacement_type": str,
                "token": str, 
                "key": str
            }
            tokens.append(token)

        for each_file in os.listdir(os.path.join(cls.addon_path, "samples")):
            if re.search(each_stanza, each_file):
                yield EventgenSample(
                    each_file,
                    meta_data,
                    tokens
                )
