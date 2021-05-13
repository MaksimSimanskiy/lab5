#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input("Введите предложение: ")
g = s.split(' ')
for i  in g:
    if( g[i].find('к') == 0):
        print(g[i])
        break

