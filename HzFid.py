import sys, os
# sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns


# Esse é um módulo Python feito por mim @aCosmicDebbuger
# https://github.com/aCosmicDebugger
# HzFid recebe uma lista de parâmetros cosmológicos e 
# o redshift (lista ou int)
# retorna o resultado do cálculo teórico de H(z).
# por padrão retorna o resultado do cálculo para o
# modelo fiducial, o Lambda-CDM.


fiducial =[ 0.2657, 0.0493, 0, 0.704, -1] 


def H_th(z, param_cosmo=[fiducial]):	
    '''
    H_th recebe os parâmetros de densidade,  o h e o valor para equação de estado da energia escura então retorna o H(z) teórico.
    
    '''
    
    omega_c, omega_b, omega_k, h, w_x = param_cosmo
    
    # Outras variáveis necessárias.
    # Temperatura da CMB em [K], erro de ± 0.002 ver Fixsen 2009 DOI:10.1088/0004-637X/707/2/916
    T_0_cmb = 2.725
    
    # Parâmetro de densidade da radiação eletromagnética x h2 ver eq. 8 https://arxiv.org/abs/1411.1074 
    Omega_EMh2 = (4.482*10**(-7.0))*T_0_cmb**4.0 
    
    # Número efetivo de neutrinos
    Neff = 3.046
    
    # Parâmetro de densidade total da radiação (E.M. + Neutrinos) x h2
    Omega_rh2 = Omega_EMh2*(1.0+0.2271*Neff)
    
    omega_m = omega_c + omega_b
    Omega_tot = omega_m + omega_k + (Omega_rh2)/(h**2.0)
    Ez = (omega_m*(1+z)**3.0 +omega_k*(1+z)**2.0 +(Omega_rh2/h**2)*(1+z)**4.0\
          +(1.0-Omega_tot)*(1+z)**(3+3*w_x))**(1/2)
    
    return 100.0*h*Ez

    
if __name__ == '__main__':
    H0_fid = H_th(0,fiducial)
    print("O valor de H0 no modelo fiducial: ", H0_fid)  
 	
 	
