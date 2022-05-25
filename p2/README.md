
# Project 2 - DataSci4Health
# Predicting Death on Stress, Psychotropic Abuse, Violence Scenarios, and Anxiety Settings

## Intro
We developed this project in the context of the graduate subject [Data Science and Visualization for Health](https://ds4h.org/) for the 2022.1 term at Unicamp.

|        Name       |       RA      |  Especialization  |
| :---------------: | ------------- | ----------------- | 
| Felipe Pinheiro   |     155298    | Computer Science  |
| Guilherme Jardim  |     203438    | Computer Science  |

## Contextualization

Literature has shown us how much stress impacts day-to-day life, so it was very intuitive to circle stress-triggering variables (e.g., Violence Scenarios, Intimate Abuse) and the consequences of said stress and compute a possible interaction between them.

News and articles on psychotropic-substances abuse as a cause of stress in different settings, either home or work-related, underpinned our decision to move forward with the attempt to find a relation of available parameters discussed in this report.

This decision-making process happened concurrently with the data analysis and a debate on what we should be searching. Finally, after available data seemed empirically satisfying, we decided to put together an actual question, so the process of assessing the data could be as tangible as possible.

The question mentioned above panned out as: "What is the death prognostic for patients submitted to depression screenings?".

Data analysis and trials on tests and scores showed unsatisfying results and a weak causal relation between those variables, which eventually led us to evolve the search question to:

"What is the death prognostic to victims of violence in environments and/or intimate partner abuse (also referred to as IPV) who are diagnosed with severe anxiety, stress, major depression disorder and show unhealthy psychotropic substances abuse?"

We used the same toolset as the one presented during classes, which consisted on:
### Tools
1. Python
	- Pandas
	- Numpy
	- SQLite3
2. SQL
3. Jupyter Notebook
	- on MyBinder
	- on Visual Studio Code
4. Orange

## Methodology
Professors extracted data from [Synthea](https://synthea.mitre.org), a synthetic health data generator. Then, they provided it through [Lab2Learn on GitHub](https://github.com/santanche/lab2learn), separated into four different scenarios, two of each we ended up using for this analysis.

We went through the tables to understand the available data during the preliminary analysis. Then, with that in hand, we had a brief discussion to shepherd our decisions moving forward - and we achieved a consensus that mental health awareness should serve as the foundation for our analysis.

Since we aimed at a direct relation between the aforementioned parameters, with no socio-economic constraint, we could drop tables containing data with prices, vendors, or anything that could sidetrack us from our goal, such as:
-   Allergies
-   Care plans
-   Claims
-   Organizations
-   Etc.

The procedure was circular across-the-board. First, we compiled data, designed a model, and executed testing - if the results were not satisfactory, we would return to assembling data.

In this context, we used the following parameters, as labeled in the Conditions table::
-   Severe Anxiety
-   Stress
-   Major Depression Disorder
-  Unhealthy Alcohol Drinking Behavior
-   Opioid Abuse
-   Drug Overdose
-   Misuses Drugs
-   Smokes Tobacco Daily
-   Reports of Violence in the Environment
-   Victim of Intimate Partner Abuse


### Used Bases
We exclusively used the given bases from the provided data as follows:
-   Scenario01
-   Scenario02

No other base of reference was required, nor were the extended bases provided.

## Project Evolution
We have been gathering results since the modeling part of the proposed problem. They pointed the direction toward our goal and helped us evolve the models in an intricate way to how they performed.

We had a `classification model` for assessing data related to death status (where 0 is for alive and 1 for dead) and a `regression model` targeting prognostics to evaluate how long it would take for a patient in the given scenario to die.

As previously stated, we wanted to tackle mental health issues and their relation to death. However, mental health thinned down to Depression Screening relatively soon since the available data was not granular enough.

However, unfortunately, we had to drop this attempt due to the lack of statistical relevance. We then added more interest variables and the `Principal Component Analysis` to enhance the likelihood of assembling a more robust model.

On Jupyter, we iterated through the available CSVs using SQL queries to understand the tendencies and create other tables that we could export and use on Orange, as recommended by the professors.

Intuitively, on the first run, we created tables from the following relations:
-   Patient-Encounter
-   Patient-Procedure
-   Patient-Condition

Once we assessed those tables from the `depression screening` standpoint and realized they were not enough, we added up more, so we ended with the following tables constrained on a timeframe:

|                            |  Trial 1 | Trial 2 | Trial 3 | 
| :------------------------: | :------: | :-----: | :-----: |
| Patient-Encounter          |     •    |         |         |
| Patient-Condition          |     •    |         |         |
| Patient-Drugs              |     •    |         |         |
| Depressive                 |          |     •   |         |
| Depression-Death           |          |     •   |         |
| Death-Conditions           |          |     •   |         |
| Conditions-Death-Counts    |          |     •   |         |
| Contidions-Type-Counts     |          |     •   |         |
| Encounters-Reasons-Counts  |          |         |    •    |
| Encounters-Type-Counts     |          |         |    •    |
| Medications-Reasons-Counts |          |         |    •    |
| Medications-Type-Counts    |          |         |    •    |

We will further explain the reasoning behind each addition alongside the results acquired after each trial due to their strong relationship.

As for the parameters, this is the timeframe in which they took place within our analysis:

|                            |  Trial 1 | Trial 2 | Trial 3 | 
| :------------------------: | :------: | :-----: | :-----: |
| Severe Anxiety             |     •    |         |         |
| Stress                     |     •    |         |         |
| Major Depression           |     •    |         |         |
| Unhealthy Alcohol Drinking |          |     •   |         |
| Opioid Abuse               |          |     •   |         |
| Drug Overdose              |          |     •   |         |
| Misuses Drugs              |          |     •   |         |
| Smokes Tobacco             |          |     •   |         |
| Reports of Violence        |          |         |     •   |
| Partner Abuse              |          |         |     •   |

### Trials
This section will report the trials and then present the results.

#### Trial 1
`input: depressive.csv`

For this first trial, we used the following parameters:
- Severe Anxiety
- Stress
- Major Depression

The results proved the data were not promising, which made us add more symptoms to strive for better success since the `Area Under Curve` was barely the same as a coin toss.

Due to the lack of a significant `Area Under Curve`, we opted not to deepen our analysis on this trial. Nevertheless, we gathered all results.

#### Classification Model

|          Model       |   AUC   |    CA   |    F1   | Precision |  Recall |
| :------------------: | :-----: | :-----: | :-----: | :-------: | :-----: |
| Tree                 |  1.000  |  1.000  |  1.000  |   1.000   |  1.000  |
| Neural Network       |  0.574  |  0.873  |  0.830  |   0.889   |  0.873  |
| Logistic Regression  |  0.500  |  0.850  |  0.782  |   0.723   |  0.850  |

The tree results were not feasible and made us realize we used the dead status as one of the analyzed variables instead of targeting it.

We also decided to drop the `Neural Network` moving forward due to the time required to obtain results.

The following ROC Curves illustrate the results shown in the Classification Table. It is visible that the tree curve (in purple) is not realistic, and the other curves (Neural Network in orange and Logistic Regression in green) are not good at all, being close to a purely random classifier.

<img width="650" alt="roc-1st" src="https://user-images.githubusercontent.com/54454569/169718522-1c2b6be3-6de4-4527-9a10-03c9bfadfe1b.png">

##### Confusion Matrix
The `Confusion Matrix` also results in the convergence of a mistake in the chosen settings thus far.

In a similar fashion, the total absence of false positives for all the matrixes in the first trial was alone a motive to raise suspicion.

The value 0 represents not dead (no death date is present in the Patients table) and 1 represents dead.

######  Tree
|   0  |   0  |   1  |   Σ  |
| ---: | ---: | ---: | ---: |
|   0  | 1990 |  0   | 1990 |
|   1  |  350 |  0   | 350  |
|   Σ  | 2340 |  0   | 2340 |

######  Neural Network
|   0  |   0  |   1  |   Σ  |
| ---: | ---: | ---: | ---: |
|   0  | 1990 |  0   | 1990 |
|   1  |  298 |  52  | 350  |
|   Σ  | 2288 |  52  | 2340 |

######  Logistic Regression
|   0  |   0  |   1  |   Σ  |
| ---: | ---: | ---: | ---: |
|   0  | 1990 |  0   | 1990 |
|   1  |    0 |  350 | 350  |
|   Σ  | 1990 |  350 | 2340 |

#### Regression Model
At this point, we were already convinced the model was a total failure, and the R2 results for the `Linear Regression` did not led us otherwise.

The `prognostic` target value used is calculated by subtracting the deathdate and the last encounter start date and scaling the result to days of each patient that has a registered death date, and -1 otherwise.

The values in the following table consider the prognostic in days, for the reason explained above.

|          Model       |          MSE           |      RMSE     |      MAE      |   R2  |
| :------------------: | :--------------------: | :-----------: | :-----------: | :---: |
| Linear Regression    | 343035556174557248.000 | 585692373.328 | 334186392.087 | 0.192 |

#### Trial 2
`input: Patient-Drugs.csv`

With the previous experience in hand, we decided to add more variables so we could search for more complex interactions. As a result, the model developed for this scenario also needed to be more complex in robustness.

The variables added for analysis were:
- Unhealthy Alcohol Drinking
- Opioid Abuse
- Drug Overdose
- Misuses Drugs
- Smokes Tobacco

Halfway through the modeling, during discussions, we felt the urge to add a few more variables (more on this later). However, we had much better results right out of the bat for the time being.

#### Classification Model
The PCA was a new addition to the analysis, which we had not included in the previous trial. In addition, the setup of the PCA required extra literature reading since we were not super confident about the relation between the number of components and the explained variance.

Besides that, correcting the fault mentioned above (not including the targeted variable as a parameter) enhanced the results immensely.

##### PCA
Principal Component Analysis (or PCA) consists of a technique to reduce the dimensionality of a set of variables by transforming them into a reduced set of orthogonal variables in a new space, therefore eliminating their linear dependency.

Literature did not recommend a manual selection of the number of components. Instead, picking an `Explained Variance` between 95-99% was the preferred way of setting up the PCA across the board.

For this trial, we had to settle for 94% of explained variance to achieve the number of 9 components. Anything equal to or greater than 95% would increase the number of components to 10, not affecting it since it is precisely the number of parameters used.

<img width="650" alt="pca-2" src="https://user-images.githubusercontent.com/54454569/169718528-17e63118-ceb7-4d8f-9379-0d32e5d435b2.png">

Despite the results being remarkably good, we again felt this might have been a confirmation bias, which served as the rationale for the subsequent trial.

Nonetheless, we did a detailed results analysis to better evolve the model.

|         Model       |   AUC   |    CA   |    F1   | Precision |  Recall |
| :-----------------: | :-----: | :-----: | :-----: | :-------: | :-----: |
| Tree                |  0.953  |  0.970  |  0.969  |   0.970   |  0.970  |
| Logistic Regression |  0.956  |  0.940  |  0.939  |   0.940   |  0.940  |

Even though this might have been the optimal model, we were not feeling confident due to the behemoth jump between the first and second attempts.

Going from 50/50 chances to a 95% did not sound plausible, even though both `ROC Curves` are now actually a curve (Tree in green and LR in orange).

<img width="650" alt="roc-2" src="https://user-images.githubusercontent.com/54454569/169718535-61fde6be-df41-49b6-b7aa-47fff2361e79.png">

Reassessing the model made us realize that all those positive results came from the `prognostic` being among the features and not set as a target.

Afterward, the debate inclined us to laugh at ourselves and add other plausible variables to this domain, not in this particular order. So from this point on, all analysis was solemnly to gather more metadata to improve the subsequent trial.

##### Confusion Matrix
Since all data was tainted with wrong inputs, additional analysis of the Matrixes would not be valuable in any shape or form.

######  Tree
|   0  |   0   |   1   |    Σ   |
| ---: | ----: | ----: | -----: |
|   0  | 89710 |  560  | 90270  |
|   1  | 3034  | 25286 | 28320  |
|   Σ  | 92744 | 25846 | 118590 |

######  Logistic Regression
|   0  |   0   |   1   |    Σ   |
| ---: | ----: | ----: | -----: |
|   0  | 88437 |  1833 | 90270  |
|   1  | 5271  | 23049 | 28320  |
|   Σ  | 93708 | 24882 | 118590 |

#### Regression Model
The following `Scatter Plot` is a soul representation of how mistakes can taint an evaluation. It presents the target value for the regression model (`prognostic`) in function of the 9th component extracted from the PCA. 

<img width="1000" alt="scatter-2" src="https://user-images.githubusercontent.com/54454569/169718555-e52b29be-9411-480f-88cb-ec650123345d.png">

The perfect - aside from the multiple - linear relation between the variables lead us to think the `prognostic` was being used as variable for the PCA model. If it were not for our suspicion, we could have assumed this model was an evident success. Being aware of the statistical behaviors and second guess results when they seemed too promising led us to the third and final trial.

#### Trial 3
input: Patient-Drugs.csv

Following the same principles as in the previous trials, we added the following variables:
- Reports of Violence
- Partner Abuse

After settling for these variables, we held no further debate to improve the model.

#### Classification Model
This model underperformed when compared to the previous. Nonetheless, the results were good enough to proceed with the trial.

|          Model       |   AUC   |    CA   |    F1   | Precision |  Recall |
| :------------------: | :-----: | :-----: | :-----: | :-------: | :-----: |
| Decision Tree        |  0.860  |  0.867  |  0.849  |   0.877   |  0.867  |
| Logistic Regression  |  0.667  |  0.817  |  0.787  |   0.811   |  0.817  |

The Decision Tree's ROC Curve (in green) delivered us from the fear of not achieving a satisfactory statistical foundation while being feasible within parameters discussed with our peers.

<img width="650" alt="roc-3" src="https://user-images.githubusercontent.com/54454569/169718566-1cb48a94-c637-4faa-9dd3-1989f336c334.png">

#### PCA
We opted for 98% of `Explained Variance`, which resulted in 9 components that we will further analyze and refer to as analysis inputs.

<img width="650" alt="pca-3" src="https://user-images.githubusercontent.com/54454569/169718571-bf1f6b69-6b55-4c4a-8818-87d270b5c221.png">

##### Confusion Matrix
Even though the confusion matrixes were far from excellent, they showed precision good enough to move on with this model without significant compromise.

######  Logistic Regression
|   0  |    0   |    1   |    Σ   |
| ---: | -----: | -----: | -----: |
|   0  | 87645  |  2616  | 90270  |
|   1  | 19057  |  9263  | 28320  |
|   Σ  | 106711 |  11879 | 118590 |

######  Decision Tree
|   0  |    0   |    1   |    Σ   |
| ---: | -----: | -----: | -----: |
|   0  | 89434  |   836  | 90270  |
|   1  | 14961  |  13359 | 28320  |
|   Σ  | 104395 |  14195 | 118590 |

#### Regression Model
The R2 results made us shiver, but debates with our peers showed commonality in finding it hard to achieve a model that could tick all the checkboxes in quality.

So we decided to stick to it since the process that led us here was enriching itself.

|          Model       |     MSE     |    RMSE  |   MAE    |  R2   |
| :------------------: | :---------: | :------: | :------: | :---: |
| Regression Tree      | 7936089.717 | 2817.107 | 1268.487 | 0.175 |
| Linear Regression    | 9273105.390 | 3045.177 | 1514.036 | 0.037 |

The Root Mean Square error for the Regression Tree model is within 7.8 years, which may be feasible for some health conditions. Even so, this result is not precisely reliable, as the following sections show.

In order to deeply understand how the small R2 influenced our model, we decided to compare the best and worst-performing components against each other:

##### Best-Performing Component (1st PCA Component)
<img width="1000" alt="bcs" src="https://user-images.githubusercontent.com/54454569/169719312-205eddec-8dc2-4e69-998f-41ea1c3f698a.png">


##### Worst-Performing Component (6th PCA component)
<img width="1000" alt="wcs" src="https://user-images.githubusercontent.com/54454569/169719327-907f0b89-1226-4d87-8733-d11ed5b06f7d.png">

As shown by the R2 metric, the variation between the best-performer and worst-performer is slight to none, and we were not able to find a correlation between those components and the target, which was prognostic of death.

The results, albeit unsatisfying, elicited a very complex decision-making process involving constant back-and-forth.

## Obtained Results
Attempting to mitigate overfitting made us approach those models incrementally, and even so, we could not reach meaningful results from cross-using the models.
The script that generates the tables with the variables used for each scenario can be found [here](https://github.com/FCollaPi/p2-datasci4health/blob/main/src/features/build_patients_drugs.py). It is worth to mention that the CSV paths saved are absolute, so it may be necessary to change the paths to the correct ones (that can also be found [here](https://github.com/FCollaPi/p2-datasci4health/blob/main/data/interim/scenario1/patient-drugs.csv) and [here](https://github.com/FCollaPi/p2-datasci4health/blob/main/data/interim/scenario2/patient-drugs.csv)) when reproducing the following tests.

### Training on Scenario 1, Testing on Scenario 2
We decided to report results segregated by classification and regression since each of those sessions could have its hindrances. [This Orange file](https://github.com/FCollaPi/p2-datasci4health/blob/main/notebooks/1.0-train-scenario1-test-scenario-2.ows) was used to train and test the mentioned scenarios.

#### Classification
The scoring below shows a slightly ok `Logistic Regression` AUC and a promising Classification Decision Tree AUC. However, that hope falls short since CDTs are not reliable as training models due to being very sensitive to data and tend to present higher variance.

|          Model               |  AUC  |   CA  |   F1  | Precision | Recall |
| :--------------------------: | :---: | :---: | :---: | :-------: | :----: |
| Logistic Regression          | 0.667 | 0.817 | 0.787 |   0.811   | 0.817  |
| Classification Decision Tree | 0.860 | 0.867 | 0.849 |   0.877   | 0.867  |

The `ROC Curves` confirms the previous table, with orange representing the LR and green the Decision Tree.

<img width="650" alt="class-g-roc" src="https://user-images.githubusercontent.com/54454569/170140564-d08b3f0c-a906-420f-931a-05ade1102b15.png">


##### Confusion Matrix
###### Logistic Regression

|   0  |    0   |    1   |    Σ   |
| :--: | :----: | :----: | :----: |
|   0  | 87654  |  2616  | 90270  |
|   1  | 19057  |  9263  | 28320  |
|   Σ  | 106711 |  11879 | 118590 |

###### Classification Decision Tree
|   0  |    0   |    1   |    Σ   |
| :--: | :----: | :----: | :----: |
|   0  | 89434  |  836   | 90270  |
|   1  | 14961  |  13359 | 28320  |
|   Σ  | 104395 |  14195 | 118590 |

##### Pythagoeran Tree
We opted for the `Pythagorean Tree` view for intelligibility and visualization purposes instead of the traditional tree view. Since the number of people labeled as dead is comprehensive low and our models are not very reliable, the tendency to more `alive` (0) nodes met expectations.

<img width="650" alt="class-g-pt" src="https://user-images.githubusercontent.com/54454569/170140607-e4694961-96dd-4f7b-9d06-76606488a0af.png">

##### Predictions
The `ROC Curve` of our `Classification Decision Tree` presented a 50/50 chance of getting it right, once again being close to a purely random classifier.

<img width="650" alt="class-pred-roc" src="https://user-images.githubusercontent.com/54454569/170140675-dd9d5827-2740-4bc1-a612-c4c63b83f5e8.png">


###### Classification Decision Tree
>TODO

|   0  |    0   |    1   |    Σ   |
| :--: | :----: | :----: | :----: |
|   0  | 11744  |   6016 | 47760  |
|   1  |   676  |    723 |  7449  |
|   Σ  | 48470  |   6739 | 55209  |

#### Regression
The low R2 scores once again confirm our model's untrustworthiness.

|            Model         |     MSE     |    RMSE  |   MAE    |  R2   |
| :----------------------: | :---------: | :------: | :------: | :---: |
| Regression Decision Tree | 7936089.717 | 2817.107 | 1268.487 | 0.175 |
| Linear Regression        | 9272105.390 | 2045.177 | 1514.036 | 0.037 |

We already know trees are less reliable, the difference in scores does not strike as a surprise, and we cannot infer much about it either.

This Scatter Plot's behavior and the Pythagorean Tree View are two strong indications of underscoring.

<img width="1000" alt="reg-scatter" src="https://user-images.githubusercontent.com/54454569/170140952-1dfb74ba-7016-43ab-80b1-63823ceece15.png">

<img width="650" alt="reg-pt" src="https://user-images.githubusercontent.com/54454569/170141488-83f4713d-f124-4bfd-8486-bb832c777566.png">


### Training on Scenario 2, Testing on Scenario 1
There is not loss in generalization from the last cross-use to this one. The file to reproduce this train and test set is [here](https://github.com/FCollaPi/p2-datasci4health/blob/main/notebooks/1.1-train-scenario2-test-scenario-1.ows). Results happened as already reported (and expected at this point).

#### Classification
|          Model               |  AUC  |   CA  |   F1  | Precision | Recall |
| :--------------------------: | :---: | :---: | :---: | :-------: | :----: |
| Logistic Regression          | 0.599 | 0.863 | 0.810 |   0.807   | 0.863  |
| Classification Decision Tree | 0.835 | 0.891 | 0.859 |   0.896   | 0.891  |

<img width="650" alt="class-g-roc" src="https://user-images.githubusercontent.com/54454569/170141020-6076e760-bc36-436d-a800-f8cb1ccbaa7c.png">

##### Confusion Matrix
###### Logistic Regression
|   0  |    0   |    1   |    Σ   |
| :--: | :----: | :----: | :----: |
|   0  | 94822  |  698   | 95520  |
|   1  | 14403  |  197   | 14900  |
|   Σ  | 107108 |  3312  | 110420 |

###### Classification Decision Tree
|   0  |    0   |    1   |    Σ   |
| :--: | :----: | :----: | :----: |
|   0  | 95297  |  223   | 95520  |
|   1  | 11811  |  3089  | 14900  |
|   Σ  | 107108 |  3312  | 110420 |

##### Pythagorean Tree
<img width="650" alt="class-g-pt" src="https://user-images.githubusercontent.com/54454569/170141047-1a2378de-1db8-4343-9c4f-4afea247fbb2.png">

##### Predictions
Our prediction for this cross-use actually underperformed the expected from a random generator.

<img width="650" alt="class-pred-roc" src="https://user-images.githubusercontent.com/54454569/170141086-516b8cf6-91c3-44ce-91df-937e7aac287e.png">

###### Classification Decision Tree
|   0  |    0   |    1   |    Σ   |
| :--: | :----: | :----: | :----: |
|   0  | 14364  |  769   | 45133  |
|   1  | 13922  |  239   | 14161  |
|   Σ  | 58286  |  1008  | 59294  |

#### Regression
|            Model         |     MSE     |    RMSE  |   MAE    |  R2   |
| :----------------------: | :---------: | :------: | :------: | :---: |
| Regression Decision Tree | 5963447.249 | 2442.017 | 882.248  | 0.134 |
| Linear Regression        | 6810200.055 | 2611.206 | 1062.678 | 0.010 |

<img width="1000" alt="reg-scatter" src="https://user-images.githubusercontent.com/54454569/170141180-38fd4c60-a720-41ee-a642-f614d46e228f.png">

<img width="650" alt="reg-pt" src="https://user-images.githubusercontent.com/54454569/170141207-09a06d61-1387-48cb-ba19-2bcab0f9c487.png">

## Discussion
As promising as the model looked, we cannot make further assumptions about its results.

Reasons could go from the sample size to the technical decision-making limitations regarding this domain. We found that intuitiveness does not always lead us to the right places when making sense of large chunks of data.

We are also aware that our approach could add noise to the whole process. So from one scenario standpoint, this trial-basis data gathering might not have been the best solution.

If we were to start over, we probably would have tested the model on several scenarios before settling on what we believed was the better model.

The differences in scenario data play a substantial role in providing outcomes we could assess.

We could not only understand more concepts like overfitting and the consequences of trying to deal with it, but we also could see in practical use the real-life applications of algorithms and how they perform differently.

In hindsight, we could draw a few significant conclusions from this whole process:
- it is very wholesome not to stress with dealing with data and with the modeling not meeting expectations;
- having the backup of a domain specialist plays a paramount role in assessing, developing, and validating a model;
- understanding the algorithms and their best use cases can help avoid biases, such as relying on decision trees.

## Conclusion
Although intense, this project allowed us to "go out on the wild" without leaving, quote-on-quote, the comfort of our fancy barn.

Making assumptions, taking risks of having to redo work, and making decisions are constantly enriching. We could align subjectiveness and technicity.

We also learned new concepts while revisiting subjects. Orange, markdown, and understanding the minutia of data analysis are the three more significant lessons we could list.

If time or concurrent workload were not such strong constraints, we could have visited the medical literature more often to find strong relations between subjects of our interest.

In that same fashion, we would have been more cautious when developing a scenario-based model to avoid scenario-biasing.

## References
- https://pubmed.ncbi.nlm.nih.gov/30914444/
- https://mecp.springeropen.com/articles/10.1186/s43045-021-00157-x
- https://www.nctsn.org/what-is-child-trauma/trauma-types/intimate-partner-violence
- https://pubmed.ncbi.nlm.nih.gov/15652265/
- https://www.apa.org/news/press/releases/2021/10/stress-pandemic-decision-making
- https://www.apa.org/news/press/releases/2021/10/stress-pandemic-decision-making
- https://www.mentalhealth.org.uk/a-to-z/s/stress
