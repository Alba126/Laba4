#!/usr/bin/env python3
# -*- coding: utf-8 -*-

<<<<<<< HEAD
import sys


if __name__ == '__main__':
# Вводится число экзаменов 𝑁 ≤ 20. Напечатать фразу Мы успешно сдали N экзаменов, согласовав слово "экзамен" с числом.
    n_1 = int(input("Введите число экзаменов -> "))
    if n_1 == 1:
        print(f"Мы успешно сдали {n_1} экзамен")
    elif 2 <= n_1 <= 4:
        print(f"Мы успешно сдали {n_1} экзаменa")
    elif 5 <= n_1 <= 20:
        print(f"Мы успешно сдали {n_1} экзаменов")
    else:
        print("Ошибка", file=sys.stderr)
        exit(1)
=======
n = int(input('Мне>'));
def age_to_str(n):
    return "лет" \
        if n // 10 % 10 == 1 or n % 10 in {0, 5, 6, 7, 8, 9} \
        else 'год' \
        if n % 10 ==1 \
        else 'года'
    print(f' {n} {age_to_str(n)} ')
>>>>>>> 2207c82e66d12eb846e71c4a955d90212a492835
