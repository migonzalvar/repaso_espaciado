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
    print("[DEBUG]", f"{MAZOS=}")
    print("Escoge un mazo:")

    todos_los_mazos = list(MAZOS.keys())
    mazos_con_preguntas = []
    for mazo in todos_los_mazos:
        if len(MAZOS[mazo]["tarjetas"]) > 0:
            mazos_con_preguntas.append(mazo)

    for n, mazo in enumerate(mazos_con_preguntas):
        print(n, mazo)

    selección = input("? ")
    print("[DEBUG]", f"{selección=}")

    índice = int(selección)
    print("[DEBUG]", f"{índice=}")

    nombre_de_mazo = mazos_con_preguntas[índice]

    print("Has seleccionado", nombre_de_mazo)

    tarjetas_en_mano = MAZOS[nombre_de_mazo]["tarjetas"]
    tarjetas_difíciles = []
    while len(tarjetas_en_mano) > 0:
        tarjeta = tarjetas_en_mano.pop(0)
        pregunta, respuesta = tarjeta
        plantilla = MAZOS[nombre_de_mazo]["plantilla"]
        mensaje = plantilla.format(pregunta=pregunta)
        input(f"{mensaje} Pulsa ENTER para comprobar la respuesta.")
        print(f"La respuesta es: {respuesta}.")
        valoración = input("¿1 Fácil / 2 Difícil / 3 Repetir? ")
        if valoración == "2":
            tarjetas_difíciles.append(tarjeta)
        elif valoración == "3":
            tarjetas_en_mano.append(tarjeta)

    MAZOS[nombre_de_mazo]["tarjetas"] = tarjetas_difíciles
