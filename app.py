from flask import Flask, render_template, request, jsonify
from urllib.parse import unquote
import random
from langchain_community.document_loaders import WikipediaLoader

app = Flask(__name__)

def get_data(query):
    """
    Fetches data from Wikipedia based on the query.

    Args:
        query (str): The topic to search for on Wikipedia.

    Returns:
        str: The first 400 characters of the Wikipedia page content,
             or an error message if the page is not found.
    """
    try:
        docs = WikipediaLoader(query=query, load_max_docs=2).load()
        if docs:
            return docs[0].page_content[:400]
        else:
            return "I couldn't find information on that topic."
    except Exception as e:
        return f"An error occurred: {e}"

def greet():
    """
    Returns a random greeting message.
    """
    greetings = [
        "Hello! I am ChatBot.",
        "Hi there! How can I assist you?",
        "Hey! What brings you here today?"
    ]
    return random.choice(greetings)

@app.route('/')
def index():
    """
    Renders the main page of the application.
    """
    greeting_message = greet()
    return render_template('index.html', greeting=greeting_message)

@app.route('/search')
def search():
    """
    Handles the search request and returns the Wikipedia summary.
    """
    topic = request.args.get('topic')
    if not topic:
        return jsonify({'error': 'No topic provided'}), 400

    decoded_topic = unquote(topic)  
    response_data = get_data(decoded_topic)
    return jsonify({'response': response_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
