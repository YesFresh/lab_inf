from validation import input_mass, input_temp1, input_deT, input_temp2
from menu import show_menu, select_C
def main():
    print("Расчёт теплоты на нагрев технологической среды")

    while True:
        show_menu()
        k = select_C()
        if k == None:
            print("Остановка")
            break
        m = input_mass()
        t1 = input_temp1()
        t2 = input_temp2()
        dt = input_deT()
        