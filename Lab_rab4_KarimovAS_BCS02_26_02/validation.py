from __future__ import annotations

from connstans import M_MAX, M_MIN, T1_MAX, T1_MIN, T2_MAX, T2_MIN
from logger import log_error

def validate_range(value: float, low: float, high: float):
    """
    Проверка попадания value в [low, high] через if-elif-else.
    :return: (True, "") или (False, сообщение)
    """
    if value < low: return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high: return False, f"Ошибка: значение больше верхней границы ({high})."
    else: return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """
    Циклически запрашивать число, пока не будет корректного.
    Проверяет тип (float) через try/except ValueError и границы.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_mass():
    return input_number(
        "Введите массу (от 01 до 1000): ",
        M_MIN, M_MAX,
    )


def input_temp1():
    return input_number(
        "Введите Т1 (-50 до 100)",
        T1_MIN, T1_MAX,
    )

def input_temp2():
    return input_number(
        "Введите Т2 (0 до 1000)",
        T2_MIN, T2_MAX,
    )

def input_deT():
    while True:
        t1 = input_temp1()
        t2 = input_temp2()
        if t2 > t1:
            return t1, t2
        msg = f"Ошибка: Температура T2 ({t2}) должна быть строго больше Т1 ({t1})."
        print(msg + " Повторите ввод температур.")
        log_error(msg)