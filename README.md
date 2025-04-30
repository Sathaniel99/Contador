# Contador de Valores

## Descripción

**Contador** es una aplicación sencilla desarrollada en Python utilizando la biblioteca `tkinter` para la interfaz gráfica. Esta aplicación permite llevar un registro de dos valores (P y S) que se pueden incrementar o decrementar mediante botones. Los valores se guardan automáticamente en un archivo `Contador.ini` ubicado en la carpeta `Documents` del usuario, asegurando que los datos persistan entre sesiones.

## Características

- **Interfaz Gráfica Intuitiva**: Diseño simple y fácil de usar con botones para incrementar y decrementar valores.
- **Persistencia de Datos**: Los valores se guardan automáticamente en un archivo, permitiendo recuperar el estado anterior al cerrar y reabrir la aplicación.
- **Manejo de Errores**: Notificaciones de error en caso de problemas de permisos o acceso a archivos.
- **Compatibilidad con PyInstaller**: Soporte para convertir la aplicación en un ejecutable independiente.

## Requisitos

- Python 3.x
- Biblioteca `tkinter` (incluida con Python estándar)

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/Sathaniel99/Contador.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd contador
    ```

3. Ejecuta la aplicación:
    ```bash
    python contador.py
    ```

4. Compilar la aplicación:
    ```bash
    pyinstaller --onefile --add-data "icon_exe.ico;." --icon="icon_exe.ico"  Contador.py
    ```

## Uso

1. **Incrementar/Decrementar Valores**:
    - Utiliza los botones `+` y `-` en cada sección (Pxxx y Sxxx) para modificar los valores.

2. **Cierre Automático**:
    - Al cerrar la aplicación, los valores actuales se guardarán automáticamente en el archivo `Contador.ini`.

## Estructura del Código

- **resource_path**: Función para obtener rutas relativas, útil para la compatibilidad con PyInstaller.
- **EditorTXT**: Clase principal que maneja la lógica y la interfaz de la aplicación.
  - **__init__**: Inicializa la ventana y carga los valores iniciales.
  - **cargar_valores**: Lee los valores desde el archivo `Contador.ini`.
  - **guardar_valores**: Guarda los valores actuales en el archivo `Contador.ini`.
  - **crear_interfaz**: Crea la interfaz gráfica con `tkinter`.
  - **cambiar_valor**: Maneja la lógica para incrementar o decrementar los valores.
  - **actualizar_labels**: Actualiza las etiquetas de la interfaz con los valores actuales.
  - **on_closing**: Guarda los valores y cierra la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para discutir cualquier cambio.