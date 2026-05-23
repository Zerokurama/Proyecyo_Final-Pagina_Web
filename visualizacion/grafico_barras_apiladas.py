import pandas as pd
import plotly.express as px

def crear_grafico_barras_apiladas(df_analisis_muertes: pd.DataFrame)->px.bar:
    """
    Crea un gráfico de barras apiladas de muertes por sexo utilizando Plotly Express.
    Args:
        df_analisis_muertes (pd.DataFrame): DataFrame con los datos de muertes.
    Returns:
        px.bar: Gráfico de barras apiladas de muertes por sexo.
    """

    # Mapear los valores de sexo a etiquetas legibles
    digcionario_sexo = {1: "Masculino", 2: "Femenino", 3: "Indeterminado"}
    df_analisis_muertes["sexo_texto"] = df_analisis_muertes["SEXO"].map(digcionario_sexo).astype(str)
    df_analisis_muertes["sexo_texto"] = df_analisis_muertes["sexo_texto"].fillna("Indeterminado")
    df_muertes_sexo_departamento = df_analisis_muertes.groupby(["DEPARTAMENTO", "sexo_texto"]).size().reset_index(name="conteo")

    # Crear el gráfico de barras apiladas de muertes por departamento utilizando Plotly Express
    bar_apilado = px.bar(
        df_muertes_sexo_departamento,
        x="DEPARTAMENTO",
        y="conteo",
        color="sexo_texto",
        color_discrete_map={
            "Masculino": "#056ef7", 
            "Femenino": "#9905fc", 
            "Indeterminado": "#fd1201"
        },
        title="Muertes por Sexo y Departamento",
        labels={"DEPARTAMENTO": "Departamento", "conteo": "Número de Muertes", "sexo_texto": "Sexo"}
    )

    # Personaliza el diseño del gráfico
    bar_apilado.update_layout(
        plot_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="#eeeeee"),
        yaxis=dict(showgrid=True, gridcolor="#eeeeee")
    )
    bar_apilado.update_traces(
        hovertemplate= "<b> %{fullData.name}</b> <br> " + "Departamento: %{x}<br> " + "Casos: %{y:,.0f} <extra></extra>"
    )

    return bar_apilado