#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k = input("Введите слово: ")
a = list(k)
x = '';
s = []
for i in a:
    if(a[i] == 'а' and a[i].isupper() == False):a[i] = "б"
    elif (a[i] == 'б' and a[i].isupper() == False): a[i] = "а"
    if (a[i] == 'А' and a[i].isupper() == True): a[i] = "Б"
    elif (a[i] == 'Б'and a[i].isupper() == True): a[i] = "А"
x = x.join(a)
print("Результат - ", x)