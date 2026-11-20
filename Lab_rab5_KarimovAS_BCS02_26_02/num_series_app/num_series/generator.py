"""Генераторы случайных и детерминированных числовых рядов."""
import math
import random
from typing import Optional


def _validate_n(n: int) -> None:
    """Проверяет, что количество точек — положительное целое число."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError(f"n должно быть положительным целым числом (получено: {n!r})")


def random_series(n: int, low: float = -100.0, high: float = 100.0,
                  seed: Optional[int] = None) -> list[float]:
    """Формирует n равномерно распределённых значений на [low, high]."""
    _validate_n(n)
    if not math.isfinite(low) or not math.isfinite(high) or low >= high:
        raise ValueError("Границы должны быть конечными числами, low < high")
    rng = random.Random(seed)
    return [rng.uniform(low, high) for _ in range(n)]


def sine_series(n: int, amplitude: float = 1.0, frequency: float = 1.0,
                noise: float = 0.0, seed: Optional[int] = None) -> list[float]:
    """Синусоидальный ряд с равномерным аддитивным шумом."""
    _validate_n(n)
    if not all(math.isfinite(x) for x in (amplitude, frequency, noise)) or noise < 0:
        raise ValueError("Параметры должны быть конечными, noise не может быть отрицательным")
    rng = random.Random(seed)
    return [amplitude * math.sin(2 * math.pi * frequency * i / n)
            + (rng.uniform(-noise, noise) if noise else 0.0) for i in range(n)]


def trend_series(n: int, start: float = 0.0, step: float = 1.0,
                 noise: float = 0.0, seed: Optional[int] = None) -> list[float]:
    """Линейный тренд с возможным равномерным шумом."""
    _validate_n(n)
    if not all(math.isfinite(x) for x in (start, step, noise)) or noise < 0:
        raise ValueError("Параметры должны быть конечными, noise не может быть отрицательным")
    rng = random.Random(seed)
    return [start + step * i + (rng.uniform(-noise, noise) if noise else 0.0)
            for i in range(n)]
