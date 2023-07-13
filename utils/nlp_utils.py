import spacy
import re

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Add any additional text preprocessing steps as needed

    return text

def extract_entities(text):
    doc = nlp(text)
    entities = []
    for entity in doc.ents:
        entities.append(entity.text)
    return entities

def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

def lemmatize_text(text):
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return lemmas

# Add more utility functions as needed for NLP tasks

