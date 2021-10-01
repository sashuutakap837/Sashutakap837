# -*- coding: utf-8 -*-

print("Введите кол-во секунд")
seconds = int(input())

days = seconds / 86400
hours = seconds &  84600 // 3600
minutes = seconds % 84600 % 3600 // 60
sec = seconds % 86400 % 3600 // 60

print (days ,'дней:', hours ,'часов:', minutes ,'минут:', sec,'секунд')