# Меню выбора среды через match case
from __future__ import annotations

from connstans import C_MASLO, C_STAL, C_WATER


def show_menu():
    #Вывести меню сред
    print("1 - вода c = 4200 ")
    print("2 - масло c = 2000 ")
    print("3 - сталь c = 500 ")
    print("0 - выход")


def select_C():
    while True:
        choice = input("Введите номер среды (от 0 до 3): ").strip()
        match choice:
            case "1":
                return "вода", C_WATER
            case "2":
                return "масло", C_MASLO
            case "3":
                return "сталь", C_STAL
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")
