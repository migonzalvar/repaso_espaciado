# repaso_espaciado.py

mazos = ["Capitales", "Marcas de coche", "Ríos"]
print("Escoge un mazo:")
n = 0
for mazo in mazos:
    print(n, mazo)
    n = n + 1

selección = input("? ")
print("[DEBUG]", f"{selección=}")

índice = int(selección)
print("[DEBUG]", f"{índice=}")

print("Has seleccionado", mazos[índice])
