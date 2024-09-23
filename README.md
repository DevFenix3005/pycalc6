# Proyecto de Calculadora en MVVM usando PySide6

Este proyecto es una calculadora de escritorio creada utilizando el patrón de diseño **MVVM** (Model-View-ViewModel) con **PySide6** para la interfaz gráfica y **Sympy** para la evaluación de expresiones matemáticas.

## Características

- Interfaz gráfica interactiva con botones para ingresar números y operadores.
- Evaluación de expresiones matemáticas usando Sympy.
- Manejo de historial de operaciones.
- Implementación del patrón **MVVM** para separar la lógica de negocio de la interfaz gráfica.
- Diseño de la interfaz gráfica utilizando **pyqt-tools**.
- Se escribieron algunos comandos con **poethepoet**, se usan de la siguiente manera `poe <comando>`:
  - updateview: Actualiza la vista
  - format: Da formato con ruff
  - check: Checa el formato con ruff
  - devstart: Inicia la aplicacion para probarla
  - devtest: Inicia las pruebas

## Requisitos

Este proyecto utiliza **Conda** para la creación y manejo de entornos, así como **Poetry** para la gestión de dependencias de Python. 

### Dependencias principales

- **Python 3.11**
- **PySide6**: Para la interfaz gráfica
- **Sympy**: Para la evaluación de expresiones matemáticas
- **pytest**: Para pruebas unitarias
- **Poetry**: Para la gestión de dependencias
- **Conda**: Para el entorno virtual y dependencias del sistema

## Instalación

### 1. Clonar el repositorio
Primero, clona el repositorio en tu máquina local:

```bash
git clone git@github.com:DevFenix3005/pycalc6.git
cd pycalc6
```

### 2. Crear el entorno con Conda

Asegúrate de tener **Conda** instalado. Luego, ejecuta el siguiente comando para crear el entorno virtual:

```bash
conda env create --name calculadora6 python=3.11
```

Esto instalará todas las dependencias del sistema necesarias.

### 3. Activar el entorno

Después de crear el entorno, actívalo:

```bash
conda activate calculadoraenv
```

### 4. Instalar dependencias de Python con Poetry

Con el entorno activado, instala las dependencias de Python usando **Poetry**:

```bash
poetry install
```

Esto instalará todas las librerías necesarias desde el archivo `pyproject.toml` y bloqueará las versiones en `poetry.lock`.

## Uso

Para ejecutar la calculadora, simplemente utiliza el comando definidor con `poethepoet`:

```bash
poe devstart
```

Esto abrirá la interfaz gráfica de la calculadora.

### Funcionalidades

- **Ingresar números**: Puedes hacer clic en los botones numéricos para ingresar números.
- **Operaciones**: Las operaciones básicas (+, -, *, /) están soportadas.
- **Igual (=)**: Evalúa la expresión matemática mostrada en la pantalla.
- **Borrar**: Borra el último carácter ingresado.
- **Limpiar**: Limpia toda la pantalla.
- **Historial**: Muestra el historial de operaciones realizadas.

## Pruebas

Este proyecto usa **pytest** para realizar pruebas unitarias. Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
poe runtest
```

Las pruebas se encuentran en la carpeta `src/test` y aseguran que el modelo y la lógica de la calculadora funcionen correctamente.

## Estructura del Proyecto

```
pycalc6/
│
├── assets/                                   # Carpeta de recursos
|
├── src/
|   ├──main/
│   │   ├── controller/
│   │   │     └── calculadora_controller.py   # Controlador que une la lógica entre el modelo y la vista
│   │   ├── model/
│   │   │     └── calculadora_model.py        # Modelo para resolver las expresiones matemáticas
│   │   ├── ui/
│   │   │     └── gen/                        # Archivos generados para la interfaz gráfica
│   │   ├── viewmodel/
│   │   │     └── calculadora_viewmodel.py    # Lógica que conecta el modelo con la vista
│   │   └── main.py                           # Punto de entrada del programa
│   │
│   └─test/
│       └── calculadora_model_test.py         # Pruebas unitarias para el modelo
│
├── LICENSE                              # Información de licencia
├── README.md                            # Este archivo
├── pyproject.toml                       # Definición de dependencias y configuración del proyecto
```

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Realiza un fork del repositorio.
2. Crea una rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Créditos

Este proyecto fue desarrollado por Roberto D. Cazarin en el contexto de un proyecto de aprendizaje de **Python** y **PySide6**.