# Creacion del grafico de lineas de muertes por mes

import pandas as pd
import plotly.express as px

def crear_grafico_lineas(df_analisis_muertes: pd.DataFrame) -> px.line:
    """
    Crea un gráfico de líneas de muertes por mes utilizando Plotly Express.
    Args:
        df_analisis_muertes (pd.DataFrame): DataFrame con los datos de muertes.
    Returns:
        px.line: Gráfico de líneas de muertes por mes.
    """
    
    # Agrupa los datos por mes y cuenta el número de muertes en cada mes
    df_analisis_muertes_mes = df_analisis_muertes.groupby('MES').size().reset_index(name='total_muertes')
    df_analisis_muertes_mes = df_analisis_muertes_mes.sort_values(by='MES')

    # Se crea un diccionario para mapear los números de mes a nombres de mes abreviados
    diccionario_meses = {
        1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
        7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic"
    }

    # Se mapea la columna 'MES' utilizando el diccionario para obtener los nombres de mes abreviados
    df_analisis_muertes_mes['MES'] = df_analisis_muertes_mes['MES'].map(diccionario_meses)

    # Crear el gráfico de líneas de muertes por mes utilizando Plotly Express
    line = px.line(
        df_analisis_muertes_mes,
        x='MES',
        y="total_muertes",
        title="Gráfico de Líneas de Muertes por Mes en Colombia",
        labels={"MES": "Mes del año", "total_muertes": "Total de Muertes"},
        markers=True
    )

    # Personaliza el diseño del gráfico

    # Configura los ticks del eje x para mostrar todos los meses
    line.update_xaxes( dtick=1)

    # Configura el modo de hover para mostrar información detallada al pasar el cursor sobre los puntos de datos
    line.update_layout(
        hovermode="x unified",
        hoverlabel=dict(
            namelength=0,
            bgcolor="rgba(255, 255, 255)",
            font_size=13
        ),
        plot_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="#eeeeee"),
        yaxis=dict(showgrid=True, gridcolor="#eeeeee")
    )

    # Configura los colores y el estilo de la línea y los marcadores
    line.update_traces(
        line=dict(color="#1f77b4", width=4),
        marker=dict(size=8, color="#1f77b4"),
        hovertemplate= "Mes: %{x}<br> " + "Casos: %{y:,.0f} <extra></extra>",
    )
    
    return line