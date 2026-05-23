import pandas as pd

def crear_tabla(df_analisis_muertes: pd.DataFrame)-> pd.DataFrame:
    """
    Crea una tabla con los datos de muertes por municipio.
    Args:
        df_analisis_muertes (pd.DataFrame): DataFrame con los datos de muertes.
    Returns:
        pd.DataFrame: Tabla con los datos de muertes por municipio.
    """
    # Agrupar los datos por municipio y contar las muertes
    df_tabla = df_analisis_muertes.groupby(['Código de la CIE-10 tres caracteres', 'COD_MUERTE', 'MANERA_MUERTE']).size().reset_index(name='CASOS')
    
    # Ordenar la tabla por la cantidad de muertes y seleccionar las 10 ciudades con más muertes
    df_tabla_top10 = df_tabla.sort_values(by='CASOS', ascending=False).head(10)
    
    return df_tabla_top10