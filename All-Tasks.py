def task1():
    countries = { "Россия": "Москва", "Беларусь": "Минск", "Германия": "Берлин", "Япония": "Токио" }
    for key in countries:
        print(key, " - ", countries[key])

    a = input("Введите название страны для получения названия столицы: ")
    a = a.title()
    if a in countries.keys():
        print(f"Столица страны {a.title()} - {countries.get(a)}")
    else:
        print("Такой страны нет в списке")

    tmp = list(countries.keys())
    tmp.sort()
    print("Отсортированный словарь: ")
    for i in tmp:
        print(i, ':', countries[i])



def task2():
    alphabet = { 1: list("АВЕИНОРСТ"), 2: list("ДКЛМПУ"), 3: list("БГЁЬЯ"), 4: list("ЙЫ"), 5: list("ЖЗХЦЧ"),8: list("ШЭЮ"), 10: list("ФЩЪ") }

    word = input("Введите слово: ").upper()

    res = 0

    for i in word:
        for key, value in alphabet.items():
            if i in value:
                res += key
                break

    print(f"Стоимость слова '{word}' составляет {res} очков.")


tasks = (task1, task2)
index = int(input("Введите номер задания (от 1 до 2): "))

if 1 <= index <= 4:
    tasks[index - 1]()
else:
    print("Ошибка: введите номер от 1 до 2.")