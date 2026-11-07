# ___ Удельная теплоёмкость ___
C_WATER: float = 4200.0    # Вода
C_MASLO: float = 2000.0     # Масло
C_STAL: float = 500.0   # Сталь

# ___ лимиты ___
M_MIN: float = 0.1
M_MAX: float = 1000.0
T1_MIN: float = -50.0
T1_MAX: float = 100.0
T2_MIN: float = 0.0
T2_MAX: float = 1000.0

# ___ значения для определения типа нагрева ___
T_SMALL_GREW: float = 10.0
T_BIG_GREW: float = 100.0

# ___ Логи ___
LOG_FILE: str = "input_errors.log"