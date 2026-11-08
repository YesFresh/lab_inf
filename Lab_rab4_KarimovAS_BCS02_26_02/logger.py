#Хранит сообщения об ошибках в памяти (для отчёта/анализа) и дублирует в файл.#
from __future__ import annotations
import datetime
from connstans import LOG_FILE

_entries: list[str] = []


def log_error(message: str):
    #Записать сообщение об ошибке ввода
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{ts}] {message}"
    _entries.append(entry)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except OSError:
        pass


def get_entries():
    #Вернуть копию журнала ошибок.#
    return list(_entries)


def clear():
    #Очистить журнал (используется в тестах).#
    _entries.clear()
