# Project 3 - DataSci4Health

# Reproducing experiments from City-wide electronic health records reveal gender and age biases in administration of known drug-drug interactions".

# Intro
We developed this project in the context of the graduate subject [Data Science and Visualization for Health](https://ds4h.org/) for the 2022.1 term at Unicamp.

|        Name       |       RA      |  Especialization  |
| :---------------: | ------------- | ----------------- | 
| Felipe Pinheiro   |     155298    | Computer Science  |
| Guilherme Jardim  |     203834    | Computer Science  |

# Citation
The [suggested database](https://icon.colorado.edu/#!/networks) led us to find the chosen article, which was "City-wide electronic health records reveal gender and age biases in administration of known drug-drug interactions and can be found [here](https://www.nature.com/articles/s41746-019-0141-x).

Since this article has a perennial nature and an organic adherence to Brazilian reality, selecting it was somewhat easy. Not only that but the size and complexity of their data processing sounded reasonable within our time constraints.

# Article Abstraction
The authors tackle the drug-drug interaction (DDI) of pharmaceutical therapies provided by the universal public health services in a Brazilian countryside city.

Since Brazil is known to be a continental-sized country, Blumenau's elevated HDI enabled the statistical generalization of the findings the authors sought, underpinning their choice.

Gathering 18 months of data, regarding pharmacotherapy, from electronic health records (EHR) enabled a thorough analysis of possible DDI from gender, education, neighborhood influence, and specific dispensed drugs perspectives.

The authors used previous top-known interactions data to establish assumptions and cluster medicine and interactions by severity on a 4-point scale (None, Minor, Moderate, Major). That previous data also facilitated drawing comparisons with the gathered data.

EHR also provided enough data so the authors could characterize patients on a multitude of demographic dimensions (such as gender, age, and education). That characterization confirmed hypotheses such as women being at a greater risk of DDI than men and denied others such as education playing a role in DDI risk.

Machine learning models also came into play to aid the predictability of DDI based on available data.

# Experiment Description
The experiment's reproduction started by creating the complex network the authors created based on DDI observed in Blumenau.

Since the raw data could not be made available due to legislation and de-anonymization avoidance, we could only work with pre-processed data on the articles' [GitHub](https://github.com/rionbr/DDIBlumenau).

Many of the references from the article could not be translated ipsis literis to the column names (such as variables like π or U), so understanding the data became a challenge.

## Complex Network Graph

Also, the authors are not straightforward on which kind of algorithm they used to organize the network, so we used our best judgment on a trial and error basis to assemble the network as they did.

In contrast to the authors, we used Cytoscape to generate the complex network. Therefore, we could not fully reproduce the network as the authors, but we will present our best representation in the result section of this report.

The CSV files used in this portion are foundable [here](https://github.com/rionbr/DDIBlumenau/tree/master/csv).

## Data Analysis

The authors crafted several python scripts to create the network and analyze the data. The scripts are available [here](https://github.com/rionbr/DDIBlumenau).

>TODO

## Entry Data

The authors could not make the raw data available due to the reasons above, so they pre-processed it and maintained it as described in the following table:

|        Dataset       |    Address    |     Description   |
| :------------------: | :-----------: | :---------------: | 
|         Título       |https://github.com/rionbr/DDIBlumenau/tree/master/csv | CSVs containing data anonymized on patients,  administered drugs, and processed results  |

No other data source was necessary for conducting this experiment replication.


# Method

## Complex Network Graph
We plotted the network graph on Cytoscape, in contrast with the authors who used in-house developed scripts.

Since the techniques were different and the article does not cover the visualization of the graph in any shape or form, and, although very complete, Cytoscape is not very reliable (and crashed several times during our attempts), trial and error served as a beacon to reaching the results:

1. Import the CSV file `net_edges.csv` as a network;
2. Import the CSV file `net_nodes.csv` as a node table;
3. Configure the node styles so it can use the column `color` for coloring the nodes and the column `p_node` as the reference for dimensioning the node's size;
4. Import the CSV file `net_edges.csv` as an edge table;
5. Configure the edge style to use the column `color` for coloring the edges and the column `weight` for dimensioning the edge's size.
6. Since we went through a different way of plotting the graph, we had to test the organizing algorithms. We chose the `Prefuse Force Directed OpenCL Layout` technique based on the `weight` attribute.

We renamed the columns `color` to match their specific reference (`node-color` and `edge-color`) during the process, but that is not necessary because Cytoscape is smart enough to differentiate both.

### Original
<img width="900" alt="network-original" src="https://user-images.githubusercontent.com/54454569/172077307-c0eb593b-91bc-45e4-9928-e154f8a30666.png">

### Replication
<img width="900" alt="network" src="https://user-images.githubusercontent.com/54454569/172077335-a0472cb7-3feb-41fc-9d35-ab9c77243061.png">
