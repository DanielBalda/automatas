# <div align="center"><a name="introduccion"> Autómatas y Gramáticas </a>
<p align="center">
  <img src="https://media3.giphy.com/media/L1R1tvI9svkIWwpVYr/200w.webp?cid=ecf05e4765u0zjv23vmsfmb51gf7il494gbhm55ve4xk2uzq&rid=200w.webp&ct=g" width=400 />
</p>


------------
Autómatas y Gramáticas es un proyecto realizado en python que permite al usuario, a partir de un registro, hacer seguimiento de las personas que se conectaron a la red días feriados y no laborales.

Para esto se le brinda al usuario final la posibilidad de ingresar un rango de fechas.

## <a name="historia">Procedimientos 📜 </a>

<p>Por empezar se nos brindó la consigna que consistía en hacer seguimiento de aquellos usuarios que se conectaron a una red específica los días feriados y no laborales (Sábados y Domingos), con la posibilidad de ingresar un rango de fechas.</p>
<p>Comenzamos realizando los análisis de requerimientos solicitados. Se realizó un planteo de soluciones y posibles problemas. Se plantéo utilizar:</p>
<ul>
	<li>Expresiones regulares para:
		<ul>a. Verificación de fechas ingresadas en la aplicación, como también reconocimiento de fechas en el archivo provisto.</ul>
		<ul>b. Verificación de aquellas direcciones <span>*ID*</span> con 16 caracteres alfanuméricos.</ul>
		<ul>c. Verificación del horario en formato 24hr. </ul>
	<li>Comprobación y eliminación de espacios en blanco contenidos en el archivo de registro provisto</li>
	<li>Consultas a una API por cuestiones de practicidad y simplicidad. En nuestro caso utilizamos la API provista por 'http://nolaborables.com.ar', la cual 		nos permitió obtener desde el año 2011 todos aquellos días feriados.</li>
	<li>Tkinter. Una librería intuitiva de python que le brinda al usuario final una interfaz amigable permitiendole facilidad en el uso de la aplicación. Para 		el programa se estableció una resolución claramente visible para el usuario (915x900px), en el cual se le da la opción de importar un archivo y a su vez 		exportarlo. Podrá ingresar también un rango de fechas a analizar, el cual los colores:</li>
		<ul>🟢 Nos indicará que la fecha fue ingresada correctamente.</ul>
		<ul>🔴 Nos indicará que la fecha fue ingresada incorrectamente.</ul>
	
</ul>
<p>En cuanto a python se utilizó:</p>
	<ul>
		<li>"re",módulo que nos proporciona operaciones de coincidencia de expresiones regulares.</li>
		<li>"requests", el cual era necesario para consumir la API.</li>
		<li>"datetime", módulo para manipular fechas y horas.</li>
		<li>"pandas", poderoso open source de analisis de datos y herramientas de manipulación.El cual utilizamos los siguientes métodos para nuestra 			finalidad:</li>
			<ul>➡️bdate_range()</ul>
			<ul>➡️DataFrame()</ul>
		<li>"locale", librería para leer/escribir archivos de Excel 2010 con extensiones xlsx/xlsm/xltx/xltm.</li>
	</ul>

<p>💡Ante posibles fallas en la API , ya sea por indisponibilidad online o modificación, decidimos proporcionar un archivo de texto con todos los días feriados desde el año 2011 hasta el presente año, incluyendo futuros años.</p>

------------
<ol>
<li><a href="#introduccion">Descripción</a></li>
<li><a href="#historia">Procedimientos</a></li>
<li><a href="#instalacion">Instalación</a></li>
<li><a href="#archivos">Archivos Soportados</a></li>
<li><a href="#librerias">Librerías Utilizadas</a></li>
<li><a href="#tutorial">Tutorial</a></li>
</ol>

## <a name="instalacion">Instalación 🧪 </a>

------------

#### *Clonar repositorio*
 $ `git clone https://github.com/DanielBalda/automatas.git`
#### *Instalar dependencias*
 $` Abrir terminal y escribir "./install.sh".`

###### Uso:

	 1) Abrir terminal y ejecutar Proyecto Automatas.py
	 2) En el botón "Abrir Archivo" seleccioná tu registro
	 3) Ingrese rango de fechas
	 4) Finalmente presione "Buscar"


###### Exportar archivo:
	 1) Seleccionar "Exportar"
	 2) Luego "Guardar"
------------
### <a name="archivos"> Archivos soportados </a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔴IMPORTANTE❗🔴
 ✔️.txt
 ✔️.xlsx
 ✔️.csv

------------
### <a name="librerias"> Librerias utilizadas  📚 </a>
💎os
💎sys
💎re
💎openpyxl
💎time
💎datetime
💎pandas
💎tkinter
💎prettytable
💎locale
💎requests

------------
## Tutorial
>Paso 1: Abrir Archivo

<p><img src="https://github.com/DanielBalda/automatas/blob/main/release/images/abrir_archivo.png" align="left" height="400" width="400" position="r"></div>
<p><img src="https://github.com/DanielBalda/automatas/blob/main/release/images/abrir.png" align="center" height="400" width="400" ></p>

>Paso 2: Insertar Fechas

<p><img src="https://github.com/DanielBalda/automatas/blob/main/release/images/fechas_correctas.png" align="left" height="400" width="400" position="r"></div>
<p><img src="https://github.com/DanielBalda/automatas/blob/main/release/images/fechas_incorrectas.png" align="center" height="400" width="400" ></p>

>Paso 3: Exportar registro

<p><img src="https://github.com/DanielBalda/automatas/blob/main/release/images/exportar_boton.png" align="left" height="400" width="400" position="r"></div>
<p><img src="https://github.com/DanielBalda/automatas/blob/main/release/images/exportar_nombre.png" align="center" height="400" width="400" ></p>
