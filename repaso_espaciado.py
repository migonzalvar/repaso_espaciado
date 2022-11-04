# repaso_espaciado.py

mazos = ["Capitales", "Marcas de coche", "Ríos"]
tarjetas_iniciales = [
    ("España", "Madrid"),
    ("Portugal", "Lisboa"),
    ("Francia", "París"),
]

while True:
    print("Escoge un mazo:")
    for n, mazo in enumerate(mazos):
        print(n, mazo)

    selección = input("? ")
    print("[DEBUG]", f"{selección=}")

    índice = int(selección)
    print("[DEBUG]", f"{índice=}")

    print("Has seleccionado", mazos[índice])

    if índice == 0:
        tarjetas_en_mano = tarjetas_iniciales
        tarjetas_difíciles = []
        while len(tarjetas_en_mano) > 0:
            tarjeta = tarjetas_en_mano.pop(0)
            pregunta, respuesta = tarjeta
            input(f"¿Cuál es la capital de {pregunta}? Pulsa ENTER para comprobar la respuesta.")
            print(f"La respuesta es: {respuesta}.")
            valoración = input("¿1 Fácil / 2 Difícil / 3 Repetir? ")
            if valoración == "2":
                tarjetas_difíciles.append(tarjeta)
            elif valoración == "3":
                tarjetas_en_mano.append(tarjeta)

        tarjetas_iniciales = tarjetas_difíciles

    elif índice == 1:
        ...
    else:
        print("Mazo no disponible")
