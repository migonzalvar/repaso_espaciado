# repaso_espaciado.py

MAZOS = {
    "Capitales": {
        "plantilla": "¿Cuál es la capital de {pregunta}?",
        "tarjetas": [("España", "Madrid"), ("Portugal", "Lisboa"), ("Francia", "París")],
    },
    "Coches": {
        "plantilla": "¿De qué país es {pregunta}?",
        "tarjetas": [("Tesla", "Estados Unidos")],
    },
    "Ríos": {
        "plantilla": "¿Dónde desemboca el {pregunta}?",
        "tarjetas": [("Miño", "Galicia")],
    },
}

while True:
    mazos_con_tarjetas = []
    for mazo in MAZOS:
        cantidad = len(MAZOS[mazo]["tarjetas"])
        if cantidad > 0:
            mazos_con_tarjetas.append(mazo)

    if len(mazos_con_tarjetas) == 0:
        break

    mazo_escogido = None
    while not mazo_escogido:
        print("Escoge un mazo:")
        for n, mazo in enumerate(mazos_con_tarjetas):
            cantidad = len(MAZOS[mazo]["tarjetas"])
            print(n, mazo, cantidad)

        selección = input("? ")
        print("[DEBUG]", f"{selección=}")

        índice = int(selección)
        print("[DEBUG]", f"{índice=}")

        try:
            mazo_escogido = mazos_con_tarjetas[índice]
        except IndexError:
            print("No entiendo.")

    print("Has seleccionado", mazo_escogido)

    tarjetas_en_mano = MAZOS[mazo_escogido]["tarjetas"]
    tarjetas_difíciles = []
    while len(tarjetas_en_mano) > 0:
        tarjeta = tarjetas_en_mano.pop(0)
        pregunta, respuesta = tarjeta
        plantilla = MAZOS[mazo_escogido]["plantilla"]
        mensaje = plantilla.format(pregunta=pregunta)
        input(f"{mensaje} Pulsa ENTER para comprobar la respuesta.")
        print(f"La respuesta es: {respuesta}.")
        valoración = input("¿1 Fácil / 2 Difícil / 3 Repetir? ")
        if valoración == "2":
            tarjetas_difíciles.append(tarjeta)
        elif valoración == "3":
            tarjetas_en_mano.append(tarjeta)

    MAZOS[mazo_escogido]["tarjetas"] = tarjetas_difíciles
