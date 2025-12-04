import pandas as pd

def transform_info(df, columna):
    """
    Imprime estadísticas básicas de una columna de un DataFrame.

    Parámetros:
    
            df: pandas.DataFrame
                Dataframe de pandas.
            columna: str
                Nombre de la columna a analizar.

    Ejemplo:
         cambios(df, "monthlyrate")
         
         """
    
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    print(f"Valores únicos: {valores_unicos}\nNúmero de registros: {num_registros}\nValores nulos: {valores_nulos}\nRegistros duplicados: {duplicados}\ndtype: {dtype}")
    print('----------------')
    print("\nPorcentajes:")
    print(df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2).sort_values(ascending=False))

def to_doc_info(df, columna):

    """
    Genera un reporte formateado con estadísticas de una columna de un DataFrame.

    Parámetros:
            
            df : pandas.DataFrame
                DataFrame de pandas.
            columna : str
                Nombre de la columna a analizar.

    Devuelve:
    ---------
    str
        Reporte formateado con estadísticas y frecuencias.

    Ejemplo:
    --------
    >>> reporte = paradocumentacion(df, "monthlyrate")
    >>> print(reporte)
    """
    
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype
    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2).sort_values(ascending=False)
    tabla_frecuencias = "\n".join([f"{idx}ㅤㅤ{val}" for idx, val in frecuencias.items()])

    reporte = f"""
|    Tipo   |   {columna}   |
|-----------|---------------|
| dtype: {dtype} |{tabla_frecuencias}<br><br>Valores únicos: **{valores_unicos}**<br>Número de registros: **{num_registros}**<br>Valores nulos: **{valores_nulos}**<br>Registros duplicados: **{duplicados}**
"""
    return reporte

def transform_headtail(df, columna):
    """
    Imprime estadísticas básicas y los 5 valores más/menos frecuentes de una columna.

    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame de pandas.
    columna : str
        Nombre de la columna a analizar.
    """
    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    print(f"Valores únicos: {valores_unicos}\nNúmero de registros: {num_registros}\nValores nulos: {valores_nulos}\nRegistros duplicados: {duplicados}\ndtype: {dtype}")
    print('----------------')

    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    print("\nTop 5 porcentajes:")
    print(frecuencias.head(5))
    print("\nBottom 5 porcentajes:")
    print(frecuencias.tail(5))

def to_doc_headtail(df, columna):

    """
    Genera un reporte formateado con estadísticas y los 5 valores más/menos frecuentes de una columna.

    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame de pandas.
    columna : str
        Nombre de la columna a analizar.

    Devuelve:
    ---------
    str
        Reporte formateado con estadísticas y top/bottom 5.
    """

    valores_unicos = df[columna].nunique()
    num_registros = len(df[columna])
    duplicados = num_registros - valores_unicos
    valores_nulos = df[columna].isnull().sum()
    dtype = df[columna].dtype

    frecuencias = df[columna].value_counts(normalize=True, dropna=False).mul(100).round(2)
    top5 = "\n".join([f"{idx}ㅤㅤ{val}%" for idx, val in frecuencias.head(5).items()])
    bottom5 = "\n".join([f"{idx}ㅤㅤ{val}%" for idx, val in frecuencias.tail(5).items()])

    reporte = f"""
|    Tipo {dtype}  |   {columna}   |
|-----------|---------------|
| Top 5: |{top5}
|Bottom 5: |{bottom5}<br><br>Valores únicos: **{valores_unicos}**<br>Número de registros: **{num_registros}**<br>Valores nulos: **{valores_nulos}**<br>Registros duplicados: **{duplicados}**
"""
    return reporte
