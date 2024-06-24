

question = [{
    "question": "What is the correct way to create a function in Python? \n A.def myFunction():   B.create myFunction(): \n C.function myfunction():  ",
    "answer": "A"
},{
    "question": "Which of the following is Immutable datatypes?  \n A.List   B.Dictionary  \n  C.String    D.Sets",
    "answer": "C"
},{
    "question": "which statement is used to  stop a loop? \n A.break    B.exit \n C.return    D.stop",
    "answer": "A"
},{
    "question": "Which method can be used to return a string  in upper case letters ? \n A.upper()   B.upperCase()   \n C.toUpperCase   D.upperCase",
    "answer": "A"
},{
    "question": "Which method can be used to remove any whitespace from both the beginning and the end of a string? \n A.trim()   B.strip()    \n C.len()    D.prtim()",
    "answer": "B"
},{
    "question": "In Python, 'Hello', is the same as 'Hello'?  A.True    B.False",
    "answer": "A"
}]


def Quiz():
    correct_answer = 0
    wrong_answer = 0
    wrong_answer_list = []
    correct_answer_list = []
    
    query = input("woud you like to play game : Y/N : ")
    if(query.lower() =="y"):

    
        for i in range(len(question)):
            print(question[i]["question"])
            answer = input("Enter your answer : ")
            if(answer.upper() ==question[i]["answer"]):
                print("correct answer")
                correct_answer =correct_answer+1
                correct_answer_list.append(question[i]["question"])
            else:
                print("wrong answer")
                wrong_answer =wrong_answer+1
                wrong_answer_list.append(question[i]["question"])

        print(f" you have given total {correct_answer} correct answer")
        print(f"correct answer list are : {correct_answer_list}")
        print(f"you have given total {wrong_answer} wrong answers")
        print(f"wrong answer lists are {wrong_answer_list}")
    
    else:
        print("thank you !!!!")

Quiz()