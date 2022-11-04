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
    preguntas = ["España", "Portugal", "Francia"]
    respuestas = ["Madrid", "Lisboa", "París"]

    for pregunta, respuesta in zip(preguntas, respuestas):
        input(f"¿Cuál es la capital de {pregunta}? Pulsa ENTER para comprobar la respuesta.")
        print(f"La respuesta es: {respuesta}.")
        valoración = input("¿Fácil/Difícil/Repetir? ")

elif índice == 1:
    ...
else:
    print("Mazo no disponible")
