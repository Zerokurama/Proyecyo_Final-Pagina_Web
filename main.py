# Programa de análisis de datos de muertes en Colombia por medio de una pagina web utilizando Streamlit. 

# Librerias necesarias para el programa main.py
import streamlit as st
import plotly.express as px

# Importar funciones para el analisis de datos y visualización en la pagina web
from datos.datos import cargar_datos
from datos.transformacion_datos import transformar_datos
from visualizacion.mapa_muertes import crear_mapa_muertes
from visualizacion.grafico_lineas import crear_grafico_lineas
from visualizacion.grafico_barras import crear_grafico_barras
from visualizacion.grafico_circular import crear_grafico_circular
from visualizacion.tabla import crear_tabla
from visualizacion.grafico_barras_apiladas import crear_grafico_barras_apiladas
from visualizacion.grafico_histograma import crear_grafico_histograma

def main():

    # 1. Cargar los datos
    df_muertes, df_codigos, df_divipola = cargar_datos()
    
    # 2. Transformar los datos para su analisis
    df_analisis_muertes = transformar_datos(df_muertes, df_codigos, df_divipola)
    
    # 3. Creacion de los graficos para la visualizacion en la pagina web
    fig_mapa = crear_mapa_muertes(df_analisis_muertes.copy())
    fig_lineas = crear_grafico_lineas(df_analisis_muertes.copy())
    fig_barras = crear_grafico_barras(df_analisis_muertes.copy())
    fig_circular = crear_grafico_circular(df_analisis_muertes.copy())
    tabla = crear_tabla(df_analisis_muertes.copy())
    fig_barras_apiladas = crear_grafico_barras_apiladas(df_analisis_muertes.copy())
    fig_histograma = crear_grafico_histograma(df_analisis_muertes.copy())
    
    # 4. Creacion de la pagina web

    st.set_page_config(
        page_title="Analisis defunciones-DANE(2019)",
        page_icon="📊",
        layout="wide",
    )
    st.sidebar.header("Menú de navegación")
    opcion = st.sidebar.radio("Selecciona una opción:", ["Inicio", "Vizualisacion de datos Colombia", "Visualizacion de datos Poblacion", "Final"])

    if opcion == "Inicio":
        st.title("Análisis de datos de defunciones en Colombia - DANE (2019)")
        st.markdown("---")
        st.write("Esta Web utiliza datos publicos del DANE para mostrar graficos interactivos sobre las defunciones en Colombia del 2019.")
        st.info("Selecciona una opción del menú de la izquierda para comenzar.")
    elif opcion == "Vizualisacion de datos Colombia":
        st.markdown("---")
        st.subheader("Visualizacion de datos Colombia")
        st.write("En este apartado encontrara graficos con relacion a los datos de los departamentos y municipios de colombia")
        st.markdown("---")
        st.plotly_chart(fig_mapa, use_container_width=True)
        st.plotly_chart(fig_barras, use_container_width=True)
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_lineas, use_container_width=True)
        with col2:
            st.plotly_chart(fig_circular, use_container_width=True)
    elif opcion == "Visualizacion de datos Poblacion":
        st.markdown("---")
        st.subheader("Visualizacion de datos Poblacion")
        st.write("En este apartado encontrara graficos con relacion a los datos de la problación de colombia")
        st.markdown("---")
        st.table(tabla)
        st.plotly_chart(fig_histograma, use_container_width=True)
        st.plotly_chart(fig_barras_apiladas, use_container_width=True)
    elif opcion == "Final":
        st.markdown("---")
        st.subheader("Final de la Pagina Web")
        st.markdown("---")
        st.info("Gracias por ver esta pagina web, espero que la información mostrada haya sido util para usted.")

        



if __name__ == "__main__":
    main()