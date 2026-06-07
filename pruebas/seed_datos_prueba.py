import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.modelo.conexion.Conexion import Conexion
from pruebas.InicializadorServicio import InicializadorServicio


def main():
    try:
        resultado = InicializadorServicio().ejecutar_seed()
        print("Seed ejecutado correctamente")
        print("Roles:", resultado["roles"])
        print("Usuarios:", resultado["usuarios"])
        print("Almacenes:", resultado["almacenes"])
        print("Materiales:", resultado["materiales"])
        print("Maquinas:", resultado["maquinas"])
        print("Proyectos:", resultado["proyectos"])
    finally:
        Conexion().closeConnection()


if __name__ == "__main__":
    main()
