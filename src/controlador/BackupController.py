from pathlib import Path

from src.modelo.BackupServicio import BackupServicio


class BackupController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__servicio = BackupServicio()

    def cargar(self):
        filas = []
        archivos = self.__servicio.listar_backups()
        for archivo in archivos:
            filas.append({
                "name": archivo.name,
                "path": str(archivo)
            })
        self.__view.mostrar_backups(filas)

    def crear(self):
        correcto, mensaje = self.__servicio.crear_backup(self.__sesion)
        if correcto:
            self.__view.mostrar_info("Backup creado: " + mensaje)
            self.cargar()
        else:
            self.__view.mostrar_error(mensaje)

    def eliminar(self):
        actual = self.__view.obtener_backup_seleccionado()
        if actual is None:
            self.__view.mostrar_error("Selecciona una copia")
            return
        if not self.__view.confirmar("Eliminar copia seleccionada?"):
            return
        ruta = Path(actual.get("path")).resolve()
        raiz = Path.cwd().resolve()
        if raiz not in ruta.parents:
            self.__view.mostrar_error("La copia no pertenece al proyecto")
            return
        self.__servicio.eliminar_backup(self.__sesion, ruta)
        self.cargar()
