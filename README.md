## INTRODUCCION DEL PROYECTO

La aplicacion tiene como propocito el generar graficos interactivos con los datos de defunciones del DANE del 2019 para su analisis.  

## OBJETIVO

La aplicacion buca analizar el comportamiento de las defunciones en Colombia en el 2019 en los diferentes departamentos y como estos afectan en la poblacion.

## ESTRUCTURA DEL PROYECTO

El proyecto esta dividido por:  
Archivo main.py: encargada de ejecutar el programa y diseño de la pagina web.  
Carpeta datos: trae dentro la base de datos, un archivo para el carge de los mismos y un archivo para la transformacion de los datos.  
Carpeta visualizacion: Trae dentro los archivos de la creacion de graficos.

## REQUISITOS

Librerias usadas en la aplicacion:

streamlit  
pandas  
plotly  
openpyxl  
requests

## DESPLIEGUE EN AZURE APP SERVICE

Los pasos para realizar el despliegue en azure app service son los siguientes:

1. Crear una cuenta como estuciante en azure.
2. Busca en la barra superior App Services
3. Va a donde dice crear (create) y selecciona aplicacion web (web app)
4. Configura la pagina web y despues le da a revisar y crear (review and create), revisa que todo este en orden y le da a crear (create).
5. Una vez creado le da en ir a recursos (go to resource).
6. selecciona barra izquierda implementazión (deployment), despues Centro de implementación (deployment center)
7. En origen (source) escoger GitHub y autorizar
8. Seleccionar el repositorio (repository) y la rama (breach) de su app y le da en guardar (save).
9. Barra lateral izquiera, configuracion (settings), configuracion (configuration), configuracion de la pila (stack settings) y por ultimo comando de inicio (start command).
10. Colocar startup.sh (si se creo el archivo) o streamlit run main.py --server.port 8000 --server.address 0.0.0.0 (si no tiene el archivo creado).
11. Introducción (Overview), click en dominio predeterminado (Default Domain) y listo, su aplicacion web esta lista.

## SOFTWARE UTILIZADOS

Python 
Streamlit  
Plotly  
Pandas  
Visual Studio Code  
GitHub  
Azure App Service

## VISUALIZACIONES E INSTERPRETACION DE RESULTADOS

!["Mapa"](/Imagenes/Mapa.png)

Interpretación: Se puede observar ques reguiones con tonos más oscuros son las que más casos de mortalidad tienen en Colombia. Lideradas por departamentos que tiene alta concentracion de población como lo son Antioquia, el Valle del Cauca y el Distrito Capital de Bogotá. Caso contrario  como son Amazonía y Orinoquía por tener menor dencidad de poblacion.

!["Linea"](/Imagenes/Linea.png)

Interpretación: En el grafico se puede evidenciar un bajon de casos de mortalidad en el mes de febrero, sin embargo, el mes de diciembre es donde más casos de mortalidad en colombia hubo en el año 2019 causa de ser un mes muy festivo.

!["Barras"](/Imagenes/Barras.png)

Interpretación: En la grafica se puede evidenciar que Santiago de Cali es el municipio con más casos de homicidios por agresiones con disparo de armas de fuego y casos no especificados (codigo x95) con una diferencia de 370 casos en comparacion de Bogotá D.C. Estos dos junto con los municipios de Medellin, Barranquilla y San José de Cúcuta lideran la tabla con mayores casos de mortalidad en Colombia.

!["Pie"](/Imagenes/Circular.png)

Interpretación: Al observar los 10 minicipios con menor cantidad de mortalidad en Colombia se puede observar que todos cuentan con el mismo numero de casos haciendo la mortalidad sea un evento poco comun en estos municipios.

!["Tabla"](/Imagenes/Tabla.png)

Interpretación: Se puede evidenciar que gran parte de los casos de muerte en la poblacion colombiana en el 2019 es por manera Natural, sin embargo, hay uno en especifico que no es Natural sino Homicidio y es el caso del codigo X954 (Agresion con disparo de otras armas de fuego, y las no especificadas, calles y carreteras). Visivilizando un impacto directo de la violencia civil que sufen los colombianos frente a las patologias medicas (mnuertes naturales).

!["Barras_Apiladas"](/Imagenes/Barras_Apiladas.png)

Interpretación: En el 2019 la mortalidad Masculina supera sistematicamente a la Femenina en todo el territorio colombiano. Esto devido mayoritariamente a los caso de accidentes de transito y eventos de violencia armada que hay en el pais.

!["Histograma"](/Imagenes/Histograma.png)

Interpretación: El histograma muestra un comportamiento tipico en la curva de vida ya que en el 2019 el segmento de vejez/longevidad muestra el mayor caso de mortalidad estos siendo personas de 60 a 84 años de edad, sin embarho, la mortalidad neonatal tiene un indice de casos mayor que la adolecencia, macando un punto critico en la atencio de las politicas de la salud materno-infantil en el pais.


