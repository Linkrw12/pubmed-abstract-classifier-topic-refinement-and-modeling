from Bio import Entrez
import re


class PubMedAbstract(object):
    """Parses an individual abstract isolated from 
    the NCBI PubMed summary file. It's a container that
    holds relevent information for downstream clustering,
    such as title, date, and authors. Its main function 
    is to split the abstract into individual words that 
    will be used for the tokenizer. 
    
    PubMedAbstract is not meant to be used by itself, but 
    is meant to be initialized through one of the 
    PubMedAbstractCollection class methods. 
    """
    def __init__(self, raw_abstract_str: str):

        self.raw_abstract_str = raw_abstract_str
        
        split_abstract_str = self.raw_abstract_str.split("\n\n")
        
        self.title = split_abstract_str[1].replace("\n", "")
        # self.date
        self.journal = split_abstract_str[0]
        self.authors = ''
        self.abstract_str = split_abstract_str[4].replace("\n", "")
        self.doi = re.search("DOI: (.+)", raw_abstract_str).group(1)
        self.pmcid = re.search("PMCID: (.+)", raw_abstract_str).group(1)
        self.pmid = int(re.search("PMID: (\d+)", raw_abstract_str).group(1))
        
    def split_abstract_into_words(self):
        return self.abstract.split(" ")

    
class PubMedAbstractCollection(object):
    """
    """
    def __init__(self, abstracts: list[PubMedAbstract]):
        self.abstracts = abstracts
    
    @classmethod
    def load_from_search_query(cls, query):
        pass
    
    @classmethod
    def load_from_abstract_txt_file(cls, file):
        pass
    
    def split_abstracts_into_words(self):
        return [abstract.split_abstract_into_words()
                for abstract in self.abstracts]