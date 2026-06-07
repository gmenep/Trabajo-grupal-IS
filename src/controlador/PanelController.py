from src.modelo.PanelServicio import PanelServicio
from src.modelo.ProyectoServicio import ProyectoServicio


class PanelController:
    def __init__(self, view, sesion):
        self.__view = view
        self.__sesion = sesion
        self.__panel_servicio = PanelServicio()
        self.__proyecto_servicio = ProyectoServicio()

    def cargar(self):
        entradas = self.__panel_servicio.listar_entradas(self.__sesion)
        filas = []
        for entrada in entradas:
            filas.append(self.__entrada_a_fila(entrada))
        self.__view.mostrar_panel(filas)

    def cargar_admin(self):
        entradas = self.__panel_servicio.listar_entradas(self.__sesion)
        filas = []
        for entrada in entradas:
            filas.append(self.__entrada_a_fila(entrada))
        self.__view.mostrar_panel_admin(filas)

    def crear(self):
        proyectos = self.__proyecto_servicio.listar_proyectos(self.__sesion)
        datos = self.__view.pedir_panel(proyectos, None)
        if datos is None:
            return
        self.__panel_servicio.agregar_entrada(
            self.__sesion,
            datos.get("project_id"),
            datos.get("study_id"),
            datos.get("title"),
            datos.get("content")
        )
        self.__view.mostrar_info("Entrada creada")
        self.cargar_admin()

    def ver_detalle(self):
        actual = self.__view.obtener_panel_seleccionado()
        if actual is None:
            return
        entrada = self.__panel_servicio.obtener_entrada(self.__sesion, actual.get("entry_id"))
        self.__view.mostrar_detalle_panel(entrada)

    def __entrada_a_fila(self, entrada):
        return {
            "entry_id": entrada.entry_id,
            "project_id": entrada.project_id,
            "study_id": entrada.study_id,
            "user_id": entrada.user_id,
            "title": entrada.title,
            "content": entrada.content,
            "created_at": entrada.created_at,
            "project_title": entrada.project_title,
            "study_label": entrada.study_label,
            "author_name": entrada.author_name,
            "likes": entrada.likes,
            "dislikes": entrada.dislikes
        }
