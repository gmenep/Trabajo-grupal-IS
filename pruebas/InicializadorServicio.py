from src.modelo.dao.AssetDaoJDBC import AssetDaoJDBC
from src.modelo.dao.BelongsToDaoJDBC import BelongsToDaoJDBC
from src.modelo.dao.MachineDaoJDBC import MachineDaoJDBC
from src.modelo.dao.MachineLocationDaoJDBC import MachineLocationDaoJDBC
from src.modelo.dao.MaterialDaoJDBC import MaterialDaoJDBC
from src.modelo.dao.PanelEntryDaoJDBC import PanelEntryDaoJDBC
from src.modelo.dao.ProjectDaoJDBC import ProjectDaoJDBC
from src.modelo.dao.RoleDaoJDBC import RoleDaoJDBC
from src.modelo.dao.StorageDaoJDBC import StorageDaoJDBC
from src.modelo.dao.StoredInDaoJDBC import StoredInDaoJDBC
from src.modelo.dao.StudyDaoJDBC import StudyDaoJDBC
from src.modelo.dao.UserRoleDaoJDBC import UserRoleDaoJDBC
from src.modelo.dao.UsersDaoJDBC import UsersDaoJDBC
from src.modelo.PasswordService import PasswordService
from src.modelo.vo.AssetVo import AssetVo
from src.modelo.vo.BelongsToVo import BelongsToVo
from src.modelo.vo.MachineLocationVo import MachineLocationVo
from src.modelo.vo.MachineVo import MachineVo
from src.modelo.vo.MaterialVo import MaterialVo
from src.modelo.vo.PanelEntryVo import PanelEntryVo
from src.modelo.vo.ProjectVo import ProjectVo
from src.modelo.vo.RoleVo import RoleVo
from src.modelo.vo.StorageVo import StorageVo
from src.modelo.vo.StoredInVo import StoredInVo
from src.modelo.vo.StudyVo import StudyVo
from src.modelo.vo.UserRoleVo import UserRoleVo
from src.modelo.vo.UsuarioVo import UsuarioVo


class InicializadorServicio:
    def __init__(self):
        self.__asset_dao = AssetDaoJDBC()
        self.__belongs_to_dao = BelongsToDaoJDBC()
        self.__machine_dao = MachineDaoJDBC()
        self.__location_dao = MachineLocationDaoJDBC()
        self.__material_dao = MaterialDaoJDBC()
        self.__panel_dao = PanelEntryDaoJDBC()
        self.__project_dao = ProjectDaoJDBC()
        self.__role_dao = RoleDaoJDBC()
        self.__storage_dao = StorageDaoJDBC()
        self.__storedin_dao = StoredInDaoJDBC()
        self.__study_dao = StudyDaoJDBC()
        self.__user_role_dao = UserRoleDaoJDBC()
        self.__users_dao = UsersDaoJDBC()
        self.__password_service = PasswordService()

    def ejecutar_seed(self):
        role_ids = self.__crear_roles()
        user_ids = self.__crear_usuarios(role_ids)
        storage_ids = self.__crear_almacenes()
        material_ids = self.__crear_materiales(storage_ids, user_ids)
        machine_ids = self.__crear_maquinas(storage_ids)
        project_ids = self.__crear_proyectos()
        study_ids = self.__crear_estudios(project_ids)
        self.__crear_pertenencias(project_ids, user_ids)
        self.__crear_panel(project_ids, study_ids, user_ids)
        return {
            "roles": role_ids,
            "usuarios": user_ids,
            "almacenes": storage_ids,
            "materiales": material_ids,
            "maquinas": machine_ids,
            "proyectos": project_ids
        }

    def __crear_roles(self):
        permisos = {
            "Administrador": "administracion, inventario, maquinaria, panel, logs, backup, estadisticas",
            "Director": "proyectos, panel, miembros, solicitudes, logs",
            "Investigador": "proyectos, panel, solicitudes",
            "Auditor": "proyectos, logs, miembros",
            "Tecnico": "maquinaria",
            "Reponedor": "inventario"
        }
        ids = {}
        for nombre in permisos:
            role_id = self.__role_dao.insert_if_not_exists(RoleVo(None, nombre, permisos[nombre]))
            ids[nombre] = role_id
        return ids

    def __crear_usuarios(self, role_ids):
        usuarios = [
            ("admin", "admin123", "Administrador LabTrack", "00000001A", "Administrador"),
            ("director", "director123", "Director de Proyecto", "00000002B", "Director"),
            ("investigador", "investigador123", "Investigador Principal", "00000003C", "Investigador"),
            ("auditor", "auditor123", "Auditor Calidad", "00000004D", "Auditor"),
            ("tecnico", "tecnico123", "Tecnico de Maquinaria", "00000005E", "Tecnico"),
            ("reponedor", "reponedor123", "Reponedor de Inventario", "00000006F", "Reponedor")
        ]
        ids = {}
        for login, password, full_name, dni, role_name in usuarios:
            usuario = self.__users_dao.select_by_login(login)
            if usuario is None:
                pass_hash = self.__password_service.hash_password(password)
                nuevo = UsuarioVo(None, login, pass_hash, full_name, dni, "Activo", "General")
                user_id = self.__users_dao.insert(nuevo)
            else:
                user_id = usuario.user_id
            ids[login] = user_id
            self.__asignar_rol_si_falta(user_id, role_ids[role_name])
        return ids

    def __crear_almacenes(self):
        datos = [
            ("Almacen Quimico", "Reactivos y sustancias controladas"),
            ("Almacen Biologico", "Material biologico y consumibles"),
            ("Sala Maquinaria", "Equipos de laboratorio")
        ]
        ids = {}
        for name, specifications in datos:
            storage_id = self.__storage_dao.insert_if_not_exists(StorageVo(None, name, specifications))
            ids[name] = storage_id
        return ids

    def __crear_materiales(self, storage_ids, user_ids):
        datos = [
            ("Etanol 70", "Medio", "Desinfectante de laboratorio", "C2H6O", "L", "Almacen Quimico", "ET-001", 25, "2026-12-31"),
            ("Buffer PBS", "Bajo", "Solucion tampon", "PBS", "L", "Almacen Biologico", "PBS-001", 12, "2026-10-15"),
            ("Acido clorhidrico", "Alto", "Reactivo corrosivo", "HCl", "L", "Almacen Quimico", "HCL-001", 4, "2026-08-01")
        ]
        ids = {}
        for name, risk, specifications, formula, unit, storage_name, batch, quantity, exp_date in datos:
            asset = self.__asset_dao.select_by_name_type(name, "material")
            if asset is None:
                material_id = self.__asset_dao.insert(AssetVo(None, name, "material", risk))
                self.__material_dao.insert(MaterialVo(material_id, specifications, formula, unit))
            else:
                material_id = asset.asset_id
            ids[name] = material_id
            storage_id = storage_ids[storage_name]
            lote = self.__storedin_dao.select_one(material_id, storage_id, batch)
            if lote is None:
                self.__storedin_dao.insert(StoredInVo(material_id, storage_id, quantity, batch, exp_date))
        return ids

    def __crear_maquinas(self, storage_ids):
        datos = [
            ("Centrifuga C-200", "Medio", "Operativa", "2026-01-15", "2026-07-15", "Centrifuga refrigerada", "Sala Maquinaria"),
            ("Microscopio M-10", "Bajo", "Operativa", "2026-02-01", "2026-08-01", "Microscopio optico", "Sala Maquinaria"),
            ("Autoclave A-5", "Alto", "Mantenimiento", "2026-03-10", "2026-06-30", "Autoclave de esterilizacion", "Sala Maquinaria")
        ]
        ids = {}
        for name, risk, state, last_date, next_date, description, storage_name in datos:
            asset = self.__asset_dao.select_by_name_type(name, "machine")
            if asset is None:
                machine_id = self.__asset_dao.insert(AssetVo(None, name, "machine", risk))
                self.__machine_dao.insert(MachineVo(machine_id, state, last_date, next_date, description))
            else:
                machine_id = asset.asset_id
            ids[name] = machine_id
            self.__location_dao.upsert(MachineLocationVo(machine_id, storage_ids[storage_name]))
        return ids

    def __crear_proyectos(self):
        datos = [
            ("Proyecto Bioseguridad", "Control de trazabilidad de muestras", "2026-01-01", None, "Activo"),
            ("Proyecto Reactivos", "Optimizacion de uso de reactivos", "2026-02-01", None, "Activo")
        ]
        ids = {}
        for title, description, start_date, end_date, state in datos:
            project_id = self.__project_dao.insert_if_not_exists(ProjectVo(None, title, description, start_date, end_date, state))
            ids[title] = project_id
        return ids

    def __crear_estudios(self, project_ids):
        ids = {}
        for title in project_ids:
            existentes = self.__study_dao.select_by_project(project_ids[title])
            if len(existentes) == 0:
                study_id = self.__study_dao.insert(StudyVo(None, project_ids[title]))
            else:
                study_id = existentes[0].study_id
            ids[title] = study_id
        return ids

    def __crear_pertenencias(self, project_ids, user_ids):
        for title in project_ids:
            self.__insertar_pertenencia_si_falta(project_ids[title], user_ids["director"])
            self.__insertar_pertenencia_si_falta(project_ids[title], user_ids["investigador"])
            self.__insertar_pertenencia_si_falta(project_ids[title], user_ids["auditor"])

    def __crear_panel(self, project_ids, study_ids, user_ids):
        titulos_existentes = []
        for entrada in self.__panel_dao.select():
            titulos_existentes.append(entrada.title)
        if "Inicio de estudio" not in titulos_existentes:
            entry = PanelEntryVo(None, project_ids["Proyecto Bioseguridad"], study_ids["Proyecto Bioseguridad"], user_ids["investigador"], "Inicio de estudio", "Registro inicial del estudio de bioseguridad.", None, None, None, None)
            self.__panel_dao.insert(entry)
        if "Revision de reactivos" not in titulos_existentes:
            entry = PanelEntryVo(None, project_ids["Proyecto Reactivos"], study_ids["Proyecto Reactivos"], user_ids["director"], "Revision de reactivos", "Se revisan lotes con stock bajo y proxima caducidad.", None, None, None, None)
            self.__panel_dao.insert(entry)

    def __asignar_rol_si_falta(self, user_id, role_id):
        actuales = self.__user_role_dao.select_by_user(user_id)
        for relacion in actuales:
            if relacion.role_id == role_id:
                return
        self.__user_role_dao.insert(UserRoleVo(user_id, role_id))

    def __insertar_pertenencia_si_falta(self, project_id, user_id):
        actuales = self.__belongs_to_dao.select_by_project(project_id)
        for relacion in actuales:
            if relacion.user_id == user_id:
                return
        self.__belongs_to_dao.insert(BelongsToVo(project_id, user_id))
