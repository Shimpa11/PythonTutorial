"""
    Simple Chatbot with NLTK
    PS: No ML or Deep Learning Associated
"""



# Chat is a Class which will handle Chat-Bot logic for us !
# reflections is a dictionary of key and value pairs, For a key as input we have an outcome as value
# print(reflections)
# print(reflections['i was'])

from nltk.chat.util import Chat,reflections

conversation=[
    [
        "Hi",
        ["Hey, What can I dlo for you?",]
    ],

    [
        "What is your name?",
        ["My name is John. Good to talk to you!"]
    ],


    [
        r"my name is(.*)",
        ["Hello %1, its good to chat with you!!"]
    ],

[
        r"i know (.*)",
        ["OK!! So you can code  %1" "this is great that you know %1"]
    ],


]
# print(conversation)
# print(reflections)
def main():
    print("This is John. How can I  help you? You can anytime press quit to finish the chat")
    chatBot=Chat(conversation,reflections)
    chatBot.converse()
if __name__=='__main__':
    main()