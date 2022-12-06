Interactive Map
================

Concept
^^^^^^^

The map is based on the power consumption database downloaded from the link provided on the official `government <https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B>`_ website and spreads out the consumption data on the map given the commune.
The mean of consumption throughout the past 4 years is the value represented.
With ``Folium``, the map is firstly defined as:

.. code:: python

    mymap = folium.Map(location=[46.2276,2.2137], zoom_start=5.5)

The coordinates being those of France.

Choropleth
^^^^^^^^^^

``Choropleth`` is the function that helped introduce the data to the Folium map. The below code was used:

.. code-block:: python

    mymap.choropleth(
        geo_data=geo_json_data,
        name='Communes',
        data=commune_avg,
        columns=['Nom de la commune','Consommation annuelle moyenne de la commune (MWh)'],
        key_on="feature.properties.libgeo",
        fill_color='YlGnBu', nan_fill_color="#FF000000",
        fill_opacity=1,
        line_opacity=0.2,
        legend_name='Consommation moyenne des 4 dernières années (MWh)',
        smooth_factor=0
    )

The ``geo_data`` option is used for the file containing the coordinates of the communes, and ``data`` is for the data added to the map. As for the color fills, it is simply for visual effects and can be easily changed depending on preference.


Folium Package & Other Ressources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``Folium`` package allows the manipulation of the map of the world using specific coordinates. 
With the coordinates of France being known, and a geo json file found on github with the coordinates of each commune, it was easy to join those in the json file with the commune names in the dataset at hand.
`Here <https://www.data.gouv.fr/fr/datasets/r/fb3580f6-e875-408d-809a-ad22fc418581>`_  is the used link for the json file.

The ``Folium`` package contains several tools including the one used to implement the interactive feature of the map:

.. code-block:: python

    folium.features.GeoJson(
        data=df_final,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['Nom de la commune','Consommation annuelle moyenne de la commune (MWh)'],
            aliases=['Commune: ','Consommation moyenne (MWh): '],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
            localize=True,
            sticky=True,
            labels=True,
            )
    ).add_to(mymap)

The ``df_final``  dataset is a merge between the json file previously used and the dataset. It allows to match the geometry features of the communes to the ones in the database, removing any commune that does not have data.
Both the ``style_function`` and ``highlight_function`` are defined according to preference before the function.
The ``GeoJsonTooltip`` feature details what part of the data will be displayed when you hover over the selected commune.

Output
^^^^^^

The map was saved in HTML format using:

.. code:: python

    mymap.save("mymap.html")


An HTML view of the map is linked `here <./mymap.html>`_.
The file might be too large to load, which is why we provided an image in PDF format to help visualize the result better:

.. image:: ../_images/mymap.pdf.pdf
    :width: 500
    :alt: Interactive Map of France
    :align: center



