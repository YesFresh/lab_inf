        # Валидация
from __future__ import annotations

from connstans import M_MAX, M_MIN, T1_MAX, T1_MIN, T2_MAX, T2_MIN
from logger import log_error


def validate_range(value: float, low: float, high: float):
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float,
                 greater_than: float | None = None):        #проверка на число 

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
        if not ok:
            print(msg + " Повторите ввод.")
            log_error(msg)
            continue

        if greater_than is not None and not value > greater_than:
            msg = (f"Ошибка: значение ({value}) должно быть строго больше "
                   f"начальной температуры t1 ({greater_than}).")
            print(msg + " Повторите ввод.")
            log_error(msg)
            continue
        return value


def input_mass():   # Ввод массы 
    return input_number("Введите массу m, кг (0.1..1000): ", M_MIN, M_MAX)



def input_temp1():  # Ввод начальной температуры t1
    return input_number("Введите начальную температуру t1, °C (-50..100): ",
                        T1_MIN, T1_MAX)

def input_temp2(t1: float):     #Ввод конечной температуры t2 с проверкой на t2 > t1
    return input_number(
        f"Введите конечную температуру t2, °C (0..1000, t2 > {t1}): ",
        T2_MIN, T2_MAX, greater_than=t1,
    )
