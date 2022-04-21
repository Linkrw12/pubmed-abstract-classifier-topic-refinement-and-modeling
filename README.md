# pubmed-abstract-classifier-topic-refinement-and-modeling

Stremlit app designed to query pubmed and (eventually) perform topic modeling. 

# Goals
* Make streamlit app base
* Query pubmed w/ app
* Alternatively, upload abstract file
* Embed abstracts using PubMedBERT "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
* OR select from a dropdown
* Topic modeling using abstracts

# Extra
* Make Dockerfile to create streamlit app image

## Run streamlit app
`$ streamlit run streamlit_pubmed_topic_modeling.py`
