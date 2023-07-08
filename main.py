# Task 3

# 1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
# 2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат
# Якщо будуть потрібні додаткові завдання - писати лс.

# Task 1

try:
    day_number = int(input("Pls input day number of the week: "))
    if day_number <= 7 and day_number >= 1:
        match day_number:
                case 1:
                    print("Monday")
                case 2:
                    print("Tuesday")
                case 3:
                    print("Wednesday")
                case 4:
                    print("Thursday")
                case 5:
                    print("Friday")
                case 6:
                    print("Saturday")
                case 7:
                    print("Sunday")
    else:
        print("Pls input integer from 1 to 7!")
except ValueError as val_error:
    print(f"Pls input only integer! {val_error}")
except Exception as any_error:
    print(f"Some error {Exception}")




