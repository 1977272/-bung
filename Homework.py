# Just doing the homework
# Function for making a question
def check_weather(question):
    if question.lower() == "wie ist das wetter?":
        return "Das Wetter ist hervorragend. Da kann man nicht meckern"  # change
    else:
        return "Diese Frage macht überhaupt keinen Sinn."


# Question
question = input("Frage: ")
answer = check_weather(question)
print(answer)
