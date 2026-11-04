# Rule based chatbot project
import datetime
import time

name = input(" welcome !!! Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 11 :
    print("Good Morning", name)
elif 11 <= presentHour < 17 :
    print("Good Afternoon", name)
elif 17 <= presentHour < 19 :
    print("Good Evening", name)
else :
    print("Good Night", name)


print("Hello , User Welcome to Rule Based Chatbot :) ")
print("You can ask me basic questions, type 'Bye' to exit bot")

# Chatbot Memory Creation [dictionary of  responses]

responses = {
    "hello": "Hi, How can I help you?",
    "tell me about yourself":  "I am rule based chatbot",
    "do some praise about me": '''You are so beautiful .You have good thoughts.
    Your heart and soul are so pure.''',
    "you are a liar": "no, I am chatbot. I can assist you in your work.",
    "motivate me":"you are a young lady. Go ahead and keep going.Inshallah everything will be alright.",
    "inshallah" : "You are very brave. Allah is always with  you.",
    "nobody loves me" : "Who told you ? Allah loves you. Pray to Allah.",
    "can you see me" : "no, I am chatbot your assistant. ",
    "are you chatbot?" : "Yes, I am. tell me how can I help you?",
    "can you love me?" : " I am not human . I am chatbot .I dont have feelings like you.",
    "what can you do ?" : ''' I can assist in your homework, studies, projects , presentation."
    what are you doing today?'''

}

# Method / Function to get response of chatbot

def getResponseOfBot(userQuest) :
    userQuest = userQuest.lower()
    for eachKey in responses:
        if eachKey in userQuest:
            return responses[eachKey]
    return " see you tomorrow.I don't know now."
    
# take user input []
while True:
    userInput = input("ask questions to chatbot: ")
    reply = getResponseOfBot(userInput)
    print("Bot Response: ", reply)

    if 'bye' in userInput.lower() :
        break


