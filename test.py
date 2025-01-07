from hugchat import hugchat
from hugchat.login import Login
import os
from engine.feautures import chatBot  # Import the chatBot function from features.py

try:
    # Define the query you want to send to the chatbot
    query = "I feel sad"

    # Call the chatBot function from features.py
    response = chatBot(query)
    
    # Print the response from the chatbot
    print("ChatBot Response:", response)

except Exception as e:
    print(f"Error: {e}")
