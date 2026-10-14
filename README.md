# Manim Animations

Repositorio con animaciones creadas con [Manim](https://www.manim.community/) (Python) para
visualizar conceptos matematicos.

## Estructura

```text
manin/
├── FirstAnimation/
│   ├── firstTest.py              # Escenas: GraficoCalculo, LetterLaTex
│   ├── PropiedadTriangulo.py      # Escena: PropiedadTriangulo
│   ├── testPanda.ipynb           # Notebook auxiliar (pandas/matplotlib)
│   └── env/                      # Entorno virtual de Python (Python 3.14)
└── PropiedadesTrigonometricas/
    ├── trigonometria.py          # Escena: Trigonometria
    └── evn/                      # Entorno virtual de Python (Python 3.14)
```

## Requisitos previos

- Python 3.14 (recomendado, coincide con los entornos virtuales incluidos).
- En macOS, instala las dependencias nativas necesarias para Manim con Homebrew:

```bash
brew install ffmpeg cairo pango pkg-config
```

> Si usas Linux/Windows, consulta la documentacion oficial de Manim para las dependencias
> del sistema correspondientes.

## Entorno de desarrollo (Python)

Antes de ejecutar cualquier animacion debes activar un entorno virtual de Python.
Cada carpeta tiene su propio entorno.

### FirstAnimation

```bash
cd FirstAnimation

# Si el entorno no existe, crealo una vez:
python3 -m venv env

# Activa el entorno (hazlo siempre antes de ejecutar una animacion)
source env/bin/activate

# Instala/actualiza los paquetes usados
python -m pip install --upgrade pip
pip install manim

# (Opcional, para el notebook testPanda.ipynb)
pip install matplotlib pandas jupyter
```

### PropiedadesTrigonometricas

```bash
cd PropiedadesTrigonometricas

# Si el entorno no existe, crealo una vez:
python3 -m venv evn

# Activa el entorno (hazlo siempre antes de ejecutar una animacion)
source evn/bin/activate

# Instala/actualiza los paquetes usados
python -m pip install --upgrade pip
pip install manim
```

Para salir del entorno virtual:

```bash
deactivate
```

## Ejecutar las animaciones

Los comandos se ejecutan estando dentro de la carpeta del proyecto y con el entorno
virtual activado. Formato general:

```bash
manim -pql archivo.py NombreDeLaEscena
```

Opciones de calidad mas usadas:

- `-pql` : calidad baja (480p, 15 fps) y abre el video automaticamente.
- `-pqm` : calidad media (720p, 30 fps).
- `-pqh` : calidad alta (1080p, 60 fps).
- `-a`   : renderiza todas las escenas definidas en el archivo.

### FirstAnimation

```bash
cd FirstAnimation
source env/bin/activate

# Grafico de f(x)=x^2 con el area bajo la curva
manim -pql firstTest.py GraficoCalculo

# Teorema de Euler en LaTeX
manim -pql firstTest.py LetterLaTex

# Demostracion de que la suma de angulos de un triangulo es 180 grados
manim -pql PropiedadTriangulo.py PropiedadTriangulo

# Renderizar todas las escenas de un archivo
manim -pql -a firstTest.py
```

### PropiedadesTrigonometricas

```bash
cd PropiedadesTrigonometricas
source evn/bin/activate

# Identidad trigonometrica en el circulo unitario
manim -pql trigonometria.py Trigonometria

manim -pql CirculoUnitario.py UnitCircleAnimation

# Renderizar todas las escenas del archivo
manim -pql -a trigonometria.py
```

Si `manim` no se reconoce, ejecuta con el modulo de Python:

```bash
python -m manim -pql archivo.py NombreDeLaEscena
```

## Salida

Los videos generados se guardan por defecto en:

```text
media/videos/<nombre_del_archivo>/<calidad>/
```

Por ejemplo, la animacion de trigonometria se genera en
`PropiedadesTrigonometricas/media/videos/trigonometria/480p15/Trigonometria.mp4`.

## Paquetes usados

- `manim` (0.21.0) — motor de animacion.
- `numpy` — dependencia de Manim (trigonometria, arreglos, etc.).
- `matplotlib`, `pandas`, `jupyter` — usados en `FirstAnimation/testPanda.ipynb` (opcionales).
