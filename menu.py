#!/usr/bin/env python
import time
from data import data
from graphic import graph
from dataframe import generate_dataframe
from scipy.stats import lognorm, dweibull, gamma
import moments as mme
import mle
def afficher_menu():
    print("=== MENU ===")
    print("1. Générer un dataframe des résultats: méthodes des moments (mme)")
    print("2. Afficher les graphiques: qualité de calibration méthodes des moments (mme)")
    print("3. Générer un dataframe des résultats: maximum de vraisemblance (mle)")
    print("4. Afficher les graphiques: qualité de calibration maximum de vraisemblance (mle)")
    print("5. Quitter")
    print()

def executer_option(option):
    # Define the distributions
    distributions = [lognorm, dweibull, gamma]

    #Define label
    data_label = 'data'

    #Label of distristribution
    distribution_list_label = ['lognorm', 'weibull', 'gamma']

    if option == 1:

        # Calculate the moments using the function
        parameters_list = mme.calculate_moments(data, distributions)
        #resuparameters_list2 = mme.calculate_moments(data1, distributions)

        #Generate dataframe
        df = generate_dataframe(data_label, distribution_list_label, parameters_list)
        
        # Save the DataFrame to a CSV file with semicolon as the separator
        #df.to_csv('Méthode-des-moments.csv', index=False, sep=';')

        # Affichage du DataFrame
        print(df)

        time.sleep(5)

    elif option == 2:

        # Calculate the moments using the function
        parameters_list = mme.calculate_moments(data, distributions)

        # Define the distributions and their parameters for the graphics
        distributions = [
            ('Lognormal', 
             lognorm, 
             parameters_list[0]['param1'], 
             parameters_list[0]['loc'], 
             parameters_list[0]['param2'], 
             (1,), 
             'g', 
             'dotted'),

            ('Weibull', 
             dweibull, 
             parameters_list[1]['param1'], 
             parameters_list[1]['loc'], 
             parameters_list[1]['param2'], 
             (3,), 'r', 'dotted'),
            
            ('Gamma', 
             gamma, 
             parameters_list[2]['param1'], 
             parameters_list[2]['loc'], 
             parameters_list[2]['param2'],  
             (3,), 
             'b', 
             'dotted')
        ]

        #Afficher les graphiques avec MME
        graph(
            data=data, 
            distributions=distributions
            )
    elif option == 3:
        # Calculate mle using the function
        parameters_list = mle.calculate_mle(data, distributions)

        df = generate_dataframe(data_label, distribution_list_label, parameters_list)
        
        # Save the DataFrame to a CSV file with semicolon as the separator
        #df.to_csv('Méthode-des-moments.csv', index=False, sep=';')

        # Affichage du DataFrame
        print(df)

        time.sleep(5)

    elif option == 4:
        # Calculate the moments using the function
        parameters_list = mle.calculate_mle(data, distributions)

        # Define the distributions and their parameters
        distributions = [
            ('Lognormal', 
             lognorm, 
             parameters_list[0]['param1'], 
             parameters_list[0]['loc'], 
             parameters_list[0]['param2'], 
             (1,), 
             'g', 
             'dotted'),

            ('Weibull', 
             dweibull, 
             parameters_list[1]['param1'], 
             parameters_list[1]['loc'], 
             parameters_list[1]['param2'], 
             (3,), 'r', 'dotted'),
            
            ('Gamma', 
             gamma, 
             parameters_list[2]['param1'], 
             parameters_list[2]['loc'], 
             parameters_list[2]['param2'],  
             (3,), 
             'b', 
             'dotted')
        ]

        #Afficher les graphiques MLE
        graph(
            data=data, 
            distributions=distributions
            )
    elif option == 5:
        print("Au revoir !")
        exit()
    else:
        print("Option invalide. Veuillez sélectionner une option valide.")


def menu():
    quitter = False

    while not quitter:
        afficher_menu()
        choix = input("Sélectionnez une option : ")

        try:
            option = int(choix)
            executer_option(option)

            if option == 5:
                quitter = True
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")