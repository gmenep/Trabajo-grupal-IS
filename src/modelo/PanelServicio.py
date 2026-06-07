from src.modelo.dao.PanelEntryDaoJDBC import PanelEntryDaoJDBC
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.PanelEntryVo import PanelEntryVo


class PanelServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__panel_dao = PanelEntryDaoJDBC()

    def listar_entradas(self, sesion):
        self._verificar_permiso(sesion, "panel", "CONSULTAR_PANEL")
        self._registrar_log(sesion.user_id, "CONSULTAR_PANEL", None, "Consulta de panel")
        return self.__panel_dao.select()

    def obtener_entrada(self, sesion, entry_id):
        self._verificar_permiso(sesion, "panel", "VER_ENTRADA_PANEL")
        return self.__panel_dao.select_by_id(entry_id)

    def agregar_entrada(self, sesion, project_id, study_id, title, content):
        self._verificar_permiso(sesion, "panel", "ANADIR_ENTRADA_PANEL")
        project_id = self.__normalizar_entero(project_id, "El proyecto", True)
        study_id = self.__normalizar_entero(study_id, "El estudio", False)
        if title is None or title.strip() == "":
            raise Exception("El titulo es obligatorio")
        if content is None or content.strip() == "":
            raise Exception("El contenido es obligatorio")
        entrada = PanelEntryVo(None, project_id, study_id, sesion.user_id, title, content, None, None, None, None)
        nuevo_id = self.__panel_dao.insert(entrada)
        self._registrar_log(sesion.user_id, "ANADIR_ENTRADA_PANEL", nuevo_id, title)
        return nuevo_id

    def modificar_entrada(self, sesion, entry_id, title, content):
        self._verificar_permiso(sesion, "modificar_panel", "MODIFICAR_ENTRADA_PANEL")
        entrada = PanelEntryVo(entry_id, None, None, None, title, content, None, None, None, None)
        self.__panel_dao.update(entrada)
        self._registrar_log(sesion.user_id, "MODIFICAR_ENTRADA_PANEL", entry_id, title)
        return True

    def eliminar_entrada(self, sesion, entry_id):
        self._verificar_permiso(sesion, "modificar_panel", "ELIMINAR_ENTRADA_PANEL")
        self.__panel_dao.delete(entry_id)
        self._registrar_log(sesion.user_id, "ELIMINAR_ENTRADA_PANEL", entry_id, "Entrada eliminada")
        return True

    def dar_like(self, sesion, entry_id):
        self._verificar_permiso(sesion, "panel", "LIKE_PANEL")
        self.__panel_dao.like(entry_id)
        self._registrar_log(sesion.user_id, "LIKE_PANEL", entry_id, "Like")
        return True

    def dar_dislike(self, sesion, entry_id):
        self._verificar_permiso(sesion, "panel", "DISLIKE_PANEL")
        self.__panel_dao.dislike(entry_id)
        self._registrar_log(sesion.user_id, "DISLIKE_PANEL", entry_id, "Dislike")
        return True

    def __normalizar_entero(self, valor, nombre, obligatorio):
        if valor is None or str(valor).strip() == "":
            if obligatorio:
                raise Exception(nombre + " es obligatorio")
            return None
        try:
            return int(valor)
        except ValueError:
            raise Exception(nombre + " debe ser un numero valido")
