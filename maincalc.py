hours = int(input("часы:"))
minutes = int(input("минуты:"))
sec = int(input("секунды:"))
minutes1 = hours*60
minutes2 = sec//60
minutes3 = minutes + minutes1 + minutes2
print("минут:", minutes3)
print("Нужно проверить, сколько будет времени, если смотреть на 1,25х/1,50х/2х?")
while True:
        otime = float(input("ВЫБЕРИТЕ: 1.25, 1.50, 2:"))
        if otime == 1.25:
                otime = minutes3 // 1.25
                otime1 = otime // 60
                print("минут:", otime, "часов:", otime1)
        elif otime == 1.50:
                otime = minutes3 // 1.50
                otime1 = otime // 60
                print("минут:", otime, "часов:", otime1)
        elif otime == 2:
                otime = minutes3 // 2
                otime1 = otime // 60
                print("минут:", otime, "часов:", otime1)