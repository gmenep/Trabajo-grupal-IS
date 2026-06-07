from datetime import date

from src.modelo.dao.BelongsToDaoJDBC import BelongsToDaoJDBC
from src.modelo.dao.PanelEntryDaoJDBC import PanelEntryDaoJDBC
from src.modelo.dao.ProjectDaoJDBC import ProjectDaoJDBC
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.BelongsToVo import BelongsToVo
from src.modelo.vo.PanelEntryVo import PanelEntryVo
from src.modelo.vo.ProjectVo import ProjectVo


class PanelServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__belongs_to_dao = BelongsToDaoJDBC()
        self.__panel_dao = PanelEntryDaoJDBC()
        self.__project_dao = ProjectDaoJDBC()

    def listar_entradas(self, sesion):
        self._verificar_permiso(sesion, "panel", "CONSULTAR_PANEL")
        self._registrar_log(sesion.user_id, "CONSULTAR_PANEL", None, "Consulta de panel")
        return self.__panel_dao.select()

    def obtener_entrada(self, sesion, entry_id):
        self._verificar_permiso(sesion, "panel", "VER_ENTRADA_PANEL")
        return self.__panel_dao.select_by_id(entry_id)

    def agregar_entrada(self, sesion, title, content):
        self._verificar_permiso(sesion, "modificar_panel", "ANADIR_ENTRADA_PANEL")
        if title is None or title.strip() == "":
            raise Exception("El titulo es obligatorio")
        if content is None or content.strip() == "":
            raise Exception("El contenido es obligatorio")
        title = title.strip()
        content = content.strip()
        project_id = self.__crear_proyecto_de_panel(title, content)
        study_id = None
        entrada = PanelEntryVo(None, project_id, study_id, sesion.user_id, title, content, None, None, None, None)
        nuevo_id = self.__panel_dao.insert(entrada)
        self.__asignar_creador_si_falta(project_id, sesion.user_id)
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

    def __asignar_creador_si_falta(self, project_id, user_id):
        relaciones = self.__belongs_to_dao.select_by_project(project_id)
        for relacion in relaciones:
            if relacion.user_id == user_id:
                return
        self.__belongs_to_dao.insert(BelongsToVo(project_id, user_id))

    def __crear_proyecto_de_panel(self, title, content):
        fecha_inicio = date.today().strftime("%Y-%m-%d")
        proyecto = ProjectVo(None, title, content, fecha_inicio, None, "Activo")
        return self.__project_dao.insert_if_not_exists(proyecto)
