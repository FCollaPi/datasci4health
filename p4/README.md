## Instruções para o Relatório Final

Segue abaixo o modelo de como deve ser documentada a entrega.
> Tudo o que aparece neste modo de citação, ou indicado entre `<...>`, se refere a algo que deve ser substituído pelo indicado. No modelo são colocados exemplos ilustrativos, que serão substituídos pelos do seu projeto.

Se o relatório for feito em um notebook, o modelo a seguir pode ser colocado dentro do notebook diretamente. Nesse caso, coloque no markdown do projeto (fora do notebook) uma cópia dos dados até a seção de `Apresentação` e um link para o notebook com o relatório.

# Classifying white matter lesions on lupus

We developed this project in the context of the graduate subject [Data Science and Visualization for Health](https://ds4h.org/) for the 2022.1 term at Unicamp.

|        Name       |       RA      |  Especialization  |
| :---------------: | ------------- | ----------------- | 
| Felipe Pinheiro   |     155298    | Computer Science  |
| Guilherme Jardim  |     203834    | Computer Science  |


# Intro

Lupus is an autoimmune disease in which the immune system attacks its own tissues, causing general inflammation and damage across all affected organs. Systemic Lupus Erythematosus (SLE) is the most common type of lupus, and its seriousness ranges from mild to life-threatening.

A team of doctors specialized in the care of SLE patients should provide preventive care and education since this disease has no cure. The causes of SLE are yet unknown but believed to be linked to genetic, hormonal, and environmental factors.

This project attempts to classify white matter lesions, whether they are ischemic or demyelinating, through the usage of trained AI models.

## Tools

- Jupyter Notebooks
- Google Colab


## Data Prepare & Usage

### Normalization

Input images were normalized using a modified hyperbolic tangent normalizer. The maximum and minimum values output from this operation could be 254 and 0, respectively. After normalization, pixel values are converted back to 8 bit integer.

### Mask use

Masks available were presented as 16 bit PNG images. After reading those, the pixel which values were equal to the maximum value obtained (which was 254 across all masks) were treated as true mask pixels, and pixels equal to the minimum value (253) were treated as false mask pixels. Then, the image was multiplicated by the resulting mask, from which the full lesion image was obtained.

### Black corners cropping

After the above, the full lesion images were cropped, so as to reduce noise for the attribute selection. The region used for cropping was the inside of a rectangle defined by the minimum and maximum coordinates in which non zero pixel values were present.

### Attribute extraction

Texture attributes were extracted from the cropped lesion images. Those were obtained from the Gray Level Co-ocurrence Matrix (GLCM) and the histogram of those images.

### Attribute selection

After analysis of the data set, the Contrast attribute obtained from the GLCM and the histogram entropy were used as features from classification using a Support Vector Machine (SVM) classifier.


# Metodology
> Descreva o classificador escolhido e o pipeline de treinamento:
> * split dos dados de treinamento
> * escolha de parâmetros do classificador
> * validação cruzada
> * métricas de avaliação
> * resultados do treinamento do classificador usando tabelas e gráficos
>
> Justificar as escolhas.
> Esta parte do relatório pode ser copiada da Atividade 11, caso o grupo opte por usar o SVM já treinado.

## Cross validation

Train/validation dataset split was applied using a Stratified 5-fold algorithm. The lesion class was used to stratify the samples, but took measures to keep MRI sections from the same patient together in the same split i.e. in training or validation set) so as not to bias the trained models.

## Evaluation metrics

From each split, the validation accuracy, balanced accuracy, the Area Under Curve (AUC) of the Receiver Operating Characteristic (ROC) and the Confusion Matrix were obtained. The metric used for selecting the best model was the balanced accuracy, which is a good measure for imbalanced datasets.

## Classification model

The classification model chosen was an SVM with sigmoid kernel and automatically scaled kernel coefficient `1 / (n_features * X.var())`, being `n_features` the number of features and `X.var()` the variation of each feature column.

## Training results

The evaluation metrics calculated with the validations sets for each split are shown below.

| Split |  ROC_AUC | Accuracy | Balanced Accuracy |
|------:|---------:|---------:|------------------:|
|     1 | 0.534066 | 0.747748 |          0.534066 |
|     2 | 0.461722 | 0.713178 |          0.461722 |
|     3 | 0.674779 | 0.821138 |          0.674779 |
|     4 | 0.451287 | 0.725664 |          0.451287 |
|     5 | 0.505545 | 0.738095 |          0.505545 |

The best model considering our chosen metric was from split number 3, with approximate 67.48% balanced accuracy. The confusion matrix of that model is shown below.

<img src="https://github.com/FCollaPi/datasci4health/blob/6f8ab744e084c6ecd705ca18a1d1fd0ea6d0c056/p4/assets/cm.png?raw=true" alt="Confusion matrix of the best model trained" width=900/>

Ischemic stroke is named here as AVC after stroke initials in Portuguese. The same is done for multiple sclerosis (named as EM).


# Obtained Results & Discussion

A dataset containing mask annotated lesions on brain FLAIR MRI slices of SLE patients was provided. The model trained over ischemic stroke and multiple sclerosis MRIs was then used to classify those annotated slices according to the etiology of the annotated lesion (i.e. a classification as AVC would indicate ischemic etiology, and a classification as EM, demyelinating etiology). Predicted labels were then renamed accordingly, and the result was saved in [here](https://github.com/FCollaPi/datasci4health/blob/582314cddb1588c0ffcdbea286064d45fc78c0e0/p4/data/processed/1.0-predicted.txt). The columsn are patient ID, flair (slice) ID, and the predicted etiology (either `ischemic` or `demyelinating`).


# Final Remarks

> Destacar as principais conclusões obtidas no desenvolvimento do projeto.
>
> Destacar os principais desafios enfrentados.
>
> Lessons Learned
>
> Future Works
> * o que poderia ser melhorado se houvesse mais tempo?

# References

- https://www.cdc.gov/lupus/facts/detailed.html