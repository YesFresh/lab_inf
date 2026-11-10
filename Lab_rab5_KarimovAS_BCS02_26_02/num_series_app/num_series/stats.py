from typing import Dict, Sequence

def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт статистики невозможен")

"""Среднее арифметическое."""
def mean(data: Sequence[float]) -> float:
    _ensure_not_empty(data)
    return sum(data) / len(data)

"""Медиана (устойчива к выбросам)."""
def median(data: Sequence[float]) -> float:
    _ensure_not_empty(data)
    s = sorted(data)
    k = len(s) // 2
    if len(s) % 2:
        return float(s[k])
    return (s[k - 1] + s[k]) / 2.0

"""Размах ряда: max - min."""
def spread(data: Sequence[float]) -> float:
    _ensure_not_empty(data)
    return float(max(data) - min(data))

"""Сводный отчёт: count, mean, median, spread, min, max."""
def summarize(data: Sequence[float]) -> Dict[str, float]:
    _ensure_not_empty(data)
    return {
    "count": len(data),
    "mean": mean(data),
    "median": median(data),
    "spread": spread(data),
    "min": float(min(data)),
    "max": float(max(data)),
    }
