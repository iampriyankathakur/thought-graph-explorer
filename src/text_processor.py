import spacy
from keybert import KeyBERT

nlp = spacy.load("en_core_web_sm")
kw_model = KeyBERT()

def extract_concepts(text):
    doc = nlp(text)
    
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    keywords = [kw[0] for kw in kw_model.extract_keywords(text, top_n=10)]
    
    concepts = list(set(noun_phrases + keywords))
    return concepts
