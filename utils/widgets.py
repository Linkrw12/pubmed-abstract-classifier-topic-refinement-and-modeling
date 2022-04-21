import streamlit as st
import transformers
from .pubmed import PubMedAbstractCollection


def load_abstract_widgets():
    input_method = st.selectbox(
        "Search PubMed or load previously generated abstract file:",
        ('Search PubMed', 'Load Generated Abstract File')
    )
    if input_method == 'Search PubMed':
        query = st.text_input("PubMed Query:")
        abstracts = PubMedAbstractCollection.load_from_search_query(query)
    elif input_method == 'Load Generated Abstract File':
        file = st.file_uploader("Upload Pubmed Abstract (set) file:")
        abstracts = PubMedAbstractCollection.load_from_abstract_txt_file(file)
    return abstracts

def select_transformers_widgets():
    
    def load_embedder_and_tokenizer():
        pass
    
    embedder_tokenizer_combo = st.selectbox(
        "Select Pubmed Abstract Embedder and Tokenizer:",
        ('microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext', 'other Hugging Face transformer', 'custom pretrained transformer')
    )
    
    if embedder_tokenizer_combo == 'custom pretrained transformer':
        embedder = st.file_uploader("Embeder")
        tokenizer = st.file_uploader("Tokenizer")
        return embedder, tokenizer
    elif embedder_tokenizer_combo == 'other Hugging Face transformer':
        hugging_face_model_card = st.text_input("Type model card")
        embedder, tokenizer = 'foo', 'bar'
        return embedder, tokenizer
    else:
        embedder, tokenizer = 'foo', 'bar'
        return embedder, tokenizer