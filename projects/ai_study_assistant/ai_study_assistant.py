from multiple_choice_question import MultipleChoiceQuestion


multiple_choice_question: MultipleChoiceQuestion = MultipleChoiceQuestion(subject = "Computer Science",
                                question = "What does CPU stand for?",
                                answer = "Central Processing Unit",
                                max_mark = 1,
                                choices = [
                                    "Central Processing Unit",
                                    "Computer Processing Utility",
                                    "Central Program Unit",
                                    "Computer Power Unit"
                                ]
                                )

print(multiple_choice_question.display_question())
print(multiple_choice_question.evaluate_answer("Central rocessing Unit"))


