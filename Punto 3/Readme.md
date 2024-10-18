## Punto 3
. Diseñe una gramática para un lenguaje de programación que
calcule la transformada de Fourier.
### 1. Descargar el Archivo Proyecto
Antes de comenzar, debes descargar los archivos necesarios desde este repositorio de GitHub llamados:
```bash
fourier_transform.py
expresion.txt
FourierLexer.py
FourierParser.py
ourierListener.py
Fourier.g4
```
se sugiere dejarlos en una carpeta propia, en este caso usaremos una carpeta creada llamada prueba3
### 2. Instalar el antlr 
En la terminal navegamos hasta la carpeta donde descargamos los archivos anteriores y ingresamos el curl del antlr
```bash
cd prueba3
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Exporta la variable de entorno en la carpeta:
```bash
export CLASSPATH=".:/home/juan-wilches/prueba3/antlr-4.13.2-complete.jar:$CLASSPATH"
```

### 3. Crear entorno y instalar el antlr para python
Necesitamos de un entorno virtual para poder usar el antlr con el pip
```bash
python3 -m venv venv
```
Activaremos el entorno virtual y instalaremos el antlr
```bash
source venv/bin/activate
pip install antlr4-python3-runtime==4.13.2
```
### 4.Compilaremos la gramatica Fourier.g4
ingresaremos el siguiente comando, donde se debe de modificar la direcion de la carpeta que tu creaste para guardar los archivos de este github y del antlr, este es el comando para la carpeta llamada prueba que dijimos en el paso 1
```bash
java -jar /home/juan-wilches/prueba3/antlr-4.13.2-complete.jar -Dlanguage=Python3 objiterable.g4
```
### 5.Ejecución
el siguiente comando mostrara las operaciones ingresadas en el archivo expresion.txt
 y sus resultados
```bash
python3 fourier_transform.py

```
