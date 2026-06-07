import os


try:
    from pruebas.seed_datos_prueba import main
except ModuleNotFoundError:
    from seed_datos_prueba import main


if __name__ == "__main__":
    os.environ["JAVA_HOME"] = r"c:\Users\lmomf\anaconda3\envs\labtrack"
    main()
