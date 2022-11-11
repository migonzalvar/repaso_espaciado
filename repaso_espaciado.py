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

def obtén_valoración():
    texto = "¿1 Fácil / 2 Difícil / 3 Repetir? "
    opciones = ["1", "2", "3"]
    valor = input(texto)
    while valor not in opciones:
        print("El valor no es correcto, vuelve a intenterlo.")
        valor = input(texto)
    return valor

def imprime_tarjeta(plantilla, tarjeta):
    "Esta función muestra en pantalla la pregunta y sus posibles respuestas."
    pregunta, respuesta = tarjeta
    mensaje = plantilla.format(pregunta=pregunta)
    input(f"{mensaje} Pulsa ENTER para comprobar la respuesta.")
    print(f"La respuesta es: {respuesta}.")

def main():
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

            try:
                índice = int(selección)
                print("[DEBUG]", f"{índice=}")
                mazo_escogido = mazos_con_tarjetas[índice]
            except ValueError:
                print("Solo acepto números.")
            except IndexError:
                print("Usa uno de los números indicados.")

        print("Has seleccionado", mazo_escogido)

        plantilla = MAZOS[mazo_escogido]["plantilla"]
        tarjetas_en_mano = MAZOS[mazo_escogido]["tarjetas"]
        tarjetas_difíciles = []
        while len(tarjetas_en_mano) > 0:
            tarjeta = tarjetas_en_mano.pop(0)
            imprime_tarjeta(plantilla, tarjeta)
            valoración = obtén_valoración()
            if valoración == "1":
                # Fácil, ;la descarta
                pass
            elif valoración == "2":
                tarjetas_difíciles.append(tarjeta)
            elif valoración == "3":
                tarjetas_en_mano.append(tarjeta)
            else:
                raise ValueError("Opción incorrecta")

        MAZOS[mazo_escogido]["tarjetas"] = tarjetas_difíciles

if __name__ == "__main__":
    main()
