from functions import get_user_level, base_program, get_result

user_name = input("Введите ваше имя: ")
user_lvl = input("Выберите уровень сложности \nлегкий, средний, сложный: ").lower()

test_words = get_user_level(user_lvl)
if not test_words:
    print("Недопустимый уровень сложности.")
else:
    test_answers = base_program(test_words)
    result = get_result(test_answers, test_words)

    print(f"\n{user_name}, ваш ранг: {result:.2f}%")
