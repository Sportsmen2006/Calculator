# Функция для преобразования строки в токены
def tokenize(input_string): # функция, которая разбивает текст на токены
    words = input_string.split() # разбивает строку на список элементов
    dictionary = {
        'один': ('N', 1), 'два': ('N', 2), 'три': ('N', 3), 'четыре': ('N', 4), 'пять': ('N', 5), 'шесть': ('N', 6),
        'семь': ('N', 7), 'восемь': ('N', 8), 'девять': ('N', 9), 'десять': ('N', 10), 'одиннадцать': ('N', 11),
        'двенадцать': ('N', 12), 'тринадцать': ('N', 13), 'четырнадцать': ('N', 14), 'пятнадцать': ('N', 15),
        'шестнадцать': ('N', 16), 'семнадцать': ('N', 17), 'восемнадцать': ('N', 18), 'девятнадцать': ('N', 19),
        'двадцать': ('N', 20), 'тридцать': ('N', 30), 'сорок': ('N', 40), 'пятьдесят': ('N', 50),
        'шестьдесят': ('N', 60), 'семьдесят': ('N', 70), 'восемьдесят': ('N', 80), 'девяносто': ('N', 90),
        'плюс': ('O', '+'), 'минус': ('O', '-'), 'умножить': ('O', '*'), 'скобка': ('E', ''),
        'открывается': ('O', '('), 'закрывается': ('O', ')'), 'на': ('E', '')
    }
    tokens = [] # создаем пустой список
    for word in words: # делаем перебор
        if word in dictionary: # если элемент есть в словаре
            tokens.append(dictionary[word]) # добавляем в пустой список словарь, который индексирован
        else:
            tokens.append('Unknown') # если будет другое слово, которое не встречается в словаре
    return tokens # возвращаем пременную

# Функция для преобразования токенов в список для вычислений
def parse_tokens(tokens):
    parsed_result = []
    is_number = False
    current_number = 0
    for token in tokens:
        if token[0] == 'N':  # Если токен - число
            is_number = True
            current_number += token[1]
        else:
            if is_number:
                parsed_result.append(current_number)
                current_number = 0
            is_number = False
            if token[0] == 'O':  # Если токен - оператор
                parsed_result.append(token[1])
    if is_number:
        parsed_result.append(current_number)
    return parsed_result

# Функция для преобразования числа в текст
def number_to_words(number):
    result = ''
    number_names = [
        'ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
        'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
        'восемнадцать', 'девятнадцать'
    ]
    tens_names = [
        '', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'
    ]
    if abs(number) >= 100:
        return 'Переполнение'
    if number < 0:
        result = 'минус '
        number = -number
    if number < 20:
        result += number_names[number]
        return result
    tens = number // 10
    units = number % 10
    result += tens_names[tens]
    if units != 0:
        result += ' ' + number_names[units]
    return result.strip()

# Главная функция для вычисления результата
def calculate(input_string):
    tokens = tokenize(input_string)
    if 'Unknown' in tokens:
        return 'Неизвестное слово'
    parsed_expression = parse_tokens(tokens)
    expression_string = ''
    for element in parsed_expression:
        expression_string += str(element)
    try:
        result = eval(expression_string)
    except:
        return 'Ошибка в выражении'
    return number_to_words(result)

# Пример использования
expression_1 = 'сорок два плюс десять '
expression_2 = 'скобка открывается пять плюс два скобка закрывается умножить на три минус один'
print(calculate(expression_1))
print(calculate(expression_2))






