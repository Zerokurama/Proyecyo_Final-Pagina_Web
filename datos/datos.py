import pandas as pd
def cargar_datos()->tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Carga los datos de los archivos Excel y devuelve tres DataFrames:
     - df_muertes: Contiene los datos de muertes.
     - df_codigos: Contiene los códigos.
     - df_divipola: Contiene los datos de divipola.
     return:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
    """

    df_muertes = pd.read_excel("datos/Anexo1.NoFetal2019_CE_15-03-23.xlsx")
    df_codigos = pd.read_excel("datos/Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx", header=8)
    df_divipola = pd.read_excel("datos/Divipola_CE_.xlsx")

    return df_muertes, df_codigos, df_divipola