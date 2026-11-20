"""Алгоритмы скользящего среднего."""
from typing import Sequence
import time 
from collections import deque 
from typing import List, Sequence 

def _check_window(data: Sequence[float], window: int) -> None:
    if isinstance(window, bool) or not isinstance(window, int) or window < 1:
        raise ValueError("window должно быть положительным целым числом")
    if window > len(data):
        raise ValueError("window не может быть больше длины ряда")


def simple_moving_average(data: Sequence[float], window: int) -> list[float]:
    """SMA с бегущей суммой; время работы O(n)."""
    _check_window(data, window)
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return [float(x) for x in result]


def centered_moving_average(data: Sequence[float], window: int) -> list[float]:
    """Средние по нечётным окнам, размещённые по центру окна.

    Возвращает n-window+1 значений; каждое соответствует центру своего окна.
    """
    _check_window(data, window)
    if window % 2 == 0:
        raise ValueError("Для центрированной MA требуется нечётное window")
    return simple_moving_average(data, window)


def exponential_moving_average(data: Sequence[float], alpha: float) -> list[float]:
    """EMA: первое значение равно data[0], далее применяется рекурсия."""
    if len(data) == 0:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")
    if not isinstance(alpha, (int, float)) or isinstance(alpha, bool) or not 0 < alpha <= 1:
        raise ValueError("alpha должен удовлетворять условию 0 < alpha <= 1")
    result = [float(data[0])]
    for value in data[1:]:
        result.append(float(alpha * value + (1 - alpha) * result[-1]))
    return result

def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]: 
    """SMA с использованием deque (двусторонней очереди).""" 
    check_window(window, len(data)) 
    result = [] 
    d = deque() 
    running_sum = 0.0 
    for x in data: 
        d.append(x) 
        running_sum += x 
        if len(d) > window: 
            running_sum -= d.popleft() 
        if len(d) == window: 
            result.append(running_sum / window) 
    return result

def benchmark_moving_average(data: Sequence[float], window: int, repeats: int = 1000) -> dict: 
    
    """ 
    Замеряет среднее время выполнения SMA для реализаций на list и deque. 
    Возвращает словарь с ключами 'list' и 'deque' (время в секундах). 
    """ 

    # Проверка корректности окна (выбросит ValueError при необходимости) 
    check_window(window, len(data)) 

    # Замер для list-реализации (существующая simple_moving_average) 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average(data, window) 
    t_list = (time.perf_counter() - t0) / repeats 

    # Замер для deque-реализации 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average_deque(data, window) 
    t_deque = (time.perf_counter() - t0) / repeats 
    return {"list": t_list, "deque": t_deque}