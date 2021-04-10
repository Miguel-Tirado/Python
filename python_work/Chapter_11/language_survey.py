from survey import AnonymousSurvey

# define a question, and make a survey.
question = "What langauge did you first learn?"
my_survey = AnonymousSurvey(question)

# show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()