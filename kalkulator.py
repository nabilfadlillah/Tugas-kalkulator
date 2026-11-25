import math

print("=== KALKULATOR ===")
print("Pilihan Operator:")
print("- Aritmatika: +, -, *, /, %")
print("- Pangkat: ** atau pangkat")
print("- kuadrat, akar, sin, cos, tan")
print("-----------------------------------")

opr = input("Masukkan operator: ")

if opr in ["+", "-", "*", "/", "%", "**", "pangkat"]:
    bil1 = float(input("bil 1 = "))
    bil2 = float(input("bil 2 = "))

    if opr == "+":
        print(bil1, "+", bil2, "=", bil1 + bil2)
    elif opr == "-":
        print(bil1, "-", bil2, "=", bil1 - bil2)
    elif opr == "*":
        print(bil1, "x", bil2, "=", bil1 * bil2)
    elif opr == "/":
        if bil2 != 0:
            print(bil1, ":", bil2, "=", bil1 / bil2)
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    elif opr == "%":
        print(bil1, "%", bil2, "=", bil1 % bil2)
    elif opr in ["**", "pangkat"]:
        print(bil1, "^", bil2, "=", bil1**bil2)

elif opr in ["kuadrat", "akar", "sin", "cos", "tan"]:
    bil1 = float(input("Masukkan nilai / sudut = "))

    if opr == "kuadrat":
        print(bil1, "^2 =", bil1**2)
    elif opr == "akar":
        if bil1 >= 0:
            print("Akar dari", bil1, "=", math.sqrt(bil1))
        else:
            print("Error: Tidak dapat menghitung akar dari bilangan negatif.")
    elif opr == "sin":
        hasil = math.sin(math.radians(bil1))
        if abs(hasil) < 1e-10:
            hasil = 0
        print(f"sin({bil1}°) =", hasil)
    elif opr == "cos":
        hasil = math.cos(math.radians(bil1))
        if abs(hasil) < 1e-10:
            hasil = 0
        print(f"cos({bil1}°) =", hasil)
    elif opr == "tan":
        if bil1 % 180 == 90:
            print(f"tan({bil1}°) = Tidak terhingga (Infinity)")
        else:
            hasil = math.tan(math.radians(bil1))
            if abs(hasil) < 1e-10:
                hasil = 0
            print(f"tan({bil1}°) =", hasil)

else:
    print("Error: Operator tidak dikenali.")