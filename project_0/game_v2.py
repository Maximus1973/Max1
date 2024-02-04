"""Игра "Угадай число"

Компьютер сам загадывает и сам угадывает число

"""

# Импортируем библиотеку numpy
import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное компьютером число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    # Инициализируем количество попыток
    attempt_count = 0
    
    # Инициализируем левую границу интервала поиска
    min_number = 1
    
    # Инициализируем правую границу интервала поиска
    max_number = 100
    
    # Создаем цикл по алгоритму бинарного поиска
    while min_number <= max_number:
        attempt_count += 1
        # Инициализируем предполагаемое число
        predict_number = (min_number + max_number) // 2
        
        # Сравниваем предполагемое число с числом, которое загадал компьютер
        if predict_number == number:
            # Если числа равны, выходим из цикла
            break
        elif predict_number < number:
            min_number = predict_number + 1
        else:
            max_number = predict_number - 1
    
    # Возвращаем количество попыток
    return attempt_count

def score_game(random_predict) -> int:
    """За какое среднее количество попыток при 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    # Инициализируем список для сохранения количества попыток
    count_list = []
    
    # Фиксируем сид для воспроизводимости
    np.random.seed(1)  
    
    # Инициализируем список из 1000 загаданных чисел
    random_array = np.random.randint(1, 101, size=(1000))

    # Создаем цикл для прохождения по списку загаданных чисел
    for number in random_array:
        count_list.append(random_predict(number))

    # Вычисляем среднее количество попыток
    score = int(np.mean(count_list))
    
    # Выводим результат
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    
    # Возвращаем среднее количество попыток
    return score


if __name__ == "__main__":
    # RUN (Запускаем программу)
    score_game(random_predict)
