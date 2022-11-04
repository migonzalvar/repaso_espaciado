# repaso_espaciado.py

mazos = ["Capitales", "Marcas de coche", "Ríos"]
print("Escoge un mazo:")
for n, mazo in enumerate(mazos):
    print(n, mazo)

selección = input("? ")
print("[DEBUG]", f"{selección=}")

índice = int(selección)
print("[DEBUG]", f"{índice=}")

print("Has seleccionado", mazos[índice])

if índice == 0:
    tarjetas = [
        ("España", "Madrid"),
        ("Portugal", "Lisboa"),
        ("Francia", "París"),
    ]

    for indice in range(len(tarjetas)):
        tarjeta = tarjetas.pop()
        pregunta, respuesta = tarjeta
        input(f"¿Cuál es la capital de {pregunta}? Pulsa ENTER para comprobar la respuesta.")
        print(f"La respuesta es: {respuesta}.")
        valoración = input("¿1 Fácil /2 Difícil/ 3 Repetir? ")

elif índice == 1:
    ...
else:
    print("Mazo no disponible")
