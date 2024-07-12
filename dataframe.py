#!/usr/bin/env python
import pandas as pd
    
# Création du DataFrame
#Boucle « for » ainsi, on peut rajouter des lois de distributions supplémentaires, sans que le code ne change.
def generate_dataframe(data, distribution_list, parameters_list):
    df_data = []
    for distribution, parameters in zip(distribution_list, parameters_list):
            row = {'data': data, 'distribution': distribution}
            row.update(parameters)
            df_data.append(row)
        
    df = pd.DataFrame(df_data)
    return df