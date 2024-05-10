import pandas as pd
import os 
def exportar_excel(data,archivo_de_salida="C:/Users/franc/OneDrive/Documentos/readerpy/archivo.xlsx"):
    
    df = pd.DataFrame(data)
    columnas_con_datos = df.columns[df.iloc[1:].notna().any()]
    df_filtrado = df[columnas_con_datos]
    df_filtrado.to_excel(archivo_de_salida,index=False)
    try:
        os.startfile(archivo_de_salida)
    except:
        pass
    
def exportar_excel_simple(data,archivo_de_salida="C:/Users/franc/OneDrive/Documentos/readerpy/archivo.xlsx"):
    
    df = pd.DataFrame(data)
    df.to_excel(archivo_de_salida,index=False)
    try:
        os.startfile(archivo_de_salida)
    except:
        pass