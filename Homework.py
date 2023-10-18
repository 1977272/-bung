# Just doing the homework
# FUnktion zur Erstellung der Frage nach dem Wetter
def check_weather(question):
    if question.lower() == "wie ist das wetter?":
        return "Das Wetter ist hervorragend"
    else:
        return "Lass mich in Ruhe."


# Frage
question = input("Frage: ")
answer = check_weather(question)
print(answer)
