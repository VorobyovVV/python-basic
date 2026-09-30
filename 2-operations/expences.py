food = float(input("Введите сколько потратили на еду: "))
transport = float(input("Введите сколько потратили на транспорт: "))
entertainment = float(input("Введите сколько потратили на развлечения: "))

summary = food + transport + entertainment
average = summary / 3

print(summary, average)