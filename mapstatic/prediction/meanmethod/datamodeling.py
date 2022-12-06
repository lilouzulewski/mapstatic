#importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import datashaping

#making the prediction
class prediction:
    #defining all the variables
    def __init__(self, data, energy, mean):
        '''Here, one can choose an energy among global, thermal, nuclear, wind, solar or hydraulic.'''
        self.data = data
        self.mean = mean
        self.energy = energy
    #defining a function for the prediction in itself
    def dataset():
        energy = input('Which energy consumption would you like to predict ?')
        if energy == 'global':
            data = datashaping.datashaping.consumptiondata()
            data = data.loc[['2013-12-01', '2013-12-02', '2013-12-03', '2013-12-04', '2013-12-05', '2013-12-06', '2013-12-07', '2013-12-08',
                                '2014-12-01', '2014-12-02', '2014-12-03', '2014-12-04', '2014-12-05', '2014-12-06', '2014-12-07', '2014-12-08',
                                '2015-12-01', '2015-12-02', '2015-12-03', '2015-12-04', '2015-12-05', '2015-12-06', '2015-12-07', '2015-12-08',
                                '2016-12-01', '2016-12-02', '2016-12-03', '2016-12-04', '2016-12-05', '2016-12-06', '2016-12-07', '2016-12-08',
                                '2017-12-01', '2017-12-02', '2017-12-03', '2017-12-04', '2017-12-05', '2017-12-06', '2017-12-07', '2017-12-08',
                                '2018-12-01', '2018-12-02', '2018-12-03', '2018-12-04', '2018-12-05', '2018-12-06', '2018-12-07', '2018-12-08',
                                '2019-12-01', '2019-12-02', '2019-12-03', '2019-12-04', '2019-12-05', '2019-12-06', '2019-12-07', '2019-12-08',
                                '2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', '2020-12-07', '2020-12-08',
                                '2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06', '2021-12-07', '2021-12-08']]
            for nan in range(len(data)-1):
                if data[['consumption']].isna().iloc[:, 0][nan]:
                    data['consumption'][nan] = (data['consumption'][nan-1] + data['consumption'][nan+1])/2
                    data['consumption'][len(data)-1] = (data['consumption'][len(data)-2]+data['consumption'][len(data)-3])/2
            data.dropna(inplace = True)
            data.index = pd.to_datetime(data.index)
            data.set_index('hour', inplace=True)
            data = data.sort_values(by='hour', ascending=True)
            mean = data.groupby(['hour'])['consumption'].mean()
            plt.figure()
            mean.plot(color='blue')
            plt.title('Global Energy Consumption Prediction for the 8th of December 2022')
            plt.xlabel('Time')
            plt.ylabel('MW')
            plt.savefig('Global_Energy_Consumption', format = 'pdf')
            globalconsumption = mean.to_frame()
            print(globalconsumption)
            return(data, mean)
        elif energy == 'thermal':
            data = datashaping.datashaping.thermaldata()
            data = data.loc[['2016-12-01', '2016-12-02', '2016-12-03', '2016-12-04', '2016-12-05', '2016-12-06', '2016-12-07', '2016-12-08',
                                '2017-12-01', '2017-12-02', '2017-12-03', '2017-12-04', '2017-12-05', '2017-12-06', '2017-12-07', '2017-12-08',
                                '2018-12-01', '2018-12-02', '2018-12-03', '2018-12-04', '2018-12-05', '2018-12-06', '2018-12-07', '2018-12-08',
                                '2019-12-01', '2019-12-02', '2019-12-03', '2019-12-04', '2019-12-05', '2019-12-06', '2019-12-07', '2019-12-08',
                                '2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', '2020-12-07', '2020-12-08',
                                '2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06', '2021-12-07', '2021-12-08']]
            for nan in range(len(data)-1):
                if data[['thermal']].isna().iloc[:, 0][nan]:
                    data['thermal'][nan] = (data['thermal'][nan-1] + data['thermal'][nan+1])/2
                    data['thermal'][len(data)-1] = (data['thermal'][len(data)-2]+data['thermal'][len(data)-3])/2
            data.index = pd.to_datetime(data.index)
            data.set_index('hour', inplace=True)
            data = data.sort_values(by='hour', ascending=True)
            mean = data.groupby(['hour'])['thermal'].mean()
            plt.figure()
            mean.plot(color='blue')
            plt.title('Thermal Energy Consumption Prediction for the 8th of December 2022')
            plt.xlabel('Time')
            plt.ylabel('MW')
            plt.savefig('Thermal_Energy_Consumption', format = 'pdf')
            thermalconsumption = mean.to_frame()
            print(thermalconsumption)
            return(data, mean)
        elif energy == 'nuclear':
            data = datashaping.datashaping.nucleardata()
            data = data.loc[['2016-12-01', '2016-12-02', '2016-12-03', '2016-12-04', '2016-12-05', '2016-12-06', '2016-12-07', '2016-12-08',
                                '2017-12-01', '2017-12-02', '2017-12-03', '2017-12-04', '2017-12-05', '2017-12-06', '2017-12-07', '2017-12-08',
                                '2018-12-01', '2018-12-02', '2018-12-03', '2018-12-04', '2018-12-05', '2018-12-06', '2018-12-07', '2018-12-08',
                                '2019-12-01', '2019-12-02', '2019-12-03', '2019-12-04', '2019-12-05', '2019-12-06', '2019-12-07', '2019-12-08',
                                '2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', '2020-12-07', '2020-12-08',
                                '2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06', '2021-12-07', '2021-12-08']]
            for nan in range(len(data)-1):
                if data[['nuclear']].isna().iloc[:, 0][nan]:
                    data['nuclear'][nan] = (data['nuclear'][nan-1] + data['nuclear'][nan+1])/2
                    data['nuclear'][len(data)-1] = (data['nuclear'][len(data)-2]+data['nuclear'][len(data)-3])/2
            data.index = pd.to_datetime(data.index)
            data.set_index('hour', inplace=True)
            data = data.sort_values(by='hour', ascending=True)
            mean = data.groupby(['hour'])['nuclear'].mean()
            plt.figure()
            mean.plot(color='blue')
            plt.title('Nuclear Energy Consumption Prediction for the 8th of December 2022')
            plt.xlabel('Time')
            plt.ylabel('MW')
            plt.savefig('Nuclear_Energy_Consumption', format = 'pdf')
            nuclearconsumption = mean.to_frame()
            print(nuclearconsumption)
            return(data, mean)
        elif energy == 'wind':
            data = datashaping.datashaping.winddata()
            data = data.loc[['2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', '2020-12-07', '2020-12-08',
                                '2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06', '2021-12-07', '2021-12-08']]
            for nan in range(len(data)-1):
                if data[['wind']].isna().iloc[:, 0][nan]:
                    data['wind'][nan] = (data['wind'][nan-1] + data['wind'][nan+1])/2
                    data['wind'][len(data)-1] = (data['wind'][len(data)-2]+data['wind'][len(data)-3])/2
            data.index = pd.to_datetime(data.index)
            data.set_index('hour', inplace=True)
            data = data.sort_values(by='hour', ascending=True)
            mean = data.groupby(['hour'])['wind'].mean()
            plt.figure()
            mean.plot(color='blue')
            plt.title('Wind Energy Consumption Prediction for the 8th of December 2022')
            plt.xlabel('Time')
            plt.ylabel('MW')
            plt.savefig('Wind_Energy_Consumption', format = 'pdf')
            windconsumption = mean.to_frame()
            print(windconsumption)
            return(data, mean)
        elif energy == 'solar':
            data = datashaping.datashaping.solardata()
            data = data.loc[['2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', '2020-12-07', '2020-12-08',
                                '2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06', '2021-12-07', '2021-12-08']]
            for nan in range(len(data)-1):
                if data[['solar']].isna().iloc[:, 0][nan]:
                    data['solar'][nan] = (data['solar'][nan-1] + data['solar'][nan+1])/2
                    data['solar'][len(data)-1] = (data['solar'][len(data)-2]+data['solar'][len(data)-3])/2
            data.index = pd.to_datetime(data.index)
            data.set_index('hour', inplace=True)
            data = data.sort_values(by='hour', ascending=True)
            mean = data.groupby(['hour'])['solar'].mean()
            plt.figure()
            mean.plot(color='blue')
            plt.title('Solar Energy Consumption Prediction for the 8th of December 2022')
            plt.xlabel('Time')
            plt.ylabel('MW')
            plt.savefig('Solar_Energy_Consumption', format = 'pdf')
            solarconsumption = mean.to_frame()
            print(solarconsumption)
            return(data, mean)
        elif energy == 'hydraulic':
            data = datashaping.datashaping.hydraulicdata()
            data = data.loc[['2013-12-01', '2013-12-02', '2013-12-03', '2013-12-04', '2013-12-05', '2013-12-06', '2013-12-07', '2013-12-08',
                                '2014-12-01', '2014-12-02', '2014-12-03', '2014-12-04', '2014-12-05', '2014-12-06', '2014-12-07', '2014-12-08',
                                '2015-12-01', '2015-12-02', '2015-12-03', '2015-12-04', '2015-12-05', '2015-12-06', '2015-12-07', '2015-12-08',
                                '2016-12-01', '2016-12-02', '2016-12-03', '2016-12-04', '2016-12-05', '2016-12-06', '2016-12-07', '2016-12-08',
                                '2017-12-01', '2017-12-02', '2017-12-03', '2017-12-04', '2017-12-05', '2017-12-06', '2017-12-07', '2017-12-08',
                                '2018-12-01', '2018-12-02', '2018-12-03', '2018-12-04', '2018-12-05', '2018-12-06', '2018-12-07', '2018-12-08',
                                '2019-12-01', '2019-12-02', '2019-12-03', '2019-12-04', '2019-12-05', '2019-12-06', '2019-12-07', '2019-12-08',
                                '2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06', '2020-12-07', '2020-12-08',
                                '2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06', '2021-12-07', '2021-12-08']]
            for nan in range(len(data)-1):
                if data[['hydraulic']].isna().iloc[:, 0][nan]:
                    data['hydraulic'][nan] = (data['hydraulic'][nan-1] + data['hydraulic'][nan+1])/2
                    data['hydraulic'][len(data)-1] = (data['hydraulic'][len(data)-2]+data['hydraulic'][len(data)-3])/2
            data.index = pd.to_datetime(data.index)
            data.set_index('hour', inplace=True)
            data = data.sort_values(by='hour', ascending=True)
            mean = data.groupby(['hour'])['hydraulic'].mean()
            plt.figure()
            mean.plot(color='blue')
            plt.title('Hydraulic Energy Consumption Prediction for the 8th of December 2022')
            plt.xlabel('Time')
            plt.ylabglobalel('MW')
            plt.savefig('Hydraulic_Energy_Consumption', format = 'pdf')
            hydraulicconsumption = mean.to_frame()
            print(hydraulicconsumption)
            return(data, mean)
        else :
            print('The choosen energy is not in the available ones.')
      
print(prediction.dataset())
