from tkinter import *
import random
import re
from datetime import datetime

def generate_response(user_input):
    user_input = user_input.lower()

    # Responses based on user input patterns
    if re.match("hi|hello|hey", user_input, re.IGNORECASE):
        return "Hello! How can I help you?"
    elif re.match("how are you|how are you doing", user_input, re.IGNORECASE):
        return "I'm a bot, so I'm doing great!"
    elif re.match("bye|goodbye|see you", user_input, re.IGNORECASE):
        return "Goodbye! Have a great day!"
    elif re.match("date|day", user_input, re.IGNORECASE):
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."
    elif re.match("time", user_input, re.IGNORECASE):
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif re.match("tell me a joke", user_input, re.IGNORECASE):
        # You can add your own collection of jokes here
        jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!"]
        return random.choice(jokes)
    else:
        return "I'm not sure how to respond to that."

def process_user_input():
    user_input = user_value.get()
    t1.insert(END, "you: " + user_input + "\n")

    response = generate_response(user_input)

    t1.insert(END, "Chatbot: " + response + "\n")
    user_value.set("")

window = Tk()
window.title("Chatbot")

e1 = Label(window, text="you")
user_value = StringVar()
e2 = Entry(window, textvariable=user_value)
e2.bind("<Return>", lambda event: process_user_input())
t1 = Text(window, height=10, width=50)

# Add a scrollbar to the Text widget
scrollbar = Scrollbar(window, command=t1.yview)
t1.configure(yscrollcommand=scrollbar.set)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
t1.grid(row=1, column=0, columnspan=2)
scrollbar.grid(row=1, column=2, sticky='ns')

window.mainloop()
