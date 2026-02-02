# A01797412 - Actividad 4.2: Ejercicios de Programacion

**Materia:** Pruebas de Software y Aseguramiento de la Calidad
**Alumno:** A01797412
**Fecha:** Febrero 2026

---

## Descripcion del Proyecto

Este repositorio contiene la implementacion de 3 programas en Python siguiendo el estandar PEP-8 y verificados con pylint, como parte de la Actividad 4.2.

---

## Requerimientos de la Tarea

Cada programa debe cumplir con:
- Invocacion desde linea de comandos con archivo como parametro
- Calculos usando **algoritmos basicos** (sin funciones o librerias de estadisticas)
- Manejo de datos invalidos (mostrar errores y continuar ejecucion)
- Mostrar resultados en pantalla y guardar en archivo
- Incluir tiempo de ejecucion
- Cumplir con **PEP-8** y pasar **pylint**

---

## Programas Implementados

### 1. compute_statistics.py
Calcula estadisticas descriptivas de un archivo con numeros.

**Estadisticas calculadas:**
- COUNT (cantidad de numeros)
- MEAN (media/promedio)
- MEDIAN (mediana)
- MODE (moda)
- SD (desviacion estandar)
- VARIANCE (varianza)

**Uso:**
```bash
python compute_statistics.py fileWithData.txt
```

**Archivo de salida:** `StatisticsResults.txt`

---

### 2. convert_numbers.py
Convierte numeros a representacion binaria y hexadecimal.

**Caracteristicas:**
- Conversion a binario usando division sucesiva
- Conversion a hexadecimal
- Soporte para numeros negativos (complemento a 2)

**Uso:**
```bash
python convert_numbers.py fileWithData.txt
```

**Archivo de salida:** `ConvertionResults.txt`

---

### 3. word_count.py
Cuenta la frecuencia de palabras en un archivo de texto.

**Caracteristicas:**
- Identifica palabras distintas
- Cuenta frecuencia de cada palabra
- Ordena por frecuencia (descendente)

**Uso:**
```bash
python word_count.py fileWithData.txt
```

**Archivo de salida:** `WordCountResults.txt`

---

## Instalacion y Configuracion

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd A01797412_A4.2
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install pylint
```

---

## Ejecucion de Pruebas

### Ejecutar todos los tests con evidencia
```bash
source venv/bin/activate
python run_tests_p1.py  # Genera P1_TestEvidence.txt
python run_tests_p2.py  # Genera P2_TestEvidence.txt
python run_tests_p3.py  # Genera P3_TestEvidence.txt
```

### Ejecutar tests individuales
```bash
python compute_statistics.py test_files/TC1.txt
python convert_numbers.py test_files/P2_TC1.txt
python word_count.py test_files/P3_TC1.txt
```

---

## Resultados de Pruebas

### Programa 1: compute_statistics.py (7 casos de prueba)

```
======================================================================
EVIDENCIA DE EJECUCION - compute_statistics.py
======================================================================

TEST CASE 1: test_files/TC1.txt
----------------------------------------------------------------------
Error: Invalid data '405s' at line 400. Skipping.
COUNT: 399
MEAN: 241.9122807018
MEDIAN: 239
MODE: 393
SD: 145.3935564456
VARIANCE: 21139.2862558406
Elapsed Time: 0.000159 seconds

TEST CASE 5: test_files/TC5.txt
----------------------------------------------------------------------
Error: Invalid data 'ABA' at line 5. Skipping.
Error: Invalid data '23,45' at line 155. Skipping.
Error: Invalid data '11;54' at line 232. Skipping.
Error: Invalid data 'll' at line 239. Skipping.
COUNT: 307
MEAN: 241.4951140065
MEDIAN: 241
MODE: 393
SD: 145.702341648
VARIANCE: 21229.17236167
Elapsed Time: 0.000141 seconds

======================================================================
TODOS LOS CASOS DE PRUEBA EJECUTADOS EXITOSAMENTE
======================================================================
```

| TC | COUNT | Datos Invalidos Detectados |
|----|-------|---------------------------|
| TC1 | 399 | `405s` |
| TC2 | 1977 | - |
| TC3 | 12624 | - |
| TC4 | 12624 | - |
| TC5 | 307 | `ABA`, `23,45`, `11;54`, `ll` |
| TC6 | 3000 | - |
| TC7 | 12767 | `ABBA`, `ERROR` |

---

### Programa 2: convert_numbers.py (4 casos de prueba)

```
======================================================================
EVIDENCIA DE EJECUCION - convert_numbers.py
======================================================================

TEST CASE 3: test_files/P2_TC3.txt (numeros negativos)
----------------------------------------------------------------------
INDEX   NUMBER         BINARY                             HEXADECIMAL
-------------------------------------------------------------------------
1       -39            1111011001                         FFFFFFD9
2       -36            1111011100                         FFFFFFDC
3       8              1000                               8
...
Total numbers converted: 200

TEST CASE 4: test_files/P2_TC4.txt (con datos invalidos)
----------------------------------------------------------------------
Error: Invalid data 'ABC' at line 8. Skipping.
Error: Invalid data 'ERR' at line 21. Skipping.
Error: Invalid data 'VAL' at line 41. Skipping.
...
Total numbers converted: 38

======================================================================
TODOS LOS CASOS DE PRUEBA EJECUTADOS EXITOSAMENTE
======================================================================
```

---

### Programa 3: word_count.py (5 casos de prueba)

```
======================================================================
EVIDENCIA DE EJECUCION - word_count.py
======================================================================

TEST CASE 1: test_files/P3_TC1.txt
----------------------------------------------------------------------
WORD                          COUNT
----------------------------------------
conservative                  2
achievement                   1
adequate                      1
...
----------------------------------------
Total distinct words: 99
Total words: 100
Elapsed Time: 0.000629 seconds

======================================================================
TODOS LOS CASOS DE PRUEBA EJECUTADOS EXITOSAMENTE
======================================================================
```

---

## Resultados de Pylint

### Verificacion de codigo con pylint

```bash
$ pylint compute_statistics.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10

$ pylint convert_numbers.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10

$ pylint word_count.py
--------------------------------------------------------------------
Your code has been rated at 10.00/10
```

### Resumen de Scores

| Programa | Score Pylint | Estado |
|----------|-------------|--------|
| compute_statistics.py | 10.00/10 | PASS |
| convert_numbers.py | 10.00/10 | PASS |
| word_count.py | 10.00/10 | PASS |

**Nota:** Los unicos warnings menores (R0801 - codigo duplicado) son por patrones de manejo de errores similares entre archivos, lo cual es una practica estandar.

---

## Estructura del Proyecto

```
A01797412_A4.2/
├── README.md                    # Este archivo
├── compute_statistics.py        # Programa 1: Estadisticas
├── convert_numbers.py           # Programa 2: Conversion binario/hex
├── word_count.py                # Programa 3: Conteo de palabras
├── run_tests_p1.py              # Script de pruebas P1
├── run_tests_p2.py              # Script de pruebas P2
├── run_tests_p3.py              # Script de pruebas P3
├── P1_TestEvidence.txt          # Evidencia de ejecucion P1
├── P2_TestEvidence.txt          # Evidencia de ejecucion P2
├── P3_TestEvidence.txt          # Evidencia de ejecucion P3
├── StatisticsResults.txt        # Ultimo resultado de P1
├── ConvertionResults.txt        # Ultimo resultado de P2
├── WordCountResults.txt         # Ultimo resultado de P3
├── test_files/                  # Archivos de prueba
│   ├── TC1.txt ... TC7.txt      # Casos de prueba P1
│   ├── P2_TC1.txt ... P2_TC4.txt # Casos de prueba P2
│   └── P3_TC1.txt ... P3_TC5.txt # Casos de prueba P3
└── venv/                        # Entorno virtual Python
```

---

## Cumplimiento de Requerimientos

| Requerimiento | P1 | P2 | P3 |
|--------------|----|----|-----|
| Invocacion por linea de comandos | OK | OK | OK |
| Archivo como parametro | OK | OK | OK |
| Algoritmos basicos (sin librerias) | OK | OK | OK |
| Manejo de datos invalidos | OK | OK | OK |
| Resultados en pantalla | OK | OK | OK |
| Resultados en archivo | OK | OK | OK |
| Tiempo de ejecucion | OK | OK | OK |
| Cumple PEP-8 | OK | OK | OK |
| Pylint sin errores | OK | OK | OK |

---

## Autor

- **Matricula:** A01797412
- **Materia:** Pruebas de Software y Aseguramiento de la Calidad
- **Institucion:** Tecnologico de Monterrey
