# Creación del gráfico circular para mostrar los municipios con menor indice de mortalidad

import pandas as pd
import plotly.express as px

def crear_grafico_circular(df_analisis_muertes: pd.DataFrame) -> px.pie:
    """
    Crea un gráfico circular de los 10 municipios con menor índice de mortalidad utilizando Plotly Express.
    Args:
        df_analisis_muertes (pd.DataFrame): DataFrame con los datos de muertes.
    Returns:
        px.pie: Gráfico circular de muertes por departamento.
    """
    
    # Filtrar el DataFrame para obtener solo las muertes por homicidio
    df_analisis_muertes ['CIUDAD'] = df_analisis_muertes['MUNICIPIO'] + " (" + df_analisis_muertes['DEPARTAMENTO'] + ")"
    df_municipio = df_analisis_muertes.groupby('CIUDAD').size().reset_index(name='Muertes')
    df_municipio_top10 = df_municipio.sort_values(by='Muertes', ascending=True).head(10)
    # Tomamos de menor a mayor los 10 municipios con menor indice de mortalidad
    
    # Crear el gráfico circular utilizando Plotly Express
    pie = px.pie(
        df_municipio_top10, 
        values= 'Muertes', 
        names= 'CIUDAD',
        title='Top 10 Municipios con Menor Índice de Mortalidad en Colombia',
        color='Muertes',
        color_discrete_sequence= px.colors.qualitative.Prism
    )
    
    # Personalizar el diseño del gráfico
    pie.update_layout(
        showlegend=False,
        margin=dict(t=50, b=20, l=20, r=20),
        legend_title_text='Municipios'
    )
    pie.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate= "Municipio: %{label}<br> " + "Casos: %{value:,.0f} <extra></extra>",
        marker=dict(
            line=dict(color='#FFFFFF', width=2)
        )
    )

    return pie