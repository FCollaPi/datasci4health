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

## Entry Data

The authors could not make the raw data available due to the reasons above, so they pre-processed it and maintained it as described in the following table:

|        Dataset       |    Address    |     Description   |
| :------------------: | :-----------: | :---------------: | 
|         Título       |https://github.com/rionbr/DDIBlumenau/tree/master/csv | CSVs containing data anonymized on patients,  administered drugs, and processed results  |

No other data source was necessary for conducting this experiment replication.

## Complex Network Graph

Also, the authors are not straightforward on which kind of algorithm they used to organize the network, so we used our best judgment on a trial and error basis to assemble the network as they did.

In contrast to the authors, we used Cytoscape to generate the complex network. Therefore, we could not fully reproduce the network as the authors, but we will present our best representation in the result section of this report.

The CSV files used in this portion are foundable [here](https://github.com/rionbr/DDIBlumenau/tree/master/csv).

## Handling Data

The authors crafted several python scripts to create the network and analyze the data. The scripts are available [here](https://github.com/rionbr/DDIBlumenau).

We could not validate most of the python files due to the lack of the appropriate input data. As already mentioned, data could not be made available for agreement and regulation reasons.

The authors also mentioned they could release the data in appropriate electronic form with due permission from the city of Blumenau upon reasonable requests. However, unfortunately, that diverged from our time constraints.

So we focused our efforts on replicating the experiment at length to report our findings and a replicability rate. We will further describe the steps taken in the coming section.


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

This is the original graph shown in the article:
<img width="900" alt="network-original" src="https://user-images.githubusercontent.com/54454569/172077307-c0eb593b-91bc-45e4-9928-e154f8a30666.png">

### Replication

This is the graph we could sought to reproduce:
<img width="900" alt="network" src="https://user-images.githubusercontent.com/54454569/172077335-a0472cb7-3feb-41fc-9d35-ab9c77243061.png">

Differences are particularly latent, albeit efforts to mitigate them.

We had difficulty achieving similar results using different tools and having no formula to translate the work to a different platform.

## Scripts

The available scripts are three years old, leading us to find inconsistencies with updated technology that could hinder the whole process. For example, they all used notation from python 2.x, whereas we are on version 3.10.

We decided to update all scripts to the 3.x notation and check for progress. Nonetheless, we stepped across another hiccup: most of the required entry data is not publicly available.

Of the 18 available python scripts, eleven are still executable, and seven are not, as seen in the downward chart:

<img width="500" alt="chart" src="https://user-images.githubusercontent.com/54454569/172206740-6aee8cbc-de81-42f3-974d-414b8e6746d4.png">

Working scripts, their description, and results are:
- `plot_network_dist.py`: Information on nodes and edges (limited by the first five tuples) and the histogram plot relating the number of drugs administered to the recurrency of know interaction (that translates to the property `value` in the node table and `weight` on the edge table).

#### Nodes

|   |   dbi |p_node|hormone|len_i |degree| color |degree-strength|      label  |node_bet_cent|module-louvain|module-infomap|         class       |rank_degree|
|:-:| :----:|:----:|:-----:|:---: |:----:|:-----:|:-------------:|:-----------:|:-----------:|:------------:|:------------:|:-------------------:|:---------:|
| 0 |DB00252|0.20  |False  |42794 |   24 |#976fb0|       6.51    |Phenytoin    |      0.30   |        2     |      1       |CNS agents           |       1   |
| 1 |DB00564|0.18  |False  |87950 |   18 |#976fb0|       4.84    |Carbamazepine|      0.20   |        0     |      2       |CNS agents           |       2   |
|2  |DB01174|0.05  |False  |13638 |   15 |#976fb0|       2.17    |Phenobarbital|      0.28   |        2     |      1       |CNS agents           |       3   |
|3  |DB00571|0.10  |False  |109099|   14 |#ee262c|       4.81    |Propranolol  |      0.06   |        4     |      0       |Cardiovascular agents|       4   |
|4  |DB00682|0.13  |False  |57959 |   14 |#f498b7|       3.31    |Warfarin     |      0.17   |        1     |      3       |Coagulation modifiers|       4   |

#### Edges

|   |   dbi |  dbj  | tau|severity|weight|edge_bet_cent|  color|gender|patients_norm|RRI^F |patients|tau_norm|RRI^M|   label_i   |    label_j   |
|:-:| :----:|:-----:|:--:|:------:|:----:|:----------: |:-----:|:----:| :---------: |:---: |:------:| :----: |:---:|:-----------:|:------------:|
| 0 |DB01174|DB00741|0.01|Moderate| 1.13 |    0.20     |#976fb0|Female|    1.01     | 1.42 |    3   |   1.13 | 0.71|Phenobarbital|Hydrocortisone|
| 1 |DB00252|DB00741|0.02|Moderate| 1.26 |    0.19     |#976fb0| Male |    1.00     | 0.71 |    2   |   1.26 | 1.41|Phenytoin    |Hydrocortisone|
|2  |DB00682|DB00537|0.07|Major   | 1.90 |    0.14     |#976fb0|Female|    1.06     | 1.02 |   22   |   1.90 | 0.98|Warfarin     |Ciprofloxacin |
|3  |DB00916|DB01174|0.04|Moderate| 1.51 |    0.14     |#ee262c|Female|    1.02     | 1.18 |    8   |   1.51 | 0.85|Metronidazole|Phenobarbital |
|4  |DB01223|DB00199|0.02|Moderate| 1.26 |    0.14     |#f498b7|Female|    1.00     |126.09|    1   |   1.26 | 0.00|Aminophylline|Erythromycin  |

##### Plot
<img width="900" alt="img-graph-dist" src="https://user-images.githubusercontent.com/54454569/172216868-8c1232a7-50a5-4109-9dce-0653750a7409.png">


- `plot_colorbar2graph.py`:
- `calculate_pca.py`:
- `display_ml.py`:
- `plot_rc_age_gender.py`:
- `plot_u_coadmin_age.py`:
- `plot_u_coadmin_age_gender.py`:
