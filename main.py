
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 3. Finanzas Conductuales                                                       -- #
# -- script: main.py : script de python con la funcionalidad main                                        -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# Configuraciones
import data, functions

def estadistica_descriptiva(nombre : "Nombre del Trader"):
    """
    estadistica_descriptiva elabora la primera parte del laboratorio.
    
    """
    
    datos = data.f_leer_archivo("bitacora_operaciones", nombre)
    datos = functions.f_columnas_tiempos(datos)
    datos = functions.f_columnas_pips(datos)
    
    dic_estadisticas_ba = functions.f_estadisticas_ba(datos)

    return datos, dic_estadisticas_ba

def metricas_atribucion_desempeño(historicoOperaciones):
    """
    metricas_atribucion_desempeño elabora la segunda parte del laboratorio.
    
    """
    
    evolucionCapital = functions.f_evolucion_capital(historicoOperaciones)
    mad = functions.f_estadisticas_mad(evolucionCapital)

    return evolucionCapital, mad

def finanzas_conductuales(historicoOperaciones, evolucionCapital):
    """
    finanzas_conductuales elabora la tercera parte del laboratorio.
    
    """
    
    return  functions.f_be_de(historicoOperaciones, evolucionCapital)
