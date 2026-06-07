# LabTrack

LabTrack es una aplicacion de escritorio local para gestion de laboratorios de investigacion. Usa Python, PyQt5, MySQL y conexion JDBC con `jaydebeapi`.

## Requisitos

- Python 3.12 del proyecto.
- Java JDK instalado y disponible para JPype.
- MySQL local con la base de datos `labtrack`.
- `lib/mysql-connector-j-9.6.0.jar`.
- Dependencias de `requirements.txt`: PyQt5, jaydebeapi, JPype1 y bcrypt.

## Instalacion

1. Crear la base de datos en MySQL.
2. Importar `labtrack_structure.sql`.
3. Colocar `mysql-connector-j-9.6.0.jar` en `lib`.
4. Instalar dependencias.
5. Configurar credenciales si no se usa `root/changeme`:
   - `LABTRACK_DB_HOST`
   - `LABTRACK_DB_NAME`
   - `LABTRACK_DB_USER`
   - `LABTRACK_DB_PASSWORD`
6. Ejecutar el seed:

```powershell
.local\python312\python.exe pruebas\seed_datos_prueba.py
```

7. Ejecutar la app:

```powershell
.local\python312\python.exe main.py
```

## Usuarios de prueba

- admin / admin123
- director / director123
- investigador / investigador123
- auditor / auditor123
- tecnico / tecnico123
- reponedor / reponedor123

Las contrasenas se guardan como hash bcrypt. El seed contiene las claves iniciales solo para generar hashes de prueba, no las guarda en texto plano.

## Arquitectura

La aplicacion sigue MVC:

- `src/vista`: clases de vista que cargan los `.ui`.
- `src/controlador`: conecta eventos de la vista con servicios.
- `src/modelo`: reglas de negocio y permisos.
- `src/modelo/dao`: SQL y acceso JDBC a MySQL.
- `src/modelo/vo`: objetos de datos inmutables.

Los DAO usan consultas parametrizadas con `?`. Las vistas y controladores no contienen SQL. El modelo no importa PyQt5.

## VO inmutables

Los VO tienen constructor, atributos privados y propiedades de lectura. No tienen setters. Si un dato cambia se crea otro VO con los valores nuevos.

## Conexion JDBC y Singleton

`src/modelo/conexion/Conexion.py` aplica Singleton sin metaclases. Usa `jaydebeapi`, `JPype1` y el jar relativo `lib/mysql-connector-j-9.6.0.jar`. Tras conectar intenta desactivar autocommit con `setAutoCommit(False)` para controlar `commit` y `rollback`.

## Observer de logs

Los servicios crean un `LogVo` cuando una accion relevante termina. `SujetoAuditoria` notifica a `LogObserver`, que registra el evento mediante `LogDaoJDBC`.

## Permisos

Los permisos se aplican en dos niveles:

- UI: `MainWindow` solo muestra paginas autorizadas y cada vista oculta botones no permitidos.
- Servicio: antes de ejecutar una accion se comprueba el permiso. Si falla, se registra `ACCION_NO_AUTORIZADA`.

Permisos principales:

- Inventario: Administrador, Reponedor.
- Maquinaria: Administrador, Tecnico.
- Proyectos: Investigador, Director, Auditor.
- Panel: Investigador, Director, Administrador.
- Administracion, backups y estadisticas: Administrador.
- Logs: Administrador, Auditor, Director.
- Ayuda y salir: todos.

## Funcionalidades

Inventario permite buscar por nombre y almacen, crear materiales, crear lotes, modificar cantidades, mover lotes, eliminar lotes o materiales, solicitar material y devolverlo desde proyectos.

Maquinaria permite buscar, crear, modificar, mover, retirar o eliminar maquinas, registrar mantenimiento, solicitar uso y finalizar uso.

Proyectos muestra proyectos, estudios y miembros segun permisos. Directores pueden agregar o quitar usuarios de un proyecto.

Panel colaborativo muestra entradas y abre una ventana de detalle con el texto completo. Administradores y directores pueden modificar o eliminar entradas.

Administracion permite gestionar usuarios, roles, logs, backups y estadisticas.

Backups usa `mysqldump` y restauracion usa `mysql`. Si no estan en PATH, la app muestra un mensaje claro.

## Tablas nuevas

Se agregan a `labtrack_structure.sql`:

- `machine_usage`: usos activos y finalizados de maquinaria.
- `material_movements`: trazabilidad de entradas, salidas, solicitudes, devoluciones y movimientos.
- `machine_location`: ubicacion de maquinas en almacenes.
- `panel_entries`: entradas reales del panel colaborativo.

## Validacion

Comando principal:

```powershell
.local\python312\python.exe -m compileall src
```

Despues de validar se deben eliminar `__pycache__` y `*.pyc` generados.

## Problemas comunes

- Si falla la conexion, revisar MySQL, credenciales y nombre de base de datos.
- Si falla JPype, revisar que Java JDK este instalado.
- Si falla JDBC, revisar que el jar este en `lib`.
- Si backup o restauracion falla, revisar `mysqldump` y `mysql` en PATH.

## Carpeta pruebas

- Esta carpeta contiene lo necesario para cargar datos para realizar pruebas en la app
