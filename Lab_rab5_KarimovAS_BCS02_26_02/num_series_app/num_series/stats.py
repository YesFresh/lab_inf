"""Ручной расчёт базовых статистических показателей."""
from typing import Sequence


def _ensure_not_empty(data: Sequence[float]) -> None:
    if len(data) == 0:
        raise ValueError("Ряд пуст: расчёт статистики невозможен")


def mean(data: Sequence[float]) -> float:
    """Среднее арифметическое."""
    _ensure_not_empty(data)
    return float(sum(data) / len(data))


def median(data: Sequence[float]) -> float:
    """Медиана упорядоченного ряда."""
    _ensure_not_empty(data)
    values = sorted(data)
    middle = len(values) // 2
    if len(values) % 2:
        return float(values[middle])
    return float((values[middle - 1] + values[middle]) / 2.0)


def spread(data: Sequence[float]) -> float:
    """Размах ряда: максимум минус минимум."""
    _ensure_not_empty(data)
    return float(max(data) - min(data))


def abs_spread(data: Sequence[float]) -> float: #Разность max - min по модулю
    _ensure_not_empty(data)
    return float(abs(max(data) - min(data)))


def minmax_indices(data: Sequence[float]) -> tuple[int, int]: #Возвращает индекс минимума и индекс максимума
    _ensure_not_empty(data)
    min_idx = 0
    max_idx = 0
    for i, val in enumerate(data):
        if val < data[min_idx]:
            min_idx = i
        if val > data[max_idx]:
            max_idx = i
    return min_idx, max_idx


def summarize(data: Sequence[float]) -> dict[str, float | int]: #Сводка показателей ряда
    _ensure_not_empty(data)
    min_val = float(min(data))
    max_val = float(max(data))
    min_idx, max_idx = minmax_indices(data)
    return {"count": len(data),"mean": mean(data),
            "median": median(data),"spread": spread(data),
            "abs_spread": abs_spread(data),
            "min": min_val,"max": max_val,
            "min_index": min_idx,"max_index": max_idx,}
