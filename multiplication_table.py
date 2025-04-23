import random
import time
def print_welcome():
    print("=" * 50)
    print("ТРЕНАЖЕР ТАБЛИЦЫ УМНОЖЕНИЯ")
    print("=" * 50)
    print("Эта программа поможет вам выучить таблицу умножения.")
    print("Вам будут предложены примеры, на которые нужно дать ответ.")
    print("=" * 50)
def choose_difficulty():
    print("\nВыберите уровень сложности:")
    print("1. Легкий (таблица умножения на 1-5)")
    print("2. Средний (таблица умножения на 1-9)")
    print("3. Сложный (таблица умножения на 1-12)")
    while True:
        try:
            choice = int(input("Ваш выбор (1-3): "))
            if choice == 1:
                return 5
            elif choice == 2:
                return 9
            elif choice == 3:
                return 12
            else:
                print("Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Пожалуйста, введите число.")
def choose_number_of_questions():
    while True:
        try:
            num = int(input("\nСколько примеров вы хотите решить? (5-20): "))
            if 5 <= num <= 20:
                return num
            else:
                print("Пожалуйста, выберите число от 5 до 20.")
        except ValueError:
            print("Пожалуйста, введите число.")

def generate_question(max_number):
    a = random.randint(1, max_number)
    b = random.randint(1, max_number)
    return a, b, a * b

def run_test(max_number, num_questions):
    correct_answers = 0
    questions = []
    
    # Генерируем все вопросы заранее
    for _ in range(num_questions):
        questions.append(generate_question(max_number))
    
    # Перемешиваем вопросы
    random.shuffle(questions)
    
    print("\nНачинаем тест! Для выхода введите 'q'.")
    print("=" * 50)
    
    start_time = time.time()
    
    for i, (a, b, correct) in enumerate(questions, 1):
        print(f"\nВопрос {i} из {num_questions}:")
        print(f"{a} × {b} = ?")
        
        try:
            user_answer = input("Ваш ответ: ")
            if user_answer.lower() == 'q':
                print("Тест прерван.")
                break
                
            user_answer = int(user_answer)
            
            if user_answer == correct:
                print("Правильно! ✓")
                correct_answers += 1
            else:
                print(f"Неправильно. ✗ Правильный ответ: {correct}")
                
        except ValueError:
            print(f"Неправильный ввод. Правильный ответ: {correct}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return correct_answers, i, elapsed_time

def show_results(correct, total, time_taken):
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ ТЕСТА")
    print("=" * 50)
    
    if total > 0:
        percentage = (correct / total) * 100
        print(f"Правильных ответов: {correct} из {total} ({percentage:.1f}%)")
        print(f"Затраченное время: {time_taken:.1f} секунд")
        
        if percentage == 100:
            print("\nОтлично! Вы знаете таблицу умножения идеально!")
        elif percentage >= 80:
            print("\nХороший результат! Продолжайте практиковаться.")
        elif percentage >= 60:
            print("\nНеплохо, но нужно больше практики.")
        else:
            print("\nСтоит уделить больше времени изучению таблицы умножения.")
    else:
        print("Тест не был завершен.")

def play_again():
    while True:
        choice = input("\nХотите попробовать еще раз? (да/нет): ").lower()
        if choice in ['да', 'д', 'yes', 'y']:
            return True
        elif choice in ['нет', 'н', 'no', 'n']:
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

def main():
    print_welcome()
    
    while True:
        max_number = choose_difficulty()
        num_questions = choose_number_of_questions()
        
        correct, total, time_taken = run_test(max_number, num_questions)
        show_results(correct, total, time_taken)
        
        if not play_again():
            print("\nСпасибо за использование тренажера таблицы умножения! До свидания!")
            break

if __name__ == "__main__":
    main()