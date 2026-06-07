from src.controlador.AyudaController import AyudaController
from src.controlador.BackupController import BackupController
from src.controlador.EstadisticasController import EstadisticasController
from src.controlador.InventarioController import InventarioController
from src.controlador.LogController import LogController
from src.controlador.MaquinariaController import MaquinariaController
from src.controlador.PanelController import PanelController
from src.controlador.ProyectoController import ProyectoController
from src.controlador.UsuarioController import UsuarioController
from src.modelo.PermisoServicio import PermisoServicio


class MainController:
    def __init__(self, window, sesion, volver_login_callback):
        self.__window = window
        self.__sesion = sesion
        self.__volver_login_callback = volver_login_callback
        self.__permiso_servicio = PermisoServicio()
        self.__inventario_controller = InventarioController(window, sesion)
        self.__maquinaria_controller = MaquinariaController(window, sesion)
        self.__proyecto_controller = ProyectoController(window, sesion)
        self.__panel_controller = PanelController(window, sesion)
        self.__usuario_controller = UsuarioController(window, sesion)
        self.__backup_controller = BackupController(window, sesion)
        self.__log_controller = LogController(window, sesion)
        self.__estadisticas_controller = EstadisticasController(window, sesion)
        self.__ayuda_controller = AyudaController(window)
        self.__conectar_eventos()
        self.__aplicar_permisos()
        self.__abrir_pagina_inicial()

    def salir(self):
        self.__window.hide()
        self.__volver_login_callback()
        self.__window.close()

    def abrir_inventario(self):
        if not self.__puede("inventario"):
            self.__sin_permiso()
            return
        self.__window.mostrar_pagina("inventario")
        self.__ejecutar(self.__inventario_controller.cargar)

    def abrir_maquinaria(self):
        if not self.__puede("maquinaria"):
            self.__sin_permiso()
            return
        self.__window.mostrar_pagina("maquinaria")
        self.__ejecutar(self.__maquinaria_controller.cargar)

    def abrir_proyectos(self):
        if not self.__puede("proyectos"):
            self.__sin_permiso()
            return
        self.__window.mostrar_pagina("proyectos")
        self.__ejecutar(self.__proyecto_controller.cargar)

    def abrir_panel(self):
        if not self.__puede("panel"):
            self.__sin_permiso()
            return
        self.__window.mostrar_pagina("panel")
        self.__ejecutar(self.__panel_controller.cargar)

    def abrir_administracion(self):
        if not self.__puede_ver_administracion():
            self.__sin_permiso()
            return
        self.__window.mostrar_pagina("administracion")
        if self.__puede("backup"):
            self.__ejecutar(self.__backup_controller.cargar)
        if self.__puede("gestionar_usuarios"):
            self.__ejecutar(self.__usuario_controller.cargar)
        if self.__puede("panel"):
            self.__ejecutar(self.__panel_controller.cargar_admin)

    def abrir_ayuda(self):
        if not self.__puede("ayuda"):
            self.__sin_permiso()
            return
        self.__ejecutar(self.__ayuda_controller.cargar)

    def mostrar_logs(self):
        if not self.__puede("logs"):
            self.__sin_permiso()
            return
        self.__ejecutar(self.__log_controller.cargar)

    def mostrar_estadisticas(self):
        if not self.__puede("estadisticas"):
            self.__sin_permiso()
            return
        self.__ejecutar(self.__estadisticas_controller.cargar)

    def solicitar_maquina_proyecto(self):
        try:
            self.__maquinaria_controller.solicitar_maquina()
            self.__proyecto_controller.cargar()
        except Exception as error:
            self.__window.mostrar_error(str(error))

    def finalizar_maquina_proyecto(self):
        try:
            self.__maquinaria_controller.finalizar_uso()
            self.__proyecto_controller.cargar()
        except Exception as error:
            self.__window.mostrar_error(str(error))

    def __conectar_eventos(self):
        self.__window.inventario_btn.clicked.connect(self.abrir_inventario)
        self.__window.maquinaria_btn.clicked.connect(self.abrir_maquinaria)
        self.__window.proyecto_btn.clicked.connect(self.abrir_proyectos)
        self.__window.panel_btn.clicked.connect(self.abrir_panel)
        self.__window.admin_btn.clicked.connect(self.abrir_administracion)
        self.__window.ayuda_btn.clicked.connect(self.abrir_ayuda)
        self.__window.salir_btn.clicked.connect(self.salir)

        self.__window.bus_inventario_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.buscar))
        self.__window.recargar_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.cargar))
        self.__window.add_material_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.crear_material))
        self.__window.add_lote_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.crear_lote))
        self.__window.modificar_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.modificar_lote))
        self.__window.move_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.mover_lote))
        self.__window.eliminar_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.eliminar))

        self.__window.bus_maquina_btn.clicked.connect(lambda: self.__ejecutar(self.__maquinaria_controller.buscar))
        self.__window.recargar_btn_2.clicked.connect(lambda: self.__ejecutar(self.__maquinaria_controller.cargar))
        self.__window.add_maquina_btn.clicked.connect(lambda: self.__ejecutar(self.__maquinaria_controller.crear_maquina))
        self.__window.modificar_btn_2.clicked.connect(lambda: self.__ejecutar(self.__maquinaria_controller.modificar_maquina))
        self.__window.move_btn_2.clicked.connect(lambda: self.__ejecutar(self.__maquinaria_controller.mover_maquina))
        self.__window.eliminar_btn_2.clicked.connect(lambda: self.__ejecutar(self.__maquinaria_controller.eliminar_maquina))

        self.__window.sol_materiales_btn.clicked.connect(lambda: self.__ejecutar(self.__inventario_controller.solicitar_material))
        self.__window.sol_maquinaria_btn.clicked.connect(self.solicitar_maquina_proyecto)
        self.__window.pushButton.clicked.connect(self.finalizar_maquina_proyecto)
        self.__window.tabla_miembros.itemDoubleClicked.connect(lambda item: self.__ejecutar(self.__proyecto_controller.cargar_miembros))
        self.__window.add_user_btn_2.clicked.connect(lambda: self.__ejecutar(self.__proyecto_controller.agregar_usuario))
        self.__window.remove_user_btn_2.clicked.connect(lambda: self.__ejecutar(self.__proyecto_controller.eliminar_usuario))
        self.__window.finalizar_proyecto_btn.clicked.connect(lambda: self.__ejecutar(self.__proyecto_controller.finalizar_proyecto))

        self.__window.tableWidget.itemDoubleClicked.connect(lambda item: self.__ejecutar(self.__panel_controller.ver_detalle))

        self.__window.add_copia_btn.clicked.connect(lambda: self.__ejecutar(self.__backup_controller.crear))
        self.__window.delete_copia_btn.clicked.connect(lambda: self.__ejecutar(self.__backup_controller.eliminar))
        self.__window.add_user_btn.clicked.connect(lambda: self.__ejecutar(self.__usuario_controller.crear))
        self.__window.modificar_btn_3.clicked.connect(lambda: self.__ejecutar(self.__usuario_controller.modificar))
        self.__window.remove_user_btn.clicked.connect(lambda: self.__ejecutar(self.__usuario_controller.baja))
        self.__window.add_panel_btn.clicked.connect(lambda: self.__ejecutar(self.__panel_controller.crear))
        self.__window.pushButton_2.clicked.connect(self.mostrar_logs)

    def __aplicar_permisos(self):
        self.__configurar_modulo("inventario", self.__window.inventario_btn, "inventario")
        self.__configurar_modulo("maquinaria", self.__window.maquinaria_btn, "maquinaria")
        self.__configurar_modulo("proyectos", self.__window.proyecto_btn, "proyectos")
        self.__configurar_modulo("panel", self.__window.panel_btn, "panel")

        puede_admin = self.__puede_ver_administracion()
        self.__window.admin_btn.setVisible(puede_admin)
        if not puede_admin:
            self.__window.ocultar_pagina("administracion")

        self.__window.ayuda_btn.setVisible(self.__puede("ayuda"))
        self.__window.salir_btn.setVisible(self.__puede("salir"))

        self.__window.contenedor_solicitudes_widget.setVisible(self.__puede("solicitar_assets"))
        self.__window.sol_materiales_btn.setVisible(self.__puede("solicitar_assets"))
        self.__window.sol_maquinaria_btn.setVisible(self.__puede("solicitar_assets"))
        self.__window.pushButton.setVisible(self.__puede("solicitar_assets"))

        self.__window.miembros_widget.setVisible(self.__puede("proyectos"))
        self.__window.add_user_btn_2.setVisible(self.__puede("modificar_proyecto_usuarios"))
        self.__window.remove_user_btn_2.setVisible(self.__puede("modificar_proyecto_usuarios"))
        self.__window.finalizar_proyecto_btn.setVisible(self.__puede("finalizar_proyecto"))

        self.__window.copias_widget.setVisible(self.__puede("backup"))
        self.__window.usuarios_widget.setVisible(self.__puede("gestionar_usuarios"))
        self.__window.panel_widget.setVisible(self.__puede("panel") or self.__puede("logs"))
        self.__window.add_panel_btn.setVisible(self.__puede("modificar_panel"))
        self.__window.pushButton_2.setVisible(self.__puede("logs"))

    def __configurar_modulo(self, permiso, boton, pagina):
        permitido = self.__puede(permiso)
        boton.setVisible(permitido)
        if not permitido:
            self.__window.ocultar_pagina(pagina)

    def __abrir_pagina_inicial(self):
        if self.__puede("inventario"):
            self.abrir_inventario()
            return
        if self.__puede("maquinaria"):
            self.abrir_maquinaria()
            return
        if self.__puede("proyectos"):
            self.abrir_proyectos()
            return
        if self.__puede("panel"):
            self.abrir_panel()
            return
        if self.__puede_ver_administracion():
            self.abrir_administracion()
            return
        self.abrir_ayuda()

    def __puede_ver_administracion(self):
        if self.__puede("administracion"):
            return True
        if self.__puede("backup"):
            return True
        if self.__puede("logs"):
            return True
        if self.__puede("estadisticas"):
            return True
        if self.__puede("gestionar_usuarios"):
            return True
        return False

    def __puede(self, permiso):
        return self.__permiso_servicio.puede(self.__sesion, permiso)

    def __sin_permiso(self):
        self.__window.mostrar_error("No tienes permiso para acceder a este modulo")

    def __ejecutar(self, funcion):
        try:
            funcion()
        except Exception as error:
            self.__window.mostrar_error(str(error))
