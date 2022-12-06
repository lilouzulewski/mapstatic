Consumption Prediction
=======================
The steps of that led to the prediction will be detailed in the three parts below: the data, the preprocess, and the model development.

Data  
^^^^^
The French consumption data was imported from the `government <https://odre.opendatasoft.com/explore/dataset/eco2mix-regional-cons-def/table/?disjunctive.libelle_region&disjunctive.nature&sort=-date_heure>`_ website linked using the below class before applying the predictive model:

.. class:: datadownloading

This dataset is composed of the different types of energy (global, thermal, nuclear, wind, solar, hydraulic,) and their respective consumption value in France for every thirty minutes since 2013.

Preprocess
^^^^^^^^^^^
Now that the dataset is imported, it has to be cleaned and prepped for better use.

Thus, new dataframes were deduced for each type of energy including only variables of time and values of consumption in MW. The original dataset also contained NaN values (missing values) that had to be replaced by the mean of closer values.
Another class was introduced to do this job:

.. class:: datashaping

If one wishes to view only the thermal dataframe for instance, simply type the following command in a python editor:

.. code-block:: python

    print(datashaping.datashaping.solardata())

The output resembles the table below:

+-------------+----------+----------+
|*date*       |*hour*    |*thermal* |
+=============+==========+==========+
|`...`        |`...`     | \...     |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \345.0   |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \5.0     |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \1220.0  |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \28.0    |
+-------------+----------+----------+
|`2022-05-31` |`23:30`   | \883.0   |
+-------------+----------+----------+

Modelisation
^^^^^^^^^^^^^
How to use ?
""""""""""""
In order to predict the consumption of any energy on the 8th of December 2022, one last class was created.

.. class:: datamodeling

This class asks the user to choose a certain type of energy and returns a dataframe of the predicted consumption every thirty minutes along with its associated graph.
Simply type in the following command in an python editor:

.. code-block:: python

    print(prediction.dataset())

Let's take the former example, if the user writes 'thermal', the ouput will be:

+----------+-------------+
|*hour*    |*thermal*    |
+==========+=============+
|`00:00`   | \732.256944 |
+----------+-------------+
|`00:30`   | \715.935764 |
+----------+-------------+
|`01:00`   | \679.218750 |
+----------+-------------+
|`01:30`   | \684.390625 |
+----------+-------------+
|`...`     | \...        |
+----------+-------------+
|`23:30`   | \719.147569 |
+----------+-------------+

Then, the following graph will be displayed:

.. image:: ../_images/thermalprediction.pdf
   :align: center


What is the model behind ?
""""""""""""""""""""""""""
In order to predict consumption of all different types of energy, we chose to use a simple and understable method. Evidently, other methods are available but prerequisited knowledge on time series would be necessary which is a rather complicated mathematical field.
The method chosen relied on means.

First, we observed the behaviour of all energies' consumptions since 2013 to distinguish a tendency. For that, we used the ``datashaping`` class to plot each energy according to its dataframe values.

.. code-block:: python

    datashaping.consumptiondata().plot(figsize=(20, 5), title="French Global Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.thermaldata().plot(figsize=(20, 5), title="French Thermal Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.nucleardata().plot(figsize=(20, 5), title="French Nuclear Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.winddata().plot(figsize=(20, 5), title="French Wind Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.solardata().plot(figsize=(20, 5), title="French Solar Energy Consumption Since 2013", xlabel='Date', ylabel='MW')
    datashaping.hydraulicdata().plot(figsize=(20, 5), title="French Hydraulic Energy Consumption Since 2013", xlabel='Date', ylabel='MW')

Here, there is an annual pattern and not a significative increase or decrease of global consumption for instance.

 .. image:: ../_images/globalconsumption.pdf
   :align: center

This explains the fact that we have chosen to select all the data of global consumption from December of each year since 2013 to predict its value on the 8th December of 2022 using the following class:

.. class:: prediction

The previous class selects the correct data, averages them, and finally, plots them. As explained, the selected data depends on observable behaviour from the dataframes.

Surely, there are several other parameters that could be taken into account in order to have a better prediction (like temperature, cost of each energy, etc.). Though, with the data at hand, we did't have access to many parameters that come at play in predicting accurately the consumption rate.



