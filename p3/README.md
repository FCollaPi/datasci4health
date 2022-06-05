# Project 3 - DataSci4Health

# Reproducing experiments from "city-wide electronic health records reveal gender and age biases in administration of known drug-drug interactions".

# Intro
We developed this project in the context of the graduate subject [Data Science and Visualization for Health](https://ds4h.org/) for the 2022.1 term at Unicamp.

|        Name       |       RA      |  Especialization  |
| :---------------: | ------------- | ----------------- | 
| Felipe Pinheiro   |     155298    | Computer Science  |
| Guilherme Jardim  |     203834    | Computer Science  |

# Citation
The [suggested database](https://icon.colorado.edu/#!/networks) led us to find the chosen article, which was "city-wide electronic health records reveal gender and age biases in administration of known drug-drug interactions" and can be found [here](https://www.nature.com/articles/s41746-019-0141-x).

# Article Abstraction
The authors tackle the drug-drug interaction (DDI) of pharmaceutical therapies provided by the universal public health services in a Brazilian countryside city.

Since Brazil is known to be a continental-sized country, Blumenau's elevated HDI enabled the statistical generalization of the findings the authors sought, underpinning their choice.
Gathering 18 months of data, regarding pharmacotherapy, from electronic health records (EHR) enabled a thorough analysis of possible DDI from gender, education, neighborhood influence, and specific dispensed drugs perspectives.

The authors used previous top-known interactions data to establish assumptions and cluster medicine and interactions by severity on a 4-point scale (None, Minor, Moderate, Major). That previous data also facilitated drawing comparisons with the gathered data.

EHR also provided enough data so the authors could characterize patients on a multitude of demographic dimensions (such as gender, age, and education). That characterization confirmed hypotheses such as women being at a greater risk of DDI than men but also denied others such as education playing a role in the risk of DDI.

Machine learning models also came into play to aid the predictability of DDI based on available data.

# Breve descrição do experimento/análise do artigo que foi replicado
> Descreva brevemente a parte do artigo cujo experimento ou análise foi reproduzido. Explique o que foi usado como entrada e saída.

## Dados usados como entrada
Dataset | Endereço na Web | Resumo descritivo
----- | ----- | -----
Título do Dataset | http://base1.org/ | Breve resumo (duas ou três linhas) sobre o dataset.

# Método
> Método usado para a análise -- adaptações feitas, ferramentas utilizadas, abordagens de análise adotadas e respectivos algoritmos.
> Etapas do processo reproduzido.

# Resultados
> Apresente os resultados obtidos pela sua adaptação.
> Confronte os seus resultados com aqueles do artigo.
> Esta seção opcionalmente pode ser apresentada em conjunto com o método.
