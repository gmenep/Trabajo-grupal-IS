class AyudaServicio:
    def secciones(self):
        return [
            ("Login", "Introduce tu usuario y contrasena. La contrasena se verifica con bcrypt contra el hash guardado."),
            ("Roles", "Cada usuario ve solo los modulos permitidos por su rol. Los servicios vuelven a comprobar el permiso."),
            ("Inventario", "Administradores y reponedores pueden buscar, crear, mover, modificar y eliminar lotes o materiales."),
            ("Maquinaria", "Administradores y tecnicos gestionan maquinas, estado, revisiones, ubicacion y mantenimiento."),
            ("Proyectos", "Investigadores, directores y auditores consultan proyectos segun sus permisos."),
            ("Panel colaborativo", "Investigadores, directores y administradores pueden consultar entradas del panel."),
            ("Solicitud de materiales", "Investigadores y directores solicitan cantidad disponible. El sistema descuenta por caducidad cercana."),
            ("Devolucion de materiales", "La devolucion registra movimiento y devuelve cantidad a un lote."),
            ("Solicitud de maquinaria", "Solo se pueden solicitar maquinas operativas. El uso queda activo hasta finalizarlo."),
            ("Finalizar uso de maquinaria", "El usuario solo libera las maquinas que tiene en uso."),
            ("Administracion", "Solo administradores gestionan usuarios, roles, logs, backups y estadisticas."),
            ("Logs", "Las acciones importantes quedan registradas para auditoria."),
            ("Backups", "El backup usa mysqldump y la restauracion usa mysql si estan disponibles en PATH."),
            ("Estadisticas", "Muestra recuentos, stock bajo, caducidades, estados de maquinas y uso de materiales.")
        ]
