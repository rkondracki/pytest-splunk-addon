from concurrent.futures import ProcessPoolExecutor
from .eventgen_sample import EventgenSample
from .eventgen_parser import EventgenParser
class SampleParser(object):
    """
    Main Class
    Parse the eventgen, Generate sample objects 
    """
    PROCESS_COUNT = 4
    def __init__(self, addon_path):
        self.addon_path = addon_path

    def get_samples(self):
        """
        Generate the samples one by one

        {
            "event": str,
            "_time": str,
            "host": str,
            "source": str,
            "sourcetype": str,
            "key_field": str,
            "fields": {
                "dvc" str 
            }
        }
        """
        self.samples =  EventgenParser.parse_eventgen(self.addon_path)

    def tokenize(self):
        """
        Tokenize all the sample files using ThreadPool 
        """
        with ProcessPoolExecutor(self.PROCESS_COUNT) as executor:
            samples = list(executor.map(EventgenSample.tokenize, self.samples))
            return samples


if __name__ == "__main__":
    egen = SampleParser("Location of TA")
    for each_sample in egen.get_samples():
        # Generate a test 
        pass

