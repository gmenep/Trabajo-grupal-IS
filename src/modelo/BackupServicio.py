import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from src.modelo.ServicioBase import ServicioBase


class BackupServicio(ServicioBase):
    def listar_backups(self):
        ruta = self.__ruta_backups()
        ruta.mkdir(exist_ok=True)
        return sorted(ruta.glob("*.sql"))

    def crear_backup(self, sesion):
        self._verificar_permiso(sesion, "backup", "CREAR_BACKUP")
        mysqldump = shutil.which("mysqldump")
        if mysqldump is None:
            self._registrar_log(sesion.user_id, "BACKUP", None, "mysqldump no disponible")
            return False, "mysqldump no esta disponible en PATH"

        ruta = self.__ruta_backups()
        ruta.mkdir(exist_ok=True)
        nombre = "labtrack_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".sql"
        destino = ruta / nombre
        user = os.getenv("LABTRACK_DB_USER", "root")
        password = os.getenv("LABTRACK_DB_PASSWORD", "changeme")
        database = os.getenv("LABTRACK_DB_NAME", "labtrack")
        comando = [mysqldump, "-u", user, "-p" + password, database]
        with open(destino, "w", encoding="utf-8") as archivo:
            resultado = subprocess.run(comando, stdout=archivo, stderr=subprocess.PIPE, text=True)
        if resultado.returncode != 0:
            self._registrar_log(sesion.user_id, "BACKUP", None, resultado.stderr)
            return False, resultado.stderr
        self._registrar_log(sesion.user_id, "BACKUP", None, str(destino))
        return True, str(destino)

    def eliminar_backup(self, sesion, ruta_backup):
        self._verificar_permiso(sesion, "backup", "ELIMINAR_BACKUP")
        ruta = Path(ruta_backup).resolve()
        raiz = self.__ruta_backups().resolve()
        if raiz != ruta.parent:
            raise Exception("La copia no pertenece a la carpeta de backups")
        if ruta.exists():
            ruta.unlink()
            self._registrar_log(sesion.user_id, "ELIMINAR_BACKUP", None, str(ruta))
        return True

    def restaurar_backup(self, sesion, ruta_backup):
        self._verificar_permiso(sesion, "backup", "RESTAURAR_BACKUP")
        mysql = shutil.which("mysql")
        if mysql is None:
            self._registrar_log(sesion.user_id, "RESTAURACION", None, "mysql no disponible")
            return False, "mysql no esta disponible en PATH"
        if ruta_backup is None or not Path(ruta_backup).exists():
            return False, "El archivo de backup no existe"
        user = os.getenv("LABTRACK_DB_USER", "root")
        password = os.getenv("LABTRACK_DB_PASSWORD", "changeme")
        database = os.getenv("LABTRACK_DB_NAME", "labtrack")
        comando = [mysql, "-u", user, "-p" + password, database]
        with open(ruta_backup, "r", encoding="utf-8") as archivo:
            resultado = subprocess.run(comando, stdin=archivo, stderr=subprocess.PIPE, text=True)
        if resultado.returncode != 0:
            self._registrar_log(sesion.user_id, "RESTAURACION", None, resultado.stderr)
            return False, resultado.stderr
        self._registrar_log(sesion.user_id, "RESTAURACION", None, ruta_backup)
        return True, "Restauracion completada"

    def __ruta_backups(self):
        return Path(__file__).resolve().parents[2] / "backups"
