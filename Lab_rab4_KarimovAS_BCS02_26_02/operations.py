#Расчёты: изменение температуры, теплота нагрева, класс нагрева.#
from typing import Annotated

from connstans import T_BIG_GREW, T_SMALL_GREW


def det_t(
    t1: Annotated[float, "Начальная температура, °C"],
    t2: Annotated[float, "Конечная температура, °C"],
):
    #Изменение температуры dt = t2 - t1
    return t2 - t1


def Q_raschet(
    m: Annotated[float, "масса"],
    c: Annotated[float, "Удельная теплоёмкость"],
    dt: Annotated[float, "Изменение температуры"],
):
    #Теплота на нагрев Q = m * c * dt
    return m * c * dt


def heating_class(dt: Annotated[float, "Δt, °C"]):
    #dt < 10 - малый 10 ≤ dt ≤ 100 - нормальный dt > 100 - интенсивный
    if dt < T_SMALL_GREW:
        return "малый нагрев"
    elif dt <= T_BIG_GREW:
        return "нормальный нагрев"
    else:
        return "интенсивный нагрев"
