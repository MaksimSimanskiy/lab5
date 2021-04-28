#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k = input("Введите предложение: ")
b=0
for i in range(len(k)-1):
    if k[i] == k[i+1]: b += 2
print('Одинаковых соседних букв = ', b)


