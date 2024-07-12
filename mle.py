#!/usr/bin/env python
def calculate_mle(data, distributions):
    results = []

    # Significations des paramètres : 
    # parametre1 : Le paramètre de forme(shape) de la distribution. 
    # parametre2 : Le paramètre d'échelle(scale) de la distribution. 

    #Boucle « for » ainsi, on peut rajouter des lois de distributions supplémentaires, sans que le code ne change.
    for distribution in distributions:
        shape, loc, scale = distribution.fit(data, loc=0, method="MLE")
        results.append({'param1': shape, 'loc': loc, 'param2': scale})

    return results