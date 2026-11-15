# вводим изначальное время(часы, минуты, секунды)
hours = int(input("часы:"))
minutes = int(input("минуты:"))
sec = int(input("секунды:"))
minutes1 = hours*60
minutes2 = sec/60
# считаем это время в общей единице измерения(в минутах)
minutes3 = minutes + minutes1 + minutes2
print("минут:", minutes3)
print("Нужно проверить, сколько будет времени, если смотреть на 1,25х/1,50х/2х?")
while True:
        otime = float(input("ВЫБЕРИТЕ: 1.25, 1.50, 2:"))
        # из заданного количества минут считаем на выбранной скорости новое время.
        if otime == 1.25:
                alltime = minutes3 / 1.25
                allsec = alltime * 60
                newmins = allsec // 60
                newhours = newmins // 60
                newmins = newmins % 60
                newsec = allsec % 60
                print("Часов:", newhours, "Минут:", newmins, "Секунд:", newsec)
        elif otime == 1.50:
                alltime = minutes3 / 1.50
                allsec = alltime * 60
                newmins = allsec // 60
                newhours = newmins // 60
                newmins = newmins % 60
                newsec = allsec % 60 
                print("Часов:", newhours, "Минут:", newmins, "Секунд:", newsec)
        elif otime == 2:
                alltime = minutes3 / 2
                allsec = alltime * 60
                newmins = allsec // 60
                newhours = newmins // 60
                newmins = newmins % 60
                newsec = allsec % 60
                print("Часов:", newhours, "Минут:", newmins, "Секунд:", newsec)
