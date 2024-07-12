#!/usr/bin/env python
import numpy as np
#from scipy.stats import lognorm, dweibull, gamma
import matplotlib.pyplot as plt
import statsmodels.api as sm

""" Generate graphic for Q-Q plot, P-P plot, CDFs and PDF"""
def graph(data, distributions):
    data = np.array(data)

    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 5))
    
    # Distribution fitted to the data
    x = np.linspace(0, np.max(data), 100)

    #Boucle « for » ainsi, on peut rajouter des lois de distributions supplémentaires, sans que le code ne change.
    for dist_name, dist, shape, loc, scale, distargs, marker_color, linestyle in distributions:
        """ Generate Q-Q plot graphic"""
        sm.qqplot(
            data, 
            dist=dist, 
            scale=scale, 
            loc=loc, 
            distargs=distargs, 
            fit=True, 
            line='45',
            ax=ax1, 
            label=dist_name, 
            marker='.', 
            markerfacecolor=marker_color, 
            markeredgecolor=marker_color)
        
        """ Generate P-P plot """
        sm.ProbPlot(
            data, 
            dist=dist, 
            scale=scale, 
            loc=loc, 
            distargs=(1,), 
            fit=True).ppplot(line='45', label=dist_name, marker='.', markerfacecolor=marker_color, markeredgecolor=marker_color, ax=ax2)
        
        """ Creating Cumulative Distribution Function (CDF) Histogram """
        cdf_theoretical = dist.cdf(x, shape, loc=loc, scale=scale)
        #Creating the theoretical density histogram
        #Plotting the CDFs of the theoretical and empirical densities
        ax3.plot(x, cdf_theoretical, label=dist_name, color=marker_color, linestyle=linestyle)

        """ Generate PDF plot for lognormal, gamma and dweibull """
        pdf = dist.pdf(x, shape, loc=loc, scale=scale)
        #Creating the theoretical density histogram
        ax4.plot(x, pdf, label=dist_name, color=marker_color, linestyle=linestyle)
    
    ax1.set_title('Q-Q plot')
    ax2.set_title('P-P plot')

    # CDF des densités théoriques
    ax3.set_xlabel('Data')
    ax3.set_ylabel('CDF')
    ax3.set_title('Empirical and theoritical CDFs')

    #Creating the theoretical density histogram
    ax4.hist(data, bins='auto', density=True, color='skyblue', alpha=0.7, edgecolor='black', label='Données observées')

    #Adding the labels
    ax4.set_xlabel('Data')
    ax4.set_ylabel('Densité')
    ax4.set_title('Histogramme et théorique des densités')

    """ Adjust spacing between subplots """
    plt.subplots_adjust(wspace=0.4)

    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    plt.show()