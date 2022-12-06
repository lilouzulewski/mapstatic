#%%
#importing modules
import pandas as pd
import datadownloading


#creating all the energies's dataframes 
class datashaping:
     '''global consumption'''
     def consumptiondata():
          consumptiondata = datadownloading.datadownloading.saving().copy(deep=True)
          consumptiondata = consumptiondata[['date', 'hour', 'consumption']]
          consumptiondata.set_index('date', inplace=True)
          return(consumptiondata)

     '''thermal'''
     def thermaldata():
          thermaldata = datadownloading.datadownloading.saving().copy(deep=True)
          thermaldata = thermaldata[['date', 'hour', 'thermal']]
          thermaldata.set_index('date', inplace=True)
          return(thermaldata)

     '''nuclear'''
     def nucleardata():
          nucleardata = datadownloading.datadownloading.saving().copy(deep=True)
          nucleardata = nucleardata[['date', 'hour', 'nuclear']]
          nucleardata.set_index('date', inplace=True)
          return(nucleardata)

     '''wind'''  
     def winddata():
          winddata = datadownloading.datadownloading.saving().copy(deep=True)
          winddata = winddata[['date', 'hour', 'wind']]
          winddata.set_index('date', inplace=True)
          return(winddata)

     '''solar'''
     def solardata():
          solardata = datadownloading.datadownloading.saving().copy(deep=True) 
          solardata = solardata[['date', 'hour', 'solar']]
          solardata.set_index('date', inplace=True)
          return(solardata)

     '''hydraulic'''
     def hydraulicdata():  
          hydraulicdata = datadownloading.datadownloading.saving().copy(deep=True)
          hydraulicdata = hydraulicdata[['date', 'hour', 'hydraulic']]
          hydraulicdata.set_index('date', inplace=True)
          return(hydraulicdata)


#visualizing all the newly created energies's dataframes
datashaping.consumptiondata().plot(figsize=(20, 5), title="French Global Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
datashaping.thermaldata().plot(figsize=(20, 5), title="French Thermal Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
datashaping.nucleardata().plot(figsize=(20, 5), title="French Nuclear Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
datashaping.winddata().plot(figsize=(20, 5), title="French Wind Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
datashaping.solardata().plot(figsize=(20, 5), title="French Solar Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
datashaping.hydraulicdata().plot(figsize=(20, 5), title="French Hydraulic Energy Consumption Since 2013", xlabel='Date', ylabel='MW')



# %%
