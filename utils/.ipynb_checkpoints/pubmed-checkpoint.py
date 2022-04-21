from Bio import Entrez

class PubMedAbstract(object):
    def __init__(self):
        pass  

    def x(self):
        pass
    
class PubMedAbstractCollection(object):
    def __init__(self, abstracts):
        self.abstracts = abstracts
    
    @classmethod
    def load_from_search_query(cls, query):
        pass
    
    @classmethod
    def load_from_abstract_txt_file(cls, file):
        pass