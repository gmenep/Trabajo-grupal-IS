from src.modelo.dao.BelongsToDaoJDBC import BelongsToDaoJDBC
from src.modelo.dao.ProjectDaoJDBC import ProjectDaoJDBC
from src.modelo.dao.RoleDaoJDBC import RoleDaoJDBC
from src.modelo.dao.StudyDaoJDBC import StudyDaoJDBC
from src.modelo.dao.UserRoleDaoJDBC import UserRoleDaoJDBC
from src.modelo.dao.MachineUsageDaoJDBC import MachineUsageDaoJDBC
from src.modelo.ServicioBase import ServicioBase
from src.modelo.vo.BelongsToVo import BelongsToVo
from src.modelo.vo.ProyectoResumenVo import ProyectoResumenVo
from src.modelo.vo.UserRoleVo import UserRoleVo


class ProyectoServicio(ServicioBase):
    def __init__(self):
        ServicioBase.__init__(self)
        self.__project_dao = ProjectDaoJDBC()
        self.__study_dao = StudyDaoJDBC()
        self.__belongs_to_dao = BelongsToDaoJDBC()
        self.__role_dao = RoleDaoJDBC()
        self.__user_role_dao = UserRoleDaoJDBC()
        self.__usage_dao = MachineUsageDaoJDBC()

    def listar_proyectos(self, sesion):
        self._verificar_permiso(sesion, "proyectos", "CONSULTAR_PROYECTOS")
        proyectos = self.__project_dao.select()
        if self._permiso_servicio.tiene_rol(sesion, "Investigador"):
            filtrados = []
            for proyecto in proyectos:
                if proyecto.project_id in sesion.project_ids:
                    filtrados.append(proyecto)
            proyectos = filtrados
        self._registrar_log(sesion.user_id, "CONSULTAR_PROYECTOS", None, "Consulta de proyectos")
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

    def listar_estudios(self, sesion, project_id):
        self._verificar_permiso(sesion, "proyectos", "CONSULTAR_ESTUDIOS")
        return self.__study_dao.select_by_project(project_id)

    def listar_miembros(self, sesion, project_id):
        self._verificar_permiso(sesion, "ver_miembros_proyecto", "CONSULTAR_MIEMBROS_PROYECTO")
        return self.__belongs_to_dao.select_members_by_project(project_id)

    def agregar_usuario_proyecto(self, sesion, project_id, user_id, role_name):
        self._verificar_permiso(sesion, "modificar_proyecto_usuarios", "ANADIR_USUARIO_PROYECTO")
        self.__belongs_to_dao.insert(BelongsToVo(project_id, user_id))
        role = self.__role_dao.select_by_name(role_name)
        if role is not None:
            roles_actuales = self.__user_role_dao.select_by_user(user_id)
            existe = False
            for relacion in roles_actuales:
                if relacion.role_id == role.role_id:
                    existe = True
            if not existe:
                self.__user_role_dao.insert(UserRoleVo(user_id, role.role_id))
        self._registrar_log(sesion.user_id, "ANADIR_USUARIO_PROYECTO", project_id, "Usuario " + str(user_id))
        return True

    def eliminar_usuario_proyecto(self, sesion, project_id, user_id):
        self._verificar_permiso(sesion, "modificar_proyecto_usuarios", "ELIMINAR_USUARIO_PROYECTO")
        self.__belongs_to_dao.delete(project_id, user_id)
        self._registrar_log(sesion.user_id, "ELIMINAR_USUARIO_PROYECTO", project_id, "Usuario " + str(user_id))
        return True
