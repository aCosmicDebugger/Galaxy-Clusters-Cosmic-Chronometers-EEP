import numpy as np
import pandas as pd
import math
import scipy.integrate as si 
import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
from HzGPR import H_GPR
from HzFid import H_th

# Esse é um módulo Python feito por mim @aCosmicDebbuger
# https://github.com/aCosmicDebugger
# Esse é um módulo para obter-se distâncias como função do
# redshift e da curvatura usando o resultado de um GPR, 
# ou como função do redshift e da curvatura usando o modelo 
# Lambda-CDM.


# Parâmetros do modelo cosmológico em questão. 
param_cosmo_fid = [0.2657, 0.0493, 0, 0.7049, -1]

def DC_Fid(param_cosmo, z):
    '''
    DC_Fid calcula a distância comóvel usando o cálculo teórico de H(z)
    '''
    
    omega_c, omega_b, omega_k, h, w_x = param_cosmo
    
    # Velocidade da luz em [km/s]
    vel_c = 299792.4580 
    
    integrando = lambda z_star: vel_c/H_th(z_star, [0.2657, 0.00493, 0, 0.704, -1])
    
    resultado = []
    erro = []
    for n in z:
        resultado.append(si.quad(integrando,0,n)[0])
        erro.append(si.quad(integrando,0,n)[1])
    
    r = np.array(resultado)
    err = np.array(erro)
    return r , err


def DC_CC(z):
    '''
    DC_CC calcula a distância comóvel usando a estimação pra H(z) 
    via processo Gaussiano de regressão (GPR)
    '''
    # Velocidade da luz em [km/s]
    vel_c = 299792.4580 
    
    integrando = lambda z_star: vel_c/H_GPR(z_star)
    
    resultado = []
    erro = []
    for n in z:
        resultado.append(si.quad(integrando,0,n)[0])
        erro.append(si.quad(integrando,0,n)[1])
    
    r = np.array(resultado)
    err = np.array(erro)
    return r , err

def DA_Fid(omega_k, z):
    '''
    DA_Fid calcula a distância de diâmetro angular usando o valor teórico calculado
    para o H(z) usando o modelo fiducial.
    '''
    
    param_cosmo = [0.2657, 0.00493, 0, 0.794, -1]
    
    H_0 = H_th(z, param_cosmo)
    DC = DC_Fid(param_cosmo, z)
    
    # Velocidade da luz em [km/s]
    vel_c = 299792.4580
    
    if omega_k < 0:
        
        DA = ( 1.0 / (1.0+z) )*( vel_c /( H_0*np.sqrt(np.abs(omega_k) ) ) )\
                *np.sin( ( H_0*np.sqrt( np.abs(omega_k) )/ vel_c )*DC[0] )
        
        return DA, DC[1]
    elif omega_k > 0:
        
        DA = ( 1.0/ (1.0+z) )*( vel_c /( H_0*np.sqrt(np.abs(omega_k ) ) ) )\
                *np.sinh( ( H_0*np.sqrt( np.abs(omega_k ) )/ vel_c )*DC[0] )
        
        return DA, DC[1]
    else:
        
        DA = (1.0 / (1.0+z) )*DC[0]
        
        return DA, DC[1]



def DA_GPR(omega_k, z):
    '''
    DA_obs calcula a distância de diâmetro angular levando em conta os dados de H(z)
    obtidos através do GPR, para cenários com ou sem curvatura.
    '''
    
    H_0 = H_GPR([0])
    DC = DC_CC(z)
    
    # Velocidade da luz em [km/s]
    vel_c = 299792.4580
    
    if omega_k < 0:
        
        DA = ( 1.0 / (1.0+z) )*( vel_c /( H_0*np.sqrt(np.abs(omega_k) ) ) )\
                *np.sin( ( H_0*np.sqrt( np.abs(omega_k) )/ vel_c )*DC[0] )
        
        return DA, DC[1]
    elif omega_k > 0:
        
        DA = ( 1.0/ (1.0+z) )*( vel_c /( H_0*np.sqrt(np.abs(omega_k ) ) ) )\
                *np.sinh( ( H_0*np.sqrt( np.abs(omega_k ) )/ vel_c )*DC[0] )
        
        return DA, DC[1]
    else:
        
        DA = (1.0 / (1.0+z) )*DC[0]
        
        return DA, DC[1]


if __name__ == '__main__':
	
	input(print('Forneça uma lista de redshifts'))
	z = input
	DA_GPR(0,z)









