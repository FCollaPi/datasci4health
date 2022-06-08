# Project 3 - DataSci4Health

# Reproducing experiments from City-wide electronic health records reveal gender and age biases in administration of known drug-drug interactions".

# Intro

We developed this project in the context of the graduate subject [Data Science and Visualization for Health](https://ds4h.org/) for the 2022.1 term at Unicamp.

|        Name       |       RA      |  Especialization  |
| :---------------: | ------------- | ----------------- | 
| Felipe Pinheiro   |     155298    | Computer Science  |
| Guilherme Jardim  |     203834    | Computer Science  |

In this project we aim to reproduce an article that uses complex networks for health research.

# Citation

The [database](https://icon.colorado.edu/#!/networks) suggested by the subject professors led us to find the chosen article, which was "City-wide electronic health records reveal gender and age biases in administration of known drug-drug interactions" and can be found [here](https://www.nature.com/articles/s41746-019-0141-x).

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

We plotted the network graph on Cytoscape, in contrast with the authors who used in-house developed scripts.

Since the techniques were different and the article does not cover the visualization of the graph in any shape or form, and, although very complete, Cytoscape is not very reliable (and crashed several times during our attempts), trial and error served as a beacon to reaching the results:

1. Import the CSV file `net_edges.csv` as a network;
2. Import the CSV file `net_nodes.csv` as a node table;
3. Configure the node styles so it can use the column `color` for coloring the nodes and the column `p_node` as the reference for dimensioning the node's size;
4. Import the CSV file `net_edges.csv` as an edge table;
5. Configure the edge style to use the column `color` for coloring the edges and the column `weight` for dimensioning the edge's size.
6. Since we went through a different plot of the graph, we had to test the organizing algorithms. We chose the `Prefuse Force Directed OpenCL Layout` technique based on the `weight` attribute.

We renamed the columns `color` to match their specific reference (`node-color` and `edge-color`) during the process, but that is not necessary because Cytoscape is smart enough to differentiate both.

After that first trial, a new column `our-color` had to be added to the edges table since the original one had only shades of gray and red, meaning that the it could not reflect the visualization provided on the original paper. To correct that, the colors were recalculated using the Relative Risk of Interaction (RRI) columns of the aforementioned table, with the RGB value of 70 corresponding to the minimun RRI value and 255 corresponding to the maximum RRI value. We used [this](https://github.com/FCollaPi/datasci4health/blob/main/p3/notebooks/1.0-explore-nodes-and-edges.ipynb) notebook for that purpose.

We also decided to explore the the scripts made available in that same repository.

# Results

## Complex Network Graph

### Original

For comparison, this is the original graph shown in the article:

<img width="900" alt="network-original" src="https://user-images.githubusercontent.com/54454569/172077307-c0eb593b-91bc-45e4-9928-e154f8a30666.png">

Each node is a dispensed drug. Nodes are colored according to their primary activity. Edge weights are given by the measure $\tau$<sub>i,j</sub><sup>$\phi$</sup>, which stands for the normalized length of co-administration of drugs i and j with known DDI, and is represented as the thickness of that edge. Node size reflects the Probability of Interaction (PI) of that drug. Edges are colored using the Relative (to gender) Risk of Interaction (RRI). That colormap is calculated proportionally (a stronger color means a higher value) and stratified by gender (red for female and blue for male), meaning that the specified gender have a higher risk of being dispensed a pair of drugs that have known interaction than the opposite gender.

### Replication

The first produced graph is the following:

<img width="900" alt="network" src="https://user-images.githubusercontent.com/54454569/172077335-a0472cb7-3feb-41fc-9d35-ab9c77243061.png">

It can be seen that only red and gray edges are displayed.


This is the graph we could sought to reproduce after a color fix and minor layout improvements.

<img width="900" alt="network" src="https://github.com/FCollaPi/datasci4health/blob/main/p3/assets/2nd-network.png?raw=true">

We then could achieve network similar to that displayed on the original article. It can be seen that most edges are red, meaning that most of the co-admnistered drugs have a higher risk of interaction among those prescribed to women than those prescribed to men.

Also, the node sizes and colors appear to follow those shown in the original representation.

## Scripts

The available scripts are three years old, leading us to find inconsistencies with updated technology that could hinder the whole process. For example, they all used notation from python 2.x, whereas we are on version 3.10.

We decided to update all scripts to the 3.x notation and check for progress. Nonetheless, we stepped across another hiccup: most of the required entry data is not publicly available.

Of the 18 available python scripts, eleven are still executable, and seven are not, as seen in the downward chart:

<img width="900" alt="chart" src="https://user-images.githubusercontent.com/54454569/172206740-6aee8cbc-de81-42f3-974d-414b8e6746d4.png">

Working scripts, their description, and results are:
- `plot_network_dist.py`: Information on nodes and edges (limited by the first five tuples) and the histogram plot relating the number of drugs administered to the recurrency of know interaction (that translates to the property `value` in the node table and `weight` on the edge table).

    - #### Nodes

    |   |   dbi |p_node|hormone|len_i |degree| color |degree-strength|      label  |node_bet_cent|module-louvain|module-infomap|         class       |rank_degree|
    |:-:| :----:|:----:|:-----:|:---: |:----:|:-----:|:-------------:|:-----------:|:-----------:|:------------:|:------------:|:-------------------:|:---------:|
    | 0 |DB00252|0.20  |False  |42794 |   24 |#976fb0|       6.51    |Phenytoin    |      0.30   |        2     |      1       |CNS agents           |       1   |
    | 1 |DB00564|0.18  |False  |87950 |   18 |#976fb0|       4.84    |Carbamazepine|      0.20   |        0     |      2       |CNS agents           |       2   |
    |2  |DB01174|0.05  |False  |13638 |   15 |#976fb0|       2.17    |Phenobarbital|      0.28   |        2     |      1       |CNS agents           |       3   |
    |3  |DB00571|0.10  |False  |109099|   14 |#ee262c|       4.81    |Propranolol  |      0.06   |        4     |      0       |Cardiovascular agents|       4   |
    |4  |DB00682|0.13  |False  |57959 |   14 |#f498b7|       3.31    |Warfarin     |      0.17   |        1     |      3       |Coagulation modifiers|       4   |

    - #### Edges

    |   |   dbi |  dbj  | tau|severity|weight|edge_bet_cent|  color|gender|patients_norm|RRI^F |patients|tau_norm|RRI^M|   label_i   |    label_j   |
    |:-:| :----:|:-----:|:--:|:------:|:----:|:----------: |:-----:|:----:| :---------: |:---: |:------:| :----: |:---:|:-----------:|:------------:|
    | 0 |DB01174|DB00741|0.01|Moderate| 1.13 |    0.20     |#976fb0|Female|    1.01     | 1.42 |    3   |   1.13 | 0.71|Phenobarbital|Hydrocortisone|
    | 1 |DB00252|DB00741|0.02|Moderate| 1.26 |    0.19     |#976fb0| Male |    1.00     | 0.71 |    2   |   1.26 | 1.41|Phenytoin    |Hydrocortisone|
    |2  |DB00682|DB00537|0.07|Major   | 1.90 |    0.14     |#976fb0|Female|    1.06     | 1.02 |   22   |   1.90 | 0.98|Warfarin     |Ciprofloxacin |
    |3  |DB00916|DB01174|0.04|Moderate| 1.51 |    0.14     |#ee262c|Female|    1.02     | 1.18 |    8   |   1.51 | 0.85|Metronidazole|Phenobarbital |
    |4  |DB01223|DB00199|0.02|Moderate| 1.26 |    0.14     |#f498b7|Female|    1.00     |126.09|    1   |   1.26 | 0.00|Aminophylline|Erythromycin  |

    - #### Plot

    <img width="900" alt="img-graph-dist" src="https://user-images.githubusercontent.com/54454569/172216868-8c1232a7-50a5-4109-9dce-0653750a7409.png">


- `plot_colorbar2graph.py`: Outputs only a scale used on an unplottable graph

<img width="300" alt="colorbar" src="https://user-images.githubusercontent.com/54454569/172240943-9e855882-e783-41d3-a2a2-8ceebc7e58ec.png">

- `calculate_pca.py`: Does not output any file, only updating a table that we also cannot create due to the lack of entry data.


- `display_ml.py`: Uses classifiers to assess the models

    - Classifier: `Biased Dummy`

    |fold|precision|recall|  f1  |  mcc  |roc_auc|pr_auc|
    |:--:|:-------:|:----:|:----:|:-----:|:-----:|:----:|
    |  2 |   0.1112|0.1118|0.1115|-0.0066|0.4967 |0.1635|
    |  4 |   0.1094|0.1100|0.1097|-0.0086|0.4957 |0.1618|
    |  1 |   0.1240|0.1247|0.1243| 0.0080|0.5040 |0.1755|
    |  3 |   0.1143|0.1149|0.1146|-0.0031|0.4984 |0.1664|
    |Mean|   0.1147|0.1153|0.1150|-0.0026|0.4987 |0.1668|

    - Classifier: `Linear SVM`

    |fold|precision|recall|  f1  |  mcc |roc_auc|pr_auc|
    |:--:|:-------:|:----:|:----:|:----:|:-----:|:----:|
    |  4 |   0.8185|0.6439|0.7208|0.6949|0.9690 |0.8310|
    |  3 |   0.8127|0.6504|0.7226|0.6957|0.9697 |0.8315|
    |  2 |   0.8241|0.6494|0.7264|0.7011|0.9702 |0.8365|
    |  1 |   0.8196|0.6309|0.7130|0.6877|0.9676 |0.8269|
    |Mean|   0.8187|0.6437|0.7207|0.6949|0.9691 |0.8315|

    - Classifier: `Logistic Regression`

    |fold|precision|recall|  f1  |  mcc |roc_auc|pr_auc|
    |:--:|:-------:|:----:|:----:|:----:|:-----:|:----:|
    |  2 |   0.8096|0.6669|0.7314|0.7037|0.9700 |0.8337|
    |  1 |   0.8085|0.6535|0.7228|0.6953|0.9675 |0.8249|
    |  4 |   0.8092|0.6612|0.7277|0.7002|0.9691 |0.8304|
    |  3 |   0.7991|0.6662|0.7266|0.6977|0.9697 |0.8299|
    |Mean|   0.8066|0.6619|0.7271|0.6992|0.9691 |0.8297|
    

    - Classifier: `Rough Dummy`


    |fold|precision|recall|  f1  |  mcc |roc_auc|pr_auc|
    |:--:|:-------:|:----:|:----:|:----:|:-----:|:----:|
    |  4 |   0.2056|0.8856|0.3337|0.2779|0.7161 |0.5523|
    |  3 |   0.2043|0.8843|0.3320|0.2752|0.7140 |0.5511|
    |  2 |   0.2048|0.8797|0.3323|0.2747|0.7136 |0.5493|
    |  1 |   0.2029|0.8841|0.3300|0.2725|0.7119 |0.5503|
    |Mean|   0.2044|0.8834|0.3320|0.2751|0.7139 |0.5507|

    - Classifier: `Uniform Dummy`

    |fold|precision|recall|  f1  |  mcc  |roc_auc|pr_auc|
    |:--:|:-------:|:----:|:----:|:-----:|:-----:|:----:|
    |  4 |   0.1184|0.5086|0.1920|0.0043 |0.5    |0.5585|
    |  3 |   0.1152|0.4951|0.1869|-0.0055|0.5    |0.5585|
    |  2 |   0.1195|0.5134|0.1939|0.0078 |0.5    |0.5585|
    |  1 |   0.1194|0.5129|0.1937|0.0074 |0.5    |0.5585|
    |Mean|   0.1181|0.5075|0.1916|0.0035 |0.5    |0.5585|

    >TODO

- `plot_rc_age_gender.py`: Plots the relationship between risk of co-administration of medication, split by gender and referencing it through age.

<img width="900" alt="img-rc-age-gender" src="https://user-images.githubusercontent.com/54454569/172390880-399e1db9-5888-4ac0-9a06-c26b4fd3061f.png">


- `plot_u_coadmin_age.py`: Plots the relation between the co-administration of medication using age as a reference axis.

<img width="900" alt="img-u-coadmin-age" src="https://user-images.githubusercontent.com/54454569/172391426-7cf399cf-233d-4c94-9660-05c86c86b399.png">


- `plot_u_coadmin_age_gender.py`: Plots the relation between the co-administration of medication using age as a reference axis and splitting the curves by gender. This three-dimensional analysis allows a more granular risk analysis within Blumenau's population.

<img width="900" alt="img-u-coadmin-age-gender" src="https://user-images.githubusercontent.com/54454569/172391489-825335d2-1a0c-4fb3-90d6-4ef94e91ad3d.png">

# Conclusion

Even though partially, we were able to reproduce the original article results.
