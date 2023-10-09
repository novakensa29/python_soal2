def bilangan_prima(n):
    angka_prima = []

    for x in range(2, n):
        prima = True
        for i in range(2, int(x//2)):
            if x % i == 0:
                prima = False
                break
        if prima:
            angka_prima.append(x)

    print("Bilangan prima yang lebih kecil dari", n, "adalah:")
    for prima in angka_prima:
        print(prima, end=" ")

n = int(input("Masukkan bilangan n: "))
bilangan_prima(n)

