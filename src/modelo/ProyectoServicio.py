from src.modelo.dao.BelongsToDaoJDBC import BelongsToDaoJDBC
from src.modelo.dao.ProjectDaoJDBC import ProjectDaoJDBC
from src.modelo.dao.StudyDaoJDBC import StudyDaoJDBC
from src.modelo.dao.UsersDaoJDBC import UsersDaoJDBC
from src.modelo.dao.MachineUsageDaoJDBC import MachineUsageDaoJDBC
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.BelongsToVo import BelongsToVo
from src.modelo.vo.ProjectVo import ProjectVo
from src.modelo.vo.ProyectoResumenVo import ProyectoResumenVo


class ProyectoServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__project_dao = ProjectDaoJDBC()
        self.__study_dao = StudyDaoJDBC()
        self.__belongs_to_dao = BelongsToDaoJDBC()
        self.__users_dao = UsersDaoJDBC()
        self.__usage_dao = MachineUsageDaoJDBC()

    def listar_proyectos(self, sesion):
        self._verificar_permiso(sesion, "proyectos", "CONSULTAR_PROYECTOS")
        proyectos = self.__project_dao.select()
        if self.__debe_filtrar_proyectos(sesion):
            project_ids = self.__belongs_to_dao.select_project_ids_by_user(sesion.user_id)
            filtrados = []
            for proyecto in proyectos:
                if proyecto.project_id in project_ids:
                    filtrados.append(proyecto)
            proyectos = filtrados
        self._registrar_log(sesion.user_id, "CONSULTAR_PROYECTOS", None, "Consulta de proyectos")
        return proyectos

    def listar_proyectos_panel(self, sesion):
        self._verificar_permiso(sesion, "modificar_panel", "CONSULTAR_PROYECTOS_PANEL")
        proyectos = self.__project_dao.select()
        self._registrar_log(sesion.user_id, "CONSULTAR_PROYECTOS_PANEL", None, "Consulta de proyectos para panel")
        return proyectos

    def listar_resumen_proyectos(self, sesion):
        proyectos = self.listar_proyectos(sesion)
        asignaciones = self.__usage_dao.select_asignaciones_activas()
        resumenes = []
        for proyecto in proyectos:
            textos = []
            for asignacion in asignaciones:
                if asignacion.project_id == proyecto.project_id:
                    texto = asignacion.machine_name + " (" + asignacion.user_name + ")"
                    textos.append(texto)
            resumenes.append(ProyectoResumenVo(
                proyecto.project_id,
                proyecto.title,
                proyecto.description,
                proyecto.start_date,
                proyecto.end_date,
                proyecto.state,
                ", ".join(textos)
            ))
        return resumenes

    def crear_proyecto(self, sesion, title, description, start_date, end_date, state):
        self._verificar_permiso(sesion, "crear_proyecto", "CREAR_PROYECTO")
        if title is None or title.strip() == "":
            raise Exception("El titulo del proyecto es obligatorio")
        if state is None or str(state).strip() == "":
            state = "Activo"
        proyecto = ProjectVo(None, title.strip(), description, start_date, end_date, state)
        project_id = self.__project_dao.insert(proyecto)
        self.__belongs_to_dao.insert(BelongsToVo(project_id, sesion.user_id))
        self._registrar_log(sesion.user_id, "CREAR_PROYECTO", project_id, title)
        return project_id

    def listar_estudios(self, sesion, project_id):
        self._verificar_permiso(sesion, "proyectos", "CONSULTAR_ESTUDIOS")
        return self.__study_dao.select_by_project(project_id)

    def listar_miembros(self, sesion, project_id):
        self._verificar_permiso(sesion, "ver_miembros_proyecto", "CONSULTAR_MIEMBROS_PROYECTO")
        return self.__belongs_to_dao.select_members_by_project(project_id)

    def listar_usuarios_para_proyecto(self, sesion):
        self._verificar_permiso(sesion, "modificar_proyecto_usuarios", "CONSULTAR_USUARIOS_PROYECTO")
        return self.__users_dao.select()

    def agregar_usuario_proyecto(self, sesion, project_id, user_id):
        self._verificar_permiso(sesion, "modificar_proyecto_usuarios", "ANADIR_USUARIO_PROYECTO")
        self.__belongs_to_dao.insert(BelongsToVo(project_id, user_id))
        self._registrar_log(sesion.user_id, "ANADIR_USUARIO_PROYECTO", project_id, "Usuario " + str(user_id))
        return True

    def eliminar_usuario_proyecto(self, sesion, project_id, user_id):
        self._verificar_permiso(sesion, "modificar_proyecto_usuarios", "ELIMINAR_USUARIO_PROYECTO")
        self.__belongs_to_dao.delete(project_id, user_id)
        self._registrar_log(sesion.user_id, "ELIMINAR_USUARIO_PROYECTO", project_id, "Usuario " + str(user_id))
        return True

    def finalizar_proyecto(self, sesion, project_id):
        self._verificar_permiso(sesion, "finalizar_proyecto", "FINALIZAR_PROYECTO")
        proyecto = self.__project_dao.select_by_id(project_id)
        if proyecto is None:
            raise Exception("El proyecto no existe")
        if proyecto.state == "Finalizado":
            raise Exception("El proyecto ya esta finalizado")
        self.__project_dao.finalizar(project_id)
        self._registrar_log(sesion.user_id, "FINALIZAR_PROYECTO", project_id, "Proyecto finalizado")
        return True

    def __debe_filtrar_proyectos(self, sesion):
        if self._permiso_servicio.tiene_rol(sesion, "Administrador"):
            return False
        if self._permiso_servicio.tiene_rol(sesion, "Investigador"):
            return True
        if self._permiso_servicio.tiene_rol(sesion, "Director"):
            return True
        return False
