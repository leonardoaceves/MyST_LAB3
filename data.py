
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 3. Finanzas Conductuales                                                       -- #
# -- script: data.py : script de python para la recolección de datos                                     -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# Configuraciones
import pandas as pd

def f_leer_archivo(param_archivo, nombre_hoja):
    """
    f_leer_archivo lee el histórico de operaciones de MetaTrader.
    
    """
    
    param_data = pd.read_excel("files/" + param_archivo + ".xlsx", sheet_name = nombre_hoja)
    param_data.columns = ["opentime", "ticket", "item", "type", "size", "openprice", "S/L", "T/P", "closetime", "closeprice",
                     "comission", "swap", "profit"]
    
    return param_data
