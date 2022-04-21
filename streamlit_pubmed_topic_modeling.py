import streamlit as st
from utils.widgets import load_abstract_widgets, select_transformers_widgets

st.title('Pubmed Abstract Classifier and Topic Modeler')

st.subheader('Select Abstract Inputs')
abstracts = load_abstract_widgets()

st.subheader('Select Abstract Embeder and Tokenizer')
embedder, tokenizer = select_transformers_widgets()




