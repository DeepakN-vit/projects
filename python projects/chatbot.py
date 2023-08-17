import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"how are you|how's it going",
        ["I'm just a chatbot, but I'm here to help!", "I don't have feelings, but I'm operational."]
    ],
    [
        r"what is your name|who are you",
        ["I'm a simple chatbot.", "You can call me ChatBot."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Have a great day!", "Take care!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I can't understand that.", "Could you please rephrase?", "I'm not sure how to respond to that."]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Main loop
print("ChatBot: Hi! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
