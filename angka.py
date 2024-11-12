def angka():
    while True:
        angka = int(input("Angka: "))
        if angka == 0:
            print("0 th")
            print("Bye bye:3")
            break

        if 10 <= angka % 100 <= 20:
            simbol = "th"
        else:
            angka_terakhir = angka % 10
            if angka_terakhir == 1:
                simbol = "st"
            elif angka_terakhir == 2:
                simbol = "nd"
            elif angka_terakhir == 3:
                simbol = "rd"
            else:
                simbol = "th"

        print(f"{angka} {simbol}")
angka()
