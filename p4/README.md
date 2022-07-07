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

## Avaliation metrics

From each split, the validation accuracy, balanced accuracy, the Area Under Curve (AUC) of the Receiver Operating Characteristic (ROC) and the Confusion Matrix were obtained. The metric used for selecting the best model was the balanced accuracy, which is a good measure for imbalanced datasets.

## Classification model

The classification model chose was an SVM with sigmoid kernel and kernel coefficient automatically scaled`1 / (n_features * X.var())`, being `n_features` the number of features and `X.var()` the variation of each feature column.


# Obtained Results & Discussion

> Esta seção deve apresentar o resultado de predição das lesões de LES usando o classificador treinado. Também deve tentar explicar quais os atributos relevantes usados na classificação obtida
> * apresente os resultados de forma quantitativa e qualitativa
> * tenha em mente que quem irá ler o relatório é uma equipe multidisciplinar. Descreva questões técnicas, mas também a intuição por trás delas.

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