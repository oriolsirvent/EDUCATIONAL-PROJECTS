from typing import Self
import requests
from datetime import datetime
import matplotlib.pyplot as plt

def extract(): 
    database = requests.get(url='https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search?resource_id=77c47da6-9e4f-46de-8c37-d0bff307a725&limit=150')
    database=database.json()
    return (database)

def transform (extracted_data):
    database = extracted_data
    database_inspection_level_1=database['result']
    total_entries = database_inspection_level_1['limit']-1
    keys_to_run = database_inspection_level_1['records'][0].keys()

    dictionary_info_classified = dict()
    iteration_dict = dict()
    order_dict = list()
    order_dict_values = list()

    for database_inspection_level_2 in keys_to_run:
        puntual_key = database_inspection_level_2
        iteration_dict = {}
        order_dict = []
        order_dict_values = []

        for entry_analisis in range(total_entries):
            database_info_to_load = database_inspection_level_1['records'][entry_analisis]
            puntual_value = str(database_info_to_load[database_inspection_level_2])
            if puntual_value == '':
                puntual_value = 'No especificado'

            if puntual_value in iteration_dict:
                iteration_dict [puntual_value] = iteration_dict [puntual_value]+1
            else: 
                iteration_dict [puntual_value]= 1
        
        for key in iteration_dict:
            order_dict.append (key)
            order_dict_values.append (iteration_dict[key])

        dictionary_info_classified [database_inspection_level_2 + " [Claves]"] = order_dict
        dictionary_info_classified [database_inspection_level_2 + " [Valores]"] = order_dict_values    

    return (dictionary_info_classified)


                         
                    
def load(extracted_data_dict):

    print("Esta es otra función")
    plt.figure(1)
    plt.bar(extracted_data_dict['partit_politic [Claves]'], extracted_data_dict['partit_politic [Valores]'], color='blue')

    #Añadir etiquetas y título
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.xlabel('MILITANTES POR PARTIDO')
    plt.ylabel('NÚMERO DE MILITANTES')
    plt.title('PARTIDO POLÍTICO')


    plt.figure(2)
    plt.bar(extracted_data_dict['descripcio_carrec_es [Claves]'], extracted_data_dict['descripcio_carrec_es [Valores]'], color='blue')

    # Añadir etiquetas y título
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.xlabel('CARGOS')
    plt.ylabel('NÚMERO DE INDIVIDUOS')
    plt.title('CARGO POLÍTICO')

    plt.figure(3)
    plt.bar(extracted_data_dict['remuneracio [Claves]'], extracted_data_dict['remuneracio [Valores]'], color='blue')

    # Añadir etiquetas y título
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.xlabel('SALARIOS')
    plt.ylabel('NÚMERO DE INDIVIDUOS')
    plt.title('REMUNERACIÓN')

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    
    extracted_data=extract()
    
    transformed_data=transform (extracted_data)

    loaded_data = load(transformed_data)
    