# Creacion del mapa de muertes por departamento

import pandas as pd
import plotly.express as px
import requests

def crear_mapa_muertes(df_analisis_muertes: pd.DataFrame) -> px.choropleth:
    """
    Crea un mapa coroplético de muertes por departamento utilizando Plotly Express.
    Args:
        df_analisis_muertes (pd.DataFrame): DataFrame con los datos de muertes.
    Returns:
        px.choropleth: Mapa de muertes por departamento.
    """
    # Se asegura de que el código del departamento esté en formato string con ceros a la izquierda si es necesario
    df_analisis_muertes['COD_DEPARTAMENTO'] = df_analisis_muertes['COD_DEPARTAMENTO'].astype(str).str.zfill(2)

    df_analisis_muertes_agrupado = df_analisis_muertes.groupby(['COD_DEPARTAMENTO', 'DEPARTAMENTO']).size().reset_index(name='Cantidad_Muertes')

    # Cargar el GeoJSON de John Guerra
    url_geojson = "https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json"
    colombia_geojson = requests.get(url_geojson).json()

    # Definir una escala de colores personalizada para el mapa
    escala_color= [
        [0.0, "#f54b4b"],
        [0.5, "#5E0404"],
        [1.0, "#5C0D0D"]
    ]
    # se crea el mapa utilizando el código del departamento como vínculo entre el DataFrame y el GeoJSON
    map = px.choropleth(
        df_analisis_muertes_agrupado,
        geojson=colombia_geojson,
        locations="COD_DEPARTAMENTO",
        featureidkey="properties.DPTO",
        color="Cantidad_Muertes",
        labels={"Cantidad_Muertes": "Cantidad de Casos"},
        hover_name="DEPARTAMENTO",
        color_continuous_scale=escala_color,
        title="Mapa de Muertes por Departamento en Colombia"
    )

    # Personaliza el diseño del mapa

    # Ajusta el enfoque del mapa para centrarse en Colombia
    map.update_geos(fitbounds="locations", visible=True)

    # Configura los márgenes y el tamaño del título para mejorar la apariencia del mapa
    map.update_layout(
        margin={"r":0,"t":50,"l":0,"b":0},
        title_font_size=24
    )

    # Configura el modo de hover para mostrar información detallada al pasar el cursor sobre los departamentos
    map.update_traces(
        hovertemplate="<b> %{hovertext}</b> <br> " +
            "Código DANE: %{location}<br> " +
            "Casos: %{z:,.0f} <extra></extra>",
        marker_line_width=0.5, marker_line_color="white"
    )
    
    return map