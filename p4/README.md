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
- Visual Studio Code


## Data Prepare & Usage

### Normalization

Input images were normalized using a modified hyperbolic tangent normalizer. This operation's maximum and minimum values output could be 254 and 0, respectively.

After normalization, pixel values are converted back to 8-bit integers.

### Mask use

The masks available were presented as 16-bit PNG images.

After reading those, the pixel values equal to the maximum value obtained (254 across all masks) were treated as true mask pixels, and pixels equal to the minimum value (253) were treated as false mask pixels.

Then, the image was multiplicated by the resulting mask, from which the full lesion image was obtained.

### Black corners cropping

After the above, the full lesion images were cropped to reduce noise for the attribute selection. The region used for cropping was the inside of a rectangle defined by the minimum and maximum coordinates in which non-zero pixel values were present.

### Attribute extraction

Texture attributes were extracted from the cropped lesion images. Those were obtained from the Gray Level Co-occurrence Matrix (GLCM) and the histogram of those images.

### Attribute selection

After analysis of the data set, the Contrast attribute obtained from the GLCM and the histogram entropy were used as features from classification using a Support Vector Machine (SVM) classifier.


# Metodology


## Cross validation

Train/validation dataset split was applied using a Stratified 5-fold algorithm. The lesion class was used to stratify the samples, but took measures to keep MRI sections from the same patient together in the same split (i.e., training or validation set) so as not to bias the trained models.

## Evaluation metrics

The validation accuracy, balanced accuracy, the Area Under Curve (AUC) of the Receiver Operating Characteristic (ROC), and the Confusion Matrix were obtained from each split.

The metric used for selecting the best model was the balanced accuracy, which is a good measure for imbalanced datasets.


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

The best model considering our chosen metric was from split number 3, with approximately 67.48% balanced accuracy. The confusion matrix of that model is shown below.

<img src="https://github.com/FCollaPi/datasci4health/blob/6f8ab744e084c6ecd705ca18a1d1fd0ea6d0c056/p4/assets/cm.png?raw=true" alt="Confusion matrix of the best model trained" width=600/>

Ischemic stroke is named here as AVC after stroke initials in Portuguese. The same is done for multiple sclerosis (named EM).


# Obtained Results & Discussion

A dataset containing mask annotated lesions on brain FLAIR MRI slices of SLE patients was provided.

The model trained over ischemic stroke and multiple sclerosis MRIs was then used to classify those annotated slices according to the etiology of the annotated lesion (i.e. a classification as AVC would indicate ischemic etiology, and a classification as EM, demyelinating etiology).

Predicted labels were then renamed accordingly, and the result was saved in [here](https://github.com/FCollaPi/datasci4health/blob/582314cddb1588c0ffcdbea286064d45fc78c0e0/p4/data/processed/1.0-predicted.txt). The columns are patient ID, flair (slice) ID, and the predicted etiology (either `ischemic` or `demyelinating`).

Our model's predictions are a little above a random classifier and can not be used to make any deeper assumptions.

Albeit unsatisfying, our results were consistent in improvement over the last assignments, which shows us that, regarding due process, we could consolidate knowledge through the course of this subject and constantly enhance our ability to make decisions.


# Final Remarks

Cross-comparing our results to our peers showed how much each approach generates different outputs of performance and accuracy. Therefore, it was paramount to join forces in solving this project.

So, as for conclusions, understanding the value of working together to overcome challenges was a major one.

Feature engineering was also very intellectually defying, and the group debates came in hand so we could move forward in developing our solution.

Thinking outside the box and understanding the intersection between all the computing jobs and their health phenomena counterparts was critical to this assignment. Since we had no health consultant, we made assumptions primarily based on online literature to underpin technical choices.

More time in hand could provide opportunities to enhance our model's accuracy.

# References

- https://www.cdc.gov/lupus/facts/detailed.html
