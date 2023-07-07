#Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s 
#(кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
def var_changer(var_dict: dict):
    to_change = [i for i in var_dict if len(i) > 1 and i[-1] == 's']
    for i in to_change:
        var_dict[i[:-1]] = var_dict[i]
        var_dict[i] = None

datas = [42,-73,12,85,-15,2]
s = "hello world"
names = ('NoName','OtherName','NewName')
sx = 42

all_var = globals()

print(f"{datas = }\n{s = }\n{names = }\n{ sx = }")
var_changer(all_var)
print(f"{datas = }\n{s = }\n{names = }\n{ sx = }")
print(f"{data = }\n{name = }")