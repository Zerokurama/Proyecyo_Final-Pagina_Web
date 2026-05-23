# Creacion del grafico de barras de 5 ciudades con mas muertes por homicidio en Colombia

import pandas as pd
import plotly.express as px

def crear_grafico_barras(df_analisis_muertes: pd.DataFrame) -> px.bar:
    """
    Crea un gráfico de barras de Homicidios por ciudad utilizando Plotly Express.
    Args:
        df_analisis_muertes (pd.DataFrame): DataFrame con los datos de muertes.
    Returns:
        px.bar: Gráfico de barras de Homicidios por ciudad.
    """

    # Filtrar el DataFrame para obtener solo las muertes por homicidio
    df_homicidios = df_analisis_muertes[df_analisis_muertes['MANERA_MUERTE'] == 'Homicidio']
    df_homicidio_municipio = df_homicidios[df_homicidios['COD_MUERTE'].str.startswith('X95')]

    # Crear una nueva columna que combine el nombre del municipio y el departamento para mostrar en el gráfico de barras
    df_homicidio_municipio['CIUDAD'] = df_homicidio_municipio['MUNICIPIO'] + " (" + df_homicidio_municipio['DEPARTAMENTO'] + ")"
    df_top5 = df_homicidio_municipio.groupby('CIUDAD').size().reset_index(name='Homicidios')

    # Ordenar el DataFrame por la cantidad de homicidios y seleccionar las 5 ciudades con más homicidios
    df_top5 = df_top5.sort_values(by='Homicidios', ascending=False).head(5)
    df_top5 = df_top5.sort_values(by='Homicidios', ascending=True)

    # Crear el gráfico de barras de muertes por departamento utilizando Plotly Express
    bar = px.bar(
        df_top5,
        x='CIUDAD',
        y='Homicidios',
        title="Gráfico de Barras de Homicidios por Ciudad en Colombia",
        labels={"CIUDAD": "Ciudad (Departamento)", "Homicidios": "Homicidios"},
        color="Homicidios",
        color_continuous_scale='haline',
    )

    # Personaliza el diseño del gráfico
    bar.update_layout(
        plot_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="#eeeeee"),
        yaxis=dict(showgrid=True, gridcolor="#eeeeee")
    )

    # Configura los colores y el estilo de las barras
    bar.update_traces(
        marker=dict(line=dict(color="#333333", width=1)),
        hovertemplate= "Ciudad: %{x}<br> " + "Homicidios: %{y:,.0f} <extra></extra>"
    )
    
    return bar