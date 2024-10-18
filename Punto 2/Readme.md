## Punto 2
Diseñe una gramática para un lenguaje de programación que
realice las siguientes funciones:
 - Aplicar una función sobre los ítems de un objeto iterable
(lista, tupla, etc...)
o Ejemplo MAP(function, objeto iterable)
### 1. Descargar el Archivo Proyecto
Antes de comenzar, debes descargar los archivos necesarios desde este repositorio de GitHub llamados:
```bash
funciones.py
objeto.txt
objiterable.g4
```
se sugiere dejarlos en una carpeta propia, en este caso usaremos una carpeta creada llamada prueba2
### 2. Instalar el antlr 
En la terminal navegamos hasta la carpeta donde descargamos los archivos anteriores y ingresamos el curl del antlr
```bash
cd prueba2
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Exporta la variable de entorno en la carpeta:
```bash
export CLASSPATH=".:/home/juan-wilches/prueba2/antlr-4.13.2-complete.jar:$CLASSPATH"
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
### 4.Compilaremos la gramatica objiterable.g4
ingresaremos el siguiente comando, donde se debe de modificar la direcion de la carpeta que tu creaste para guardar los archivos de este github y del antlr, este es el comando para la carpeta llamada prueba que dijimos en el paso 1
```bash
java -jar /home/juan-wilches/prueba2/antlr-4.13.2-complete.jar -Dlanguage=Python3 objiterable.g4
```
### 5.Ejecución
el siguiente comando mostrara las operaciones ingresadas en el archivo objeto.txt y sus resultados
```bash
python ~/prueba2/funciones.py ~/prueba2/objeto.txt
```
La ejecucion quedaria de la siguiente manera:
![image](https://github.com/user-attachments/assets/b6efe2ee-afa7-4e30-b0ec-fb62c2ed45e1)

el codigo cumple con las funciones cuadrado, par, doble, impar,incrementa de 1, desincrementa de 1, el valor absoluto de numeros -.
