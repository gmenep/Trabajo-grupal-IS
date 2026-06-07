from datetime import datetime


class FechaServicio:
    def normalizar_fecha(self, valor, nombre):
        if valor is None:
            return None
        texto = str(valor).strip()
        if texto == "":
            return None
        try:
            fecha = datetime.strptime(texto, "%Y-%m-%d")
        except ValueError:
            raise Exception(nombre + " debe ser una fecha real con formato yyyy-mm-dd")
        return fecha.strftime("%Y-%m-%d")

    def validar_orden(self, fecha_inicio, fecha_fin, nombre_inicio, nombre_fin):
        if fecha_inicio is None or fecha_fin is None:
            return
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        if fin < inicio:
            raise Exception(nombre_fin + " no puede ser anterior a " + nombre_inicio)
