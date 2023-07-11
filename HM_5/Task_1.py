# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path(path):
    *path, file_name, file_extension = path.replace('.', '\\').split('\\')
    path = '\\'.join(path)
    return path, file_name, file_extension


raw_path = "C:\\Users\\user1\\Projects\\Python\\Homework\\Seminar_5\\task_1.py"
print("path = {}\nfile_name = {}\nfile_extension = {}".format(*split_path(raw_path)))