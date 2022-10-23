
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 3. Finanzas Conductuales                                                       -- #
# -- script: visualizations.py : script de python con las funciones para la visualización de datos       -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# Configuraciones
import plotly.graph_objects as go
import main 

labels = dic_estadisticas_ba_emilio["df_2_ranking"]['r_efectividad'][0:3].index
values = dic_estadisticas_ba_emilio["df_2_ranking"]['r_efectividad'][0:3].values
fig_emilio = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[.05, 0, 0], )])
fig_emilio.update_layout(title_text='Ricardo')


labels = dic_estadisticas_ba_ricardo["df_2_ranking"]['r_efectividad'][0:3].index
values = dic_estadisticas_ba_ricardo["df_2_ranking"]['r_efectividad'][0:3].values
fig_ricardo = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[.05, 0, 0], )])
fig_ricardo.update_layout(title_text='Ricardo')

labels = dic_estadisticas_ba_leonardo["df_2_ranking"]['r_efectividad'][0:3].index
values = dic_estadisticas_ba_leonardo["df_2_ranking"]['r_efectividad'][0:3].values
fig_leonardo = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[.05, 0, 0], )])
fig_leonardo.update_layout(title_text='Ricardo')
