from quiz import Question
question_prompts=[
    "Какого цвета яблоки?\n  (a)красные\n  (b)зеленые\n (c) желтые\n\n",
    "Какого цвета клубника?\n  (a) розовая\n  (b)красная\n  (c)желтая\n\n",
    "какого цвета компьютера?\n  (a)серый\n  (b)черный\n  (c)золотистый\n\n"
]

questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"c"),
]

def run_test(questions):
    score=0
    for question in questions:
        otvet=input(question.vopros)
        if otvet==question.otvet:
            score+=1

    print(f"У вас  {score} из  {len(questions)} верны!")

run_test(questions)

