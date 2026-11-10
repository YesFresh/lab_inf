def check_window(window: int, n: int) -> None:
    """
    Валидация размера окна для скользящего среднего.
    """
    if not isinstance(window, int) or window < 1:
        raise ValueError("Размер окна должен быть целым числом больше или равным 1.")
    if window > n:
        raise ValueError(f"Размер окна ({window}) не может превышать длину ряда ({n}).")


    """
    Простая скользящая средняя (SMA), оптимизированная через бегущую сумму (O(n)).
    """
def simple_moving_average(data: list[float | int], window: int) -> list[float]:
    n = len(data)
    check_window(window, n)

    # Вычисляем сумму для первого окна
    running_sum = sum(data[:window])
    result = [running_sum / window]
    for i in range(window, n):  # Сдвигаем окно, добавляя новый элемент и вычитая ушедший
        running_sum += data[i] - data[i - window]
        result.append(running_sum / window)
    return result



def centered_moving_average(data: list[float | int], window: int) -> list[float | None]:
    if window % 2 == 0:
        raise ValueError("Размер окна для центрированной скользящей средней должен быть нечётным.")
    n = len(data)
    check_window(window, n)
    sma_values = simple_moving_average(data, window)    # Вычисляем SMA
    radius = window // 2    # Радиус окна с одной стороны
    padding = [None] * radius   # Формируем итоговый массив, центрируя значения с помощью None по краям
    return padding + sma_values + padding


def exponential_moving_average(data: list[float | int], alpha: float) -> list[float]:
    if not (0 < alpha <= 1):
        raise ValueError("Параметр сглаживания alpha должен быть в диапазоне (0, 1].")
    if not data:
        return []
    result = [float(data[0])]
    for i in range(1, len(data)):
        ema_val = alpha * data[i] + (1 - alpha) * result[-1]
        result.append(ema_val)
    return result
