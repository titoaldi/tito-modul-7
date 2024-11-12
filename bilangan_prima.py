def angka_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

def cek_angka():
    while True:
        angka = float(input("Masukan angka(Ketik -1 untuk keluar):"))
        if angka == -1:
            break

        if angka_prima(angka):
            print(f"{angka} adalah bilangan prima.")
        else:
            print(f"{angka} bukan bilangan prima.")

cek_angka()

