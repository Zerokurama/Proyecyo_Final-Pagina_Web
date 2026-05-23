import pandas as pd
import plotly.express as px


def crear_grafico_histograma(df_analisis_muertes: pd.DataFrame)->px.bar:
    """"
    Crea un gráfico de histograma de edades agrupadas y categorizadas utilizando Plotly Express.
    Args:
        df_analisis_muertes (pd.DataFrame): DataFrame con los datos de muertes.
    Returns:
        px.bar: Gráfico de historgrama de edades agrupadas y actegorizadas.
    """
    # Se crean las dos columnas en el DataFrame
    df_analisis_muertes['Categoria_Edad'] = df_analisis_muertes['GRUPO_EDAD1'].apply(lambda x: mapear_edad_completo(x)[0])
    df_analisis_muertes['Rango_Edad'] = df_analisis_muertes['GRUPO_EDAD1'].apply(lambda x: mapear_edad_completo(x)[1])

    # Se agrupan por categoría y rango al tiempo para mantenerlos amarrados
    df_conteo = df_analisis_muertes.groupby(['Categoria_Edad', 'Rango_Edad']).size().reset_index(name='Cantidad_Casos')

    # Se define el orden  de las barras
    orden_cronologico = [
        "Mortalidad neonatal", "Mortalidad infantil", "Primera infancia", 
        "Niñez", "Adolescencia", "Juventud", "Adultez temprana", 
        "Adultez intermedia", "Vejez", "Longevidad / Centenarios", "Edad desconocida"
    ]

    # Se crea el grafico de histograma usando px.bar()
    histogram = px.bar(
        df_conteo,
        x='Categoria_Edad',
        y='Cantidad_Casos',
        custom_data=['Rango_Edad'],
        title='Distribución y Frecuencia de Muertes por Grupo de Edad',
        labels={'Categoria_Edad': 'Etapa de Vida', 'Cantidad_Casos': 'Cantidad de Defunciones'},
        category_orders={'Categoria_Edad': orden_cronologico}
    )

    # Perzonalizacion del grafico
    histogram.update_traces(
        marker_color='#2A9D8F',
        texttemplate='%{y:,.0f}',
        textposition='outside',
        hovertemplate=(
            "<b>Etapa:</b> %{x}<br>"
            "<b>Edades:</b> %{customdata[0]}<br>"
            "<b>Cantidad de casos:</b> %{y:,.0f} muertes<extra></extra>"
        )
    )

    # Ajusta el diseño de la gráfica
    histogram.update_layout(
        plot_bgcolor='white',
        yaxis=dict(showgrid=True, gridcolor='#f0f0f0', title="Número de Casos"),
        margin=dict(t=60, b=120, l=50, r=30)
    )
    return histogram

# Funcion para categorizar y agrupar las edades
def mapear_edad_completo(codigo):
    try:
        codigo = int(codigo)
    except:
        return "Edad desconocida", "Edad Desconocida"
    
    if 0 <= codigo <= 4:
        return "Mortalidad neonatal", "menos de un mes"
    elif 5 <= codigo <= 6:
        return "Mortalidad infantil", "1 a 11 meses"
    elif 7 <= codigo <= 8:
        return "Primera infancia", "1 a 4 años"
    elif 9 <= codigo <= 10:
        return "Niñez", "5 a 14 años"
    elif codigo == 11:
        return "Adolescencia", "15 a 19 años"
    elif 12 <= codigo <= 13:
        return "Juventud", "20 a 29 años"
    elif 14 <= codigo <= 16:
        return "Adultez temprana", "30 a 44 años"
    elif 17 <= codigo <= 19:
        return "Adultez intermedia", "45 a 59 años"
    elif 20 <= codigo <= 24:
        return "Vejez", "60 a 84 años"
    elif 25 <= codigo <= 28:
        return "Longevidad / Centenarios", "85 a 100+ años"
    else:
        return "Edad desconocida", "Edad Desconocida"