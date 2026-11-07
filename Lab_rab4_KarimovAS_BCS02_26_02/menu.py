"     *МЕНЮ*     "

from connstans import C_MASLO, C_STAL, C_WATER

from __future__ import annotations

def show_menu(): # показывает меню
    print(" введите вещество ")
    print("1 - вода")
    print("2 - масло")
    print("3 - сталь")
    print("0- exit")

def select_C():
    while True:
        vibor = input().strip()
        match vibor:
            case "1": return C_WATER
            case "2": return C_MASLO
            case "3": return C_STAL
            case "0": return None
            case _: print("Error")

