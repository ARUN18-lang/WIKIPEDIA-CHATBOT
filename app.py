import streamlit as st
import random
from langchain_community.document_loaders import WikipediaLoader

def get_data(query):
    docs = WikipediaLoader(query=query, load_max_docs=2).load()
    return docs[0].page_content[:400]

def greet():
    greetings = [
        "Hello! I am ChatBot.",
        "Hi there! How can I assist you?",
        "Hey! What brings you here today?"
    ]
    return random.choice(greetings)

def main():
    st.title("Wikipedia Chatbot")

    greeting = greet()
    st.write(greeting)

    name = st.text_input("What's your name?", "")
    if name:
        st.write(f"Nice to meet you, {name}!")

        topic = st.text_input("What would you like to know more about? Type a topic, and I'll fetch it from Wikipedia:")
        if topic:
            response = get_data(topic)
            st.write(f"ChatBot: {response}")

        if st.button("Search another topic"):
            st.experimental_rerun()
    else:
        st.write("Please enter your name to continue.")

if __name__ == "__main__":
    main()
