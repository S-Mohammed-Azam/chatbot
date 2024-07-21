


import difflib
import json
"""
data = {
    "what is your name":"I am gamini",
    "who is your owner":"his name is Azam",
    "what is mean by python":"python is a programming language",
    "what is the use of c++":"it is also a programming language"
    }
with open('data_base.txt' , 'w') as brain :
    json.dump(data, brain)
"""

try:
    with open('data_base.txt') as brain:
        data = json.load(brain)
except:
    print('I was born right now ')

def searching_question(user_input):
    question = list(data.keys())
    best_match = difflib.get_close_matches(user_input, question,n=1)
    if best_match:
        return best_match[0]
    else:
        return None

def teacher():
    teach = input("          can you teach me? : ")
    if "yes" in teach.lower():
        question = input("question : ").lower()
        answer = input("answer : ").lower()
        data[question] = answer
        print("vision : thank you! I have learn a new response")
        print("")
        with open('data_base.txt' , 'w') as brain :
            json.dump(data, brain)
    if "no" in teach.lower():
        print("vision : Ok! would you want any help.")
        print("")




def searching_answer(match):
    return data.get(match, "I don't know about this can you teach me")

def processing(user_input):
    question = searching_question(user_input)
    if question:
        answer = searching_answer(question)
        print("vision : ",answer)
        print("")
    else:
        answer = "I don't know about this."
        print("vision : ",answer)
        teacher()



def update(input1,input2):
    data.update({input1:input2})

while True:
    user_input = input("you : ")
    if user_input.lower() == "quite" :
        break
    elif "update" in user_input.lower():
        print("enter the question which you want to update ")
        input1 = input("you : ")
        question = searching_question(input1)
        if question:
            input2 = input("enter your answer : ")
            update(input1,input2)
            print("vision : thank you I have learnt a new response.")
            with open('data_base.txt' , 'w') as brain :
                json.dump(data, brain)
            print("")

        else:
            print("I don't know about that so you can't update if you want you can teach me.")
            teacher()
    else:
        processing(user_input)






