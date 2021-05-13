#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
k = input("Введите предложение: ")
print("Количество повторяющихся символов",len(re.findall(r"(.)\1", k)))

# print('Одинаковых соседних букв = ', b)


