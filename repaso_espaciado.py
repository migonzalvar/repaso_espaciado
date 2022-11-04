# repaso_espaciado.py

mazos = {
    "Capitales": [("España", "Madrid"), ("Portugal", "Lisboa"), ("Francia", "París")],
    "Coches": [("Tesla", "Estados Unidos")],
    "Ríos": [],
}

while True:
    print("Escoge un mazo:")
    nombre_de_mazos = list(mazos.keys())
    for n, mazo in enumerate(nombre_de_mazos):
        print(n, mazo)

    selección = input("? ")
    print("[DEBUG]", f"{selección=}")

    índice = int(selección)
    print("[DEBUG]", f"{índice=}")

    nombre_de_mazo = nombre_de_mazos[índice]

    print("Has seleccionado", nombre_de_mazo)

    tarjetas_en_mano = mazos[nombre_de_mazo]
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

    mazos[nombre_de_mazo] = tarjetas_difíciles
