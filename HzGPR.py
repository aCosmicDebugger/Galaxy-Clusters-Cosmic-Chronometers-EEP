import sys, os
# sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF
from sklearn.gaussian_process.kernels import DotProduct as DotP
from sklearn.model_selection import RandomizedSearchCV


# Esse é um módulo Python feito por mim @aCosmicDebbuger
# https://github.com/aCosmicDebugger
# HzGPR recebe uma lista de redshifts ou um int apenas 
# e usando 31 observações de Cronômetros Cósmicos 
# que podem ser vistas em: https://arxiv.org/pdf/1911.12076.pdf (Tabela A2),
# retorna a estimação para medidas de H(z) através de
# Gaussian Process Regression (GPR).


# importando o dataset
H_z = pd.read_csv('CosmicChronometersData.csv')

# printando o dataset
#print(H_z)

# Transformando o dataframe em array(s)
H_z_array = np.array(H_z)

redshift = H_z_array[0:31,0]
h = H_z_array[0:31,1]
erro = H_z_array[0:31,2]

# dimensão dos arrays
d = 1
n = 31

# As variáveis para o processo Gaussiano
z = np.linspace(redshift.min(),redshift.max(),1000)
X = redshift.reshape(n,d)
Y = h

X_star = z.reshape(z.shape[0],d)


# random-search
def random_search(X, y, n):
    best_score = -np.inf
    best_params = None

    for _ in range(n):
        # Geração aleatória dos parâmetros
        s1 = np.random.uniform(0.1, 500)
        constant_value_1= np.random.uniform(0.001,500)
        l = np.random.uniform(0.001, 500)

        # Criação do modelo de regressão gaussiana
        kernel = DotP( s1)+ConstantKernel(constant_value=constant_value_1)*RBF(length_scale=l)
        model = GaussianProcessRegressor(kernel=kernel, alpha=10)

        # Ajuste do modelo aos dados
        model.fit(X, y)

        # Avaliação da pontuação (score) do modelo
        score = model.score(X, y)

        # Atualização do melhor score e melhores parâmetros
        if score > best_score:
            best_score = score
            best_params = {'s1': s1, 'C1':constant_value_1, 'l':l}
                          
                           
    return best_params, best_score
    
# Número de iterações da busca aleatória
n_int = 1500

best_params, best_score = random_search(X, Y, n_int)

s1 = best_params['s1']
constant1=best_params['C1']
l = best_params['l']

# definindo o Kernel para p/ o processo gaussiano
GPR_Kernel =DotP(s1)+ConstantKernel(constant1)*RBF(l )

# processo
GPR = GaussianProcessRegressor(kernel=GPR_Kernel, alpha=160)    # próximo GPR dar uma olhada na mudança 150-160 em alpha

# fit
GPR.fit(X, Y)

# predição:
Y_pred = GPR.predict(X_star)


def H_GPR(z):
    '''
    H_GPR vai receber um inteiro/float ou uma lista com valor(es) de redshift
    e retornar o valor estimado de H(z) usando Gaussian Process Regression
    '''
    
    if type(z) == int or type(z) == float:
        p = [z]
        p = np.array(p)
        p = p.reshape(p.shape[0],1)
        h = GPR.predict(p)
        h.reshape(1)
    else:
        z = np.array(z)
        z = z.reshape(z.shape[0],1)
        h = GPR.predict(z)
        #h.reshape(1)
    
    h = np.round(h,2)
    
    return h



if __name__ == '__main__':

	print("Melhores valores para os hiperparâmetros do GPR:")
	print(best_params)
	H_GPR(0)
	print("Melhor valor para a constante de Hubble usando GPR:", H0)

	# Plot da predição:
	fig, ax = plt.subplots(figsize=(10,6))
	plt.errorbar(redshift, h, yerr=erro, color='black', label = 'Dados de H(z)', fmt="o")
	sns.lineplot(x=z, y=Y_pred, color='blue', label='GP Best Fit', ax=ax)
	ax.set(title=f'Predição GaussianProcessRegressor, C1 = {round(constant1,3)} and l = {round(l,3) }')
	ax.legend(loc='upper left')
	plt.xlim([redshift.min()-0.03,redshift.max()+0.03])
	plt.show()




