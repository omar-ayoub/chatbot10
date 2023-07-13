from agents.agent import RealEstateAgent
from nlp_model import NLPModel

def main():
    # Train the NLP model
    nlp_model = NLPModel()
    nlp_model.train_model('data/training_data.json')

    # Create the chatbot agent
    chatbot_agent = RealEstateAgent()

    print("Bot: Hello, how can I assist you today?")

    while True:
        user_input = input("User: ")
        response = chatbot_agent.process_user_input(user_input)
        print("Bot:", response)

        if user_input.lower() == "exit":
            break

if __name__ == '__main__':
    main()


