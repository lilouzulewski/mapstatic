#%%
#importing modules
import pandas as pd
import pooch 
import os


url = 'https://odre.opendatasoft.com/explore/dataset/eco2mix-regional-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
path_target = './consumptiondata.csv'

#defining a class to download the data
class datadownloading:
    '''downloading the dataframe'''
    def __init__(selfurl=url, target_name=path_target):
        path, fname = os.path.split(path_target)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)
    '''reading the dataframe'''
    def saving():
        dataframe = pd.read_csv(path_target, usecols=['Date','Heure','Consommation (MW)','Thermique (MW)','Nucléaire (MW)','Eolien (MW)','Solaire (MW)','Hydraulique (MW)'], delimiter=";", converters={'date':str, 'hour':str})
        dataframe.rename(columns = {'Date':'date','Heure':'hour','Consommation (MW)':'consumption','Thermique (MW)':'thermal','Nucléaire (MW)':'nuclear','Eolien (MW)':'wind','Solaire (MW)':'solar','Hydraulique (MW)':'hydraulic'}, inplace=True)
        return(dataframe)

# %%
