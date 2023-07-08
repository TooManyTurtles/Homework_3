# Task 3

# 1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
# 2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат
# Якщо будуть потрібні додаткові завдання - писати лс.

# Task 1
# 1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.

# try:
#     day_number = int(input("Pls input day number of the week: "))
#     if 7 < day_number or 1 > day_number:
#         print("Pls input integer from 1 to 7!")
#     else:
#         match day_number:
#                 case 1:
#                     print("Monday")
#                 case 2:
#                     print("Tuesday")
#                 case 3:
#                     print("Wednesday")
#                 case 4:
#                     print("Thursday")
#                 case 5:
#                     print("Friday")
#                 case 6:
#                     print("Saturday")
#                 case 7:
#                     print("Sunday")
# except ValueError:
#     print("Input only numbers!")
# except Exception:
#     print("Unknown Error")

# Task 2
# 2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

# try:
#     num1 = int(input("Input number 1: "))
#     num2 = int(input("Input number 2: "))
#     if num1 == num2:
#         print("Your numbers are equal!")
#     elif num1 < num2:
#         print(f"Your numbers ARE NOT equal. In ascending order: {num1} {num2}")
#     else:
#         print(f"Your numbers ARE NOT equal. In ascending order: {num2} {num1}")
# except ValueError:
#     print("Input only numbers!")
# except Exception:
#     print("Unknown Error")

# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат

try:
    num1 = int(input("Input number 1: "))
    num2 = int(input("Input number 2: "))
    math = input("Input one of actions: ")
    if math == "+" or math == "-" or math == "*" or math == "/":
        match math:
            case "+":
                print(f"The summ of your numbers is {num1 + num2}")
            case "-":
                print(f"The summ of your numbers is {num1 - num2}")
            case "*":
                print(f"The summ of your numbers is {num1 * num2}")
            case "/":
                print(f"The summ of your numbers is {num1 / num2}")
    else:
        print("Actions allowed: + - * /. Pls try again")
except ZeroDivisionError:
    print("Cant be divided by zero")
except ValueError:
    print("Input only numbers!")
except Exception:
    print("Unknown Error")