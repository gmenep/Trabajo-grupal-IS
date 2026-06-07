from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAbstractItemView, QComboBox, QDialog, QDialogButtonBox, QFormLayout
from PyQt5.QtWidgets import QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout

from src.vista.ui.UiMainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("LabTrack")
        self.setWindowIcon(QIcon(str(Path(__file__).resolve().parent / "images" / "icono.png")))
        self.__paginas = {}
        self.__registrar_paginas()
        self.__configurar_iconos()
        self.__crear_boton_finalizar_proyecto()
        self.__configurar_tablas()

    def configurar_sesion(self, sesion):
        texto_roles = ", ".join(sesion.roles)
        self.statusbar.showMessage("Usuario: " + sesion.full_name + " | Roles: " + texto_roles)

    def mostrar_pagina(self, nombre):
        pagina = self.__paginas.get(nombre)
        if pagina is not None:
            self.stackedWidget.setCurrentWidget(pagina)

    def obtener_pagina(self, nombre):
        return self.__paginas.get(nombre)

    def ocultar_pagina(self, nombre):
        pagina = self.__paginas.get(nombre)
        if pagina is None:
            return
        indice = self.stackedWidget.indexOf(pagina)
        if indice >= 0:
            self.stackedWidget.removeWidget(pagina)

    def obtener_busqueda_inventario(self):
        return self.lineEdit.text()

    def obtener_almacen_inventario(self):
        return self.almacen_box.currentData()

    def cargar_almacenes(self, almacenes):
        actual = self.almacen_box.currentData()
        self.almacen_box.clear()
        self.almacen_box.addItem("Todos", None)
        for almacen in almacenes:
            self.almacen_box.addItem(almacen.name, almacen.storage_id)
        self.__seleccionar_combo(self.almacen_box, actual)

    def obtener_busqueda_maquinaria(self):
        return self.lineEdit_2.text()

    def obtener_filtro_maquinaria(self):
        return self.almacen_box_2.currentData()

    def cargar_filtros_maquinaria(self, almacenes):
        actual = self.almacen_box_2.currentData()
        self.almacen_box_2.clear()
        self.almacen_box_2.addItem("Todos", "")
        estados = ["Operativa", "En uso", "Mantenimiento", "Retirada"]
        for estado in estados:
            self.almacen_box_2.addItem(estado, estado)
        for almacen in almacenes:
            self.almacen_box_2.addItem(almacen.name, almacen.name)
        self.__seleccionar_combo(self.almacen_box_2, actual)

    def mostrar_inventario(self, filas):
        columnas = [
            ("material_id", "ID"),
            ("name", "Nombre"),
            ("storage_name", "Almacen"),
            ("batch_number", "Lote"),
            ("risk_level", "Riesgo"),
            ("formula", "Formula"),
            ("measure_unit", "Unidad"),
            ("quantity", "Cantidad"),
            ("exp_date", "Caducidad")
        ]
        self.__cargar_tabla(self.tabla_inventario, columnas, filas)

    def mostrar_maquinaria(self, filas):
        columnas = [
            ("machine_id", "ID"),
            ("name", "Nombre"),
            ("state", "Estado"),
            ("risk_level", "Riesgo"),
            ("storage_name", "Ubicacion"),
            ("next_revision_date", "Sig. Revision"),
            ("last_revision_date", "Ult. Revision")
        ]
        self.__cargar_tabla(self.tabla_maquinaria, columnas, filas)

    def mostrar_proyectos(self, filas):
        self.label.setText("Proyectos asignados")
        columnas = [
            ("project_id", "ID"),
            ("title", "Proyecto"),
            ("state", "Estado"),
            ("asignaciones", "Maquinaria asignada"),
            ("start_date", "Inicio"),
            ("end_date", "Fin")
        ]
        self.__cargar_tabla(self.tabla_miembros, columnas, filas)

    def mostrar_miembros(self, filas):
        self.label.setText("Miembros del proyecto")
        columnas = [
            ("user_id", "ID"),
            ("login", "Login"),
            ("full_name", "Nombre"),
            ("dni", "DNI"),
            ("state", "Estado")
        ]
        self.__cargar_tabla(self.tabla_miembros, columnas, filas)

    def mostrar_panel(self, filas):
        columnas = [
            ("entry_id", "ID"),
            ("title", "Titulo"),
            ("author_name", "Autor"),
            ("project_title", "Proyecto")
        ]
        self.__cargar_tabla(self.tableWidget, columnas, filas)

    def mostrar_panel_admin(self, filas):
        self.subtitulo_2.setText("Entradas del panel colaborativo")
        columnas = [
            ("entry_id", "ID"),
            ("title", "Titulo"),
            ("author_name", "Autor"),
            ("project_title", "Proyecto")
        ]
        self.__cargar_tabla(self.tableWidget_2, columnas, filas)

    def mostrar_usuarios(self, filas):
        columnas = [
            ("user_id", "ID"),
            ("login", "Login"),
            ("full_name", "Nombre"),
            ("dni", "DNI"),
            ("state", "Estado"),
            ("studies", "Estudios")
        ]
        self.__cargar_tabla(self.tableWidget_3, columnas, filas)

    def mostrar_backups(self, filas):
        columnas = [
            ("name", "Archivo"),
            ("path", "Ruta")
        ]
        self.__cargar_tabla(self.tabla_copias, columnas, filas)

    def mostrar_logs(self, filas):
        columnas = [
            ("log_id", "ID"),
            ("timestamp", "Fecha"),
            ("event_type", "Evento"),
            ("reference_id", "Referencia"),
            ("user_id", "Usuario"),
            ("raw_data", "Datos")
        ]
        dialogo = QDialog(self)
        dialogo.setWindowTitle("Logs")
        dialogo.resize(900, 500)
        layout = QVBoxLayout(dialogo)
        layout.addWidget(QLabel("Logs"))
        tabla = QTableWidget(dialogo)
        self.__configurar_tabla(tabla)
        self.__cargar_tabla(tabla, columnas, filas)
        layout.addWidget(tabla)
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(dialogo.accept)
        layout.addWidget(botones)
        dialogo.exec_()

    def obtener_material_seleccionado(self):
        return self.__fila_seleccionada(self.tabla_inventario)

    def obtener_maquina_seleccionada(self):
        return self.__fila_seleccionada(self.tabla_maquinaria)

    def obtener_proyecto_seleccionado(self):
        return self.__fila_seleccionada(self.tabla_miembros)

    def obtener_usuario_seleccionado(self):
        return self.__fila_seleccionada(self.tableWidget_3)

    def obtener_panel_seleccionado(self):
        fila = self.__fila_seleccionada(self.tableWidget)
        if fila is None:
            fila = self.__fila_seleccionada(self.tableWidget_2)
        return fila

    def obtener_backup_seleccionado(self):
        return self.__fila_seleccionada(self.tabla_copias)

    def pedir_material(self):
        campos = [
            ("name", "Nombre", "text", ""),
            ("risk_level", "Riesgo", "combo", self.__opciones_riesgo(), None),
            ("specifications", "Especificaciones", "text", ""),
            ("formula", "Formula", "text", ""),
            ("measure_unit", "Unidad", "text", "")
        ]
        return self.__pedir_datos("Material", campos)

    def pedir_lote(self, materiales, almacenes, datos):
        if datos is None:
            datos = {}
        campos = [
            ("material_id", "Material", "combo", self.__opciones_materiales(materiales), datos.get("material_id")),
            ("storage_id", "Almacen", "combo", self.__opciones_almacenes(almacenes), datos.get("storage_id")),
            ("batch_number", "Lote", "text", datos.get("batch_number")),
            ("quantity", "Cantidad", "text", datos.get("quantity")),
            ("exp_date", "Caducidad yyyy-mm-dd", "text", datos.get("exp_date"))
        ]
        return self.__pedir_datos("Lote", campos)

    def pedir_movimiento_lote(self, almacenes, datos):
        campos = [
            ("storage_destino_id", "Almacen destino", "combo", self.__opciones_almacenes(almacenes), None),
            ("quantity", "Cantidad", "text", "")
        ]
        resultado = self.__pedir_datos("Mover lote", campos)
        if resultado is None:
            return None
        resultado["material_id"] = datos.get("material_id")
        resultado["storage_origen_id"] = datos.get("storage_id")
        resultado["batch_number"] = datos.get("batch_number")
        return resultado

    def pedir_maquina(self, almacenes, datos):
        if datos is None:
            datos = {}
        campos = [
            ("name", "Nombre", "text", datos.get("name")),
            ("risk_level", "Riesgo", "combo", self.__opciones_riesgo(), datos.get("risk_level")),
            ("state", "Estado", "combo", self.__opciones_estados_maquina(), datos.get("state")),
            ("last_revision_date", "Ultima revision yyyy-mm-dd", "text", datos.get("last_revision_date")),
            ("next_revision_date", "Proxima revision yyyy-mm-dd", "text", datos.get("next_revision_date")),
            ("description", "Descripcion", "text", datos.get("description")),
            ("storage_id", "Almacen", "combo", self.__opciones_almacenes(almacenes), datos.get("storage_id"))
        ]
        return self.__pedir_datos("Maquina", campos)

    def pedir_movimiento_maquina(self, almacenes):
        campos = [
            ("storage_id", "Almacen destino", "combo", self.__opciones_almacenes(almacenes), None)
        ]
        return self.__pedir_datos("Mover maquina", campos)

    def pedir_solicitud_material(self, materiales):
        campos = [
            ("material_id", "Material", "combo", self.__opciones_materiales(materiales), None),
            ("quantity", "Cantidad", "text", "")
        ]
        return self.__pedir_datos("Solicitar material", campos)

    def pedir_solicitud_maquina(self, maquinas):
        campos = [
            ("machine_id", "Maquina", "combo", self.__opciones_maquinas(maquinas), None)
        ]
        return self.__pedir_datos("Solicitar maquina", campos)

    def pedir_finalizar_uso(self, usos):
        opciones = []
        for uso in usos:
            texto = "Uso " + str(uso.usage_id) + " - Maquina " + str(uso.machine_id) + " - Proyecto " + str(uso.project_id)
            opciones.append((texto, uso.usage_id))
        campos = [
            ("usage_id", "Uso activo", "combo", opciones, None)
        ]
        return self.__pedir_datos("Finalizar uso", campos)

    def pedir_usuario(self, roles, datos, pedir_password):
        if datos is None:
            datos = {}
        campos = [
            ("login", "Login", "text", datos.get("login")),
            ("full_name", "Nombre completo", "text", datos.get("full_name")),
            ("dni", "DNI", "text", datos.get("dni")),
            ("state", "Estado", "combo", [("Activo", "Activo"), ("Inactivo", "Inactivo")], datos.get("state")),
            ("studies", "Estudios", "text", datos.get("studies"))
        ]
        if pedir_password:
            campos.insert(1, ("password", "Contrasena", "text", ""))
        campos.append(("role", "Rol", "combo", self.__opciones_roles(roles), None))
        return self.__pedir_datos("Usuario", campos)

    def pedir_usuario_proyecto(self, usuarios):
        campos = [
            ("user_id", "Usuario", "combo", self.__opciones_usuarios(usuarios), None),
            ("role", "Rol en proyecto", "combo", [("Investigador", "Investigador"), ("Auditor", "Auditor")], None)
        ]
        return self.__pedir_datos("Usuario del proyecto", campos)

    def pedir_panel(self, datos):
        if datos is None:
            datos = {}
        campos = [
            ("title", "Titulo", "text", datos.get("title")),
            ("content", "Contenido", "text", datos.get("content"))
        ]
        return self.__pedir_datos("Entrada del panel", campos)

    def mostrar_detalle_panel(self, entrada):
        if entrada is None:
            return
        self.__mostrar_texto(entrada.title, entrada.content)

    def mostrar_ayuda(self, secciones):
        texto = ""
        for seccion in secciones:
            texto = texto + seccion[0] + "\n" + seccion[1] + "\n\n"
        self.__mostrar_texto("Ayuda", texto.strip())

    def mostrar_error(self, mensaje):
        QMessageBox.warning(self, "LabTrack", mensaje)

    def mostrar_info(self, mensaje):
        QMessageBox.information(self, "LabTrack", mensaje)

    def mostrar_mensaje(self, mensaje):
        self.mostrar_info(mensaje)

    def confirmar(self, mensaje):
        respuesta = QMessageBox.question(self, "LabTrack", mensaje)
        return respuesta == QMessageBox.Yes

    def __registrar_paginas(self):
        self.__paginas = {
            "inventario": self.inventario_page,
            "maquinaria": self.maquinaria_page,
            "proyectos": self.proyecto_page,
            "panel": self.panel_page,
            "administracion": self.admin_page
        }

    def __configurar_iconos(self):
        self.__estilo_icono(self.inventario_btn, "boton_inventario.png", "Inventario")
        self.__estilo_icono(self.maquinaria_btn, "boton_maquinaria.png", "Maquinaria")
        self.__estilo_icono(self.proyecto_btn, "boton_proyecto.png", "Proyecto")
        self.__estilo_icono(self.panel_btn, "boton_panel_colaborativo.png", "Panel")
        self.__estilo_icono(self.admin_btn, "boton_admin.png", "Administracion")
        self.__estilo_icono(self.ayuda_btn, "boton_ayuda.png", "Ayuda")
        self.__estilo_icono(self.salir_btn, "boton_salir.png", "Salir")

    def __crear_boton_finalizar_proyecto(self):
        self.finalizar_proyecto_btn = QPushButton(self.miembros_btn_widget)
        self.finalizar_proyecto_btn.setSizePolicy(self.add_user_btn_2.sizePolicy())
        self.finalizar_proyecto_btn.setMinimumSize(self.add_user_btn_2.minimumSize())
        self.finalizar_proyecto_btn.setMaximumSize(self.add_user_btn_2.maximumSize())
        self.finalizar_proyecto_btn.setFont(self.add_user_btn_2.font())
        self.finalizar_proyecto_btn.setStyleSheet(self.add_user_btn_2.styleSheet())
        self.finalizar_proyecto_btn.setText("Finalizar proyecto")
        self.horizontalLayout_10.addWidget(self.finalizar_proyecto_btn)

    def __estilo_icono(self, boton, archivo, tooltip):
        ruta = (Path(__file__).resolve().parent / "images" / archivo).as_posix()
        boton.setToolTip(tooltip)
        boton.setStyleSheet(
            "QPushButton {"
            "image: url(\"" + ruta + "\") 0 0 0 0 stretch stretch;"
            "border-radius: 8px;"
            "background-color: rgb(8, 77, 166);"
            "}"
            "QPushButton:hover { background-color: rgb(3, 90, 166); }"
            "QPushButton:pressed { background-color: rgb(235, 238, 242); }"
        )

    def __configurar_tablas(self):
        tablas = [
            self.tabla_inventario,
            self.tabla_maquinaria,
            self.tabla_miembros,
            self.tableWidget,
            self.tabla_copias,
            self.tableWidget_3,
            self.tableWidget_2
        ]
        for tabla in tablas:
            self.__configurar_tabla(tabla)

    def __configurar_tabla(self, tabla):
        tabla.setAlternatingRowColors(True)
        tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabla.verticalHeader().setVisible(False)

    def __cargar_tabla(self, tabla, columnas, filas):
        tabla.clear()
        tabla.setColumnCount(len(columnas))
        tabla.setRowCount(len(filas))
        tabla.setHorizontalHeaderLabels(self.__cabeceras(columnas))
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for numero_fila in range(len(filas)):
            fila = filas[numero_fila]
            for numero_columna in range(len(columnas)):
                clave = columnas[numero_columna][0]
                valor = fila.get(clave)
                item = QTableWidgetItem(self.__texto(valor))
                item.setData(Qt.UserRole, fila)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                tabla.setItem(numero_fila, numero_columna, item)
        tabla.resizeRowsToContents()

    def __cabeceras(self, columnas):
        cabeceras = []
        for columna in columnas:
            cabeceras.append(columna[1])
        return cabeceras

    def __fila_seleccionada(self, tabla):
        fila = tabla.currentRow()
        if fila < 0:
            return None
        item = tabla.item(fila, 0)
        if item is None:
            return None
        return item.data(Qt.UserRole)

    def __pedir_datos(self, titulo, campos):
        dialogo = QDialog(self)
        dialogo.setWindowTitle(titulo)
        formulario = QFormLayout(dialogo)
        controles = {}
        for campo in campos:
            clave = campo[0]
            etiqueta = campo[1]
            tipo = campo[2]
            if tipo == "combo":
                control = QComboBox()
                opciones = campo[3]
                valor_actual = campo[4]
                for opcion in opciones:
                    control.addItem(opcion[0], opcion[1])
                self.__seleccionar_combo(control, valor_actual)
            else:
                control = QLineEdit()
                valor_actual = campo[3]
                if valor_actual is not None:
                    control.setText(str(valor_actual))
            controles[clave] = control
            formulario.addRow(etiqueta, control)
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(dialogo.accept)
        botones.rejected.connect(dialogo.reject)
        formulario.addRow(botones)
        if dialogo.exec_() != QDialog.Accepted:
            return None
        datos = {}
        for clave in controles:
            control = controles[clave]
            if isinstance(control, QComboBox):
                datos[clave] = control.currentData()
            else:
                datos[clave] = control.text()
        return datos

    def __mostrar_texto(self, titulo, texto):
        dialogo = QDialog(self)
        dialogo.setWindowTitle(titulo)
        dialogo.resize(700, 450)
        layout = QVBoxLayout(dialogo)
        layout.addWidget(QLabel(titulo))
        contenido = QTextEdit()
        contenido.setReadOnly(True)
        contenido.setPlainText(texto)
        layout.addWidget(contenido)
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(dialogo.accept)
        layout.addWidget(botones)
        dialogo.exec_()

    def __opciones_materiales(self, materiales):
        opciones = []
        for material in materiales:
            texto = str(material.material_id)
            if hasattr(material, "name"):
                texto = texto + " - " + str(material.name)
            opciones.append((texto, material.material_id))
        return opciones

    def __opciones_maquinas(self, maquinas):
        opciones = []
        for maquina in maquinas:
            texto = str(maquina.machine_id)
            if hasattr(maquina, "name"):
                texto = texto + " - " + str(maquina.name)
            opciones.append((texto, maquina.machine_id))
        return opciones

    def __opciones_almacenes(self, almacenes):
        opciones = []
        for almacen in almacenes:
            opciones.append((almacen.name, almacen.storage_id))
        return opciones

    def __opciones_roles(self, roles):
        opciones = []
        for rol in roles:
            opciones.append((rol.role_name, rol.role_name))
        return opciones

    def __opciones_usuarios(self, usuarios):
        opciones = []
        for usuario in usuarios:
            texto = str(usuario.full_name) + " (" + str(usuario.login) + ")"
            opciones.append((texto, usuario.user_id))
        return opciones

    def __opciones_proyectos(self, proyectos):
        opciones = []
        for proyecto in proyectos:
            opciones.append((proyecto.title, proyecto.project_id))
        return opciones

    def __opciones_estados_maquina(self):
        return [
            ("Operativa", "Operativa"),
            ("En uso", "En uso"),
            ("Mantenimiento", "Mantenimiento"),
            ("Retirada", "Retirada")
        ]

    def __opciones_riesgo(self):
        return [
            ("Bajo", "Bajo"),
            ("Medio", "Medio"),
            ("Alto", "Alto")
        ]

    def __seleccionar_combo(self, combo, valor):
        if valor is None:
            return
        for indice in range(combo.count()):
            if combo.itemData(indice) == valor:
                combo.setCurrentIndex(indice)
                return

    def __texto(self, valor):
        if valor is None:
            return ""
        return str(valor)
