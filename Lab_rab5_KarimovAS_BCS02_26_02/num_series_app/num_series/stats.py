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


def summarize(data: Sequence[float]) -> dict[str, float]:
    """Сводка: количество значений, среднее, медиана, размах, min и max."""
    _ensure_not_empty(data)
    return {"count": len(data), "mean": mean(data), "median": median(data),
            "spread": spread(data), "min": float(min(data)), "max": float(max(data))}
