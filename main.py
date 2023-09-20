from clase import ConversorDeAngulos

def main():
    try:
        angulo = float(input("Ingrese un ángulo: "))
        conversor = ConversorDeAngulos(angulo)

        print(f"{angulo} grados equivale a {conversor.grados_a_radianes()} radianes.")
        print(f"{conversor.grados_a_radianes()} radianes equivale a {angulo} grados.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
