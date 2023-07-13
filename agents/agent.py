import json
from utils.data_handler import load_property_data

class RealEstateAgent:
    def __init__(self):
        self.properties = load_property_data()  # Load property data from JSON file

    def search_properties(self, query):
        """
        Perform property search based on user query.

        Args:
            query (str): User query to search for properties.

        Returns:
            list: List of properties that match the search criteria.
        """
        matched_properties = []
        for property in self.properties:
            # Implement your search criteria here, considering different query parameters like prices, areas, locations, etc.

            # Example: Searching by property description, location, or price
            if query.lower() in property['description'].lower() or \
               query.lower() in property['location'].lower() or \
               query.lower() in str(property['price']).lower():
                matched_properties.append(property)

        return matched_properties

    def process_user_input(self, user_input):
        """
        Process user input and generate appropriate response.

        Args:
            user_input (str): User input/query.

        Returns:
            str: Generated response based on the user input.
        """
        response = ""

        # Example: Handle property search query
        if user_input.startswith("search"):
            search_query = user_input.replace("search", "").strip()
            properties = self.search_properties(search_query)

            # Generate response based on search results
            if properties:
                response += "Here are some properties that match your search criteria:\n"
                for property in properties:
                    response += f"- {property['name']} in {property['location']} ({property['price']})\n"
            else:
                response = "Sorry, no properties match your search criteria."

        # Add more logic to handle other user queries
        # For each specific query type, implement the necessary logic to generate the appropriate response

        return response


# Instantiate the RealEstateAgent
chatbot_agent = RealEstateAgent()

# Process user input
user_input = input("User: ")
response = chatbot_agent.process_user_input(user_input)
print("Bot:", response)
