#Расчёт теплоты на нагрев технологической среды (вариант 3).#
from menu import select_C, show_menu
from operations import Q_raschet, det_t, heating_class
from validation import input_mass, input_temp1, input_temp2


def main():
    #Главный сценарий.#
    print("Расчёт теплоты на нагрев технологической среды (вариант 3)")

    while True:
        show_menu()
        medium = select_C()
        if medium is None:
            print("Работа завершена")
            break
        name, c = medium

        m = input_mass()
        t1 = input_temp1()
        t2 = input_temp2(t1)

        dt = det_t(t1, t2)
        q = Q_raschet(m, c, dt)
        cls = heating_class(dt)

        print(f"Среда:          {name} (c = {c:g} )")
        print(f"масса:          {m:g} кг")
        print(f"t1 -> t2:        {t1:g} *C -> {t2:g} *C (dt = {dt:g} *C)")
        print(f"Q (теплота):    {q:.2f} Дж")
        print(f"Класс нагрева:  {cls}")


if __name__ == "__main__":
    main()
