import json

def get_user_level(level_input):
    with open('questions.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return questions.get(level_input, {})

def base_program(words):
    answers = {}
    for english_word, russian_word in words.items():
        user_answer = input(f"Как по-английски '{russian_word}'? ").lower()
        answers[english_word] = (user_answer == english_word)
    return answers

def get_result(answers, knowledge_level):
    correct = {word: correct for word, correct in answers.items() if correct}
    incorrect = {word: not correct for word, correct in answers.items() if not correct}

    print("\nПравильные ответы:")
    for word in correct:
        print(f"- {word}")

    print("\nНеправильные ответы:")
    for word in incorrect:
        print(f"- {word}")

    score = len(correct) / len(answers) * 100
    return score
