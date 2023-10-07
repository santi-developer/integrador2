from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from graficas import obtener_Dataframe
    

def grafica_tortas(df:pd.DataFrame): 
        
 mujeres = df[df['sex']==False]
 hombres = df[df['sex'] == True]
        
 cantidad_anemic_mujeres = mujeres['anaemia'].sum()
 cantidad_anemic_hombres = hombres['anaemia'].sum()
      
 # creacion del primer grafico de torta        
 categorias=['Hombres','Mujeres']
 valores=[cantidad_anemic_hombres,cantidad_anemic_mujeres]
        
 plt.subplot(2,2,1)       
 plt.pie(valores,labels=categorias,autopct='%1.1f%%', startangle=90)
 plt.title('cantidad de anemicos') 
 
 # creacion de la segunda grafico de torta
 cantidad_diabetes_mujeres = mujeres['diabetes'].sum()
 cantidad_diabetes_hombres = hombres['diabetes'].sum()
 
 categorias=['Hombres','Mujeres']
 valores=[cantidad_diabetes_hombres,cantidad_diabetes_mujeres]
        
 plt.subplot(2,2,2)       
 plt.pie(valores,labels=categorias,autopct='%1.1f%%', startangle=90)
 plt.title('cantidad de diabeticos') 
 
 # creacion del tercer grafico de torta
 cantidad_fumadores_mujeres = mujeres['smoking'].sum()
 cantidad_fumadores_hombres = hombres['smoking'].sum()
 
 categorias=['Hombres','Mujeres']
 valores=[cantidad_fumadores_hombres,cantidad_fumadores_mujeres]
        
 plt.subplot(2,2,3)       
 plt.pie(valores,labels=categorias,autopct='%1.1f%%', startangle=90)
 plt.title('cantidad de fumadores') 
 
 # creacion del tercer grafico de torta
 cantidad_muertos_mujeres = mujeres['DEATH_EVENT'].sum()
 cantidad_muertos_hombres = hombres['DEATH_EVENT'].sum()
 
 categorias=['Hombres','Mujeres']
 valores=[cantidad_muertos_hombres,cantidad_muertos_mujeres]
        
 plt.subplot(2,2,4)       
 plt.pie(valores,labels=categorias,autopct='%1.1f%%', startangle=90)
 plt.title('cantidad de decesos') 
 
 
 plt.tight_layout()      
 plt.show()
 
def main():
   df=obtener_Dataframe()
   grafica_tortas(df)
    
if __name__ == "__main__":
    main()
        