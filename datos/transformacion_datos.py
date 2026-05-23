import pandas as pd

def transformar_datos(df_muertes: pd.DataFrame, df_codigos: pd.DataFrame, df_divipola: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma los datos de muertes, códigos y divipola para su análisis.
    Realiza las siguientes operaciones:
        1. Selecciona las columnas relevantes de cada DataFrame.
        2. Limpia y homologa las llaves de unión (COD_DANE y COD_MUERTE).
        3. Integra los DataFrames mediante .merge() para obtener un DataFrame final listo para análisis.
    Args:
        df_muertes (pd.DataFrame): DataFrame con los datos de muertes.
        df_codigos (pd.DataFrame): DataFrame con los códigos de enfermedades (CIE-10).
        df_divipola (pd.DataFrame): DataFrame con los datos geográficos (Divipola).
    Returns:
        pd.DataFrame: DataFrame integrado listo para análisis.
    """
    # Se selecciona las columnas relevantes de los dataframes para el análisis
    df_muertes_reducido = df_muertes[[
        'COD_DANE',
        'MES',
        'SEXO',
        'GRUPO_EDAD1',
        'MANERA_MUERTE',
        'COD_MUERTE'
    ]]
    df_divipola_reducido = df_divipola[[
        'COD_DANE',
        'COD_DEPARTAMENTO',
        'DEPARTAMENTO',
        'COD_MUNICIPIO',
        'MUNICIPIO'
        ]]
    df_codigos_reducido = df_codigos[[
        'Código de la CIE-10 cuatro caracteres',
        'Código de la CIE-10 tres caracteres',
    ]]

    # Se convierte COD_DANE a string y se eliminan los espacios en blanco
    df_muertes_reducido['COD_DANE'] = df_muertes_reducido['COD_DANE'].astype(str).str.strip()
    df_divipola_reducido['COD_DANE'] = df_divipola_reducido['COD_DANE'].astype(str).str.strip()

    # Se convierte COD_MUERTE y ódigo de la CIE-10 cuatro caracteres a string 
    # Se eliminan los espacios en blanco y  se converten a mayúsculas
    df_muertes_reducido['COD_MUERTE'] = df_muertes_reducido['COD_MUERTE'].astype(str).str.strip().str.upper()
    df_codigos_reducido['Código de la CIE-10 tres caracteres'] = df_codigos_reducido['Código de la CIE-10 tres caracteres'].astype(str).str.strip().str.upper()

    # Se realiza la unión entre df_muertes_reducido y df_divipola_reducido con el campo COD_DANE
    df_departamento_municipio = pd.merge(df_muertes_reducido, df_divipola_reducido, on='COD_DANE', how='left')

    # Se realiza la unión entre df_departamento_municipio y df_codigos_reducido con el campo COD_MUERTE y Código de la CIE-10 cuatro caracteres
    df_analisis_muertes = pd.merge(df_departamento_municipio, df_codigos_reducido, left_on='COD_MUERTE', right_on='Código de la CIE-10 cuatro caracteres', how='left')

    # Elimina la columna Código de la CIE-10 cuatro caracteres por los datos duplicados con COD_MUERTE
    df_analisis_muertes = df_analisis_muertes.drop(columns=['Código de la CIE-10 cuatro caracteres'])

    return df_analisis_muertes