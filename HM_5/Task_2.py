# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["Данил", "Василий", "Иван"]
base_salary = [1500, 700, 1025]
premium = ["10%", "10.25%", "8.5%"]
print({name: int(sal) / 100 * float(per[:-1]) for name, sal, per in zip(names, base_salary, premium)})