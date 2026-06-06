
import requests
import json

# Generates random quotes as source of motivation

class Quotes:

    def __init__(self):
        pass

    def random_quote(self):

        url = "https://zenquotes.io/api/random"
        try:
            
            response = requests.get(url)
        except Exception as err:
            return f""

        data = response.json()

        q_dict = data[0]
        
        return f"Quote: '{q_dict['q']}' - {q_dict['a']}"