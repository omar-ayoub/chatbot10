import json
import spacy
import random
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


class NLPModel:
    def __init__(self):
        self.trained_model_path = 'trained_model'

def train_model(self, training_data_path):
    # Load the training data
    with open(training_data_path, 'r') as file:
        training_data = json.load(file)

    # Create a new spaCy pipeline
    nlp = spacy.blank("en")

    # Add the text categorizer component to the pipeline
    textcat = nlp.create_pipe("textcat", config={"exclusive_classes": True})
    nlp.add_pipe(textcat)

    # Add labels to the text categorizer
    labels = list(set(example["intent"] for example in training_data))
    for label in labels:
        textcat.add_label(label)

    # Prepare the training data for spaCy
    train_data = []
    for example in training_data:
        text = example["text"]
        intent = example["intent"]
        train_data.append((text, {"cats": {intent: 1.0}}))

    # Train the spaCy model
    optimizer = nlp.begin_training()
    for _ in range(10):
        random.shuffle(train_data)
        losses = {}
        for text, annotations in train_data:
            nlp.update([text], [annotations], sgd=optimizer, losses=losses)
        print("Losses", losses)

    # Save the trained model
    nlp.to_disk(self.trained_model_path)


    def predict_intent(self, text):
        interpreter = Interpreter.load(self.trained_model_path, project_name='nlp_model')
        intent = interpreter.parse(text)['intent']['name']
        return intent
