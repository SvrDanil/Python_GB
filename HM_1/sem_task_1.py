# Вывести в консоль таблицу умножения как на школьной тетрадке.
first = 2
last = 10
half = 2

for i in range(first, last):
    for j in range(first, last // half + 1):
        print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
    print()
print()
for i in range(first, last):
    for j in range(last // half + 1, last):
        print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
    print()