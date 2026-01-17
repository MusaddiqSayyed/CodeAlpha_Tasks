def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your name":
        return "I'm Chatbot."
    elif user_input == "tell me a joke":
        return "why did the scarecrow win an award? Because he was outstanding in his field!"
    elif user_input == "what can you do":
        return "I can chat with you and tell you jokes!"
    
    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "bye":
            break


if __name__ == "__main__":
    run_chatbot()