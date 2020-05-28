# Green Jobs Program Classification Prediction
Final Project Job Connector Data Science Bandung Batch 2 Purwadhika, Muhammad Zahid

> The Green Jobs - Green New York Program provides New Yorkers with access to energy assesments, installation services, low interest financing, and pathway to training for various green-collar careers

This dataset taken from kaggle [https://www.kaggle.com/new-york-state/nys-residential-homes-energy-efficiency-projects](https://www.kaggle.com/new-york-state/nys-residential-homes-energy-efficiency-projects). 

This dataset have 29 columns and 57924 rows of information. 


#### In this project, there are 3 steps that I did:
-    Data Cleaning (Handle Missing Value and Outlier)
-    Exploratory Data Analysis
-    Modelling Machine Learning Algorithm to Make Classification for Homeowner to either get the program or not, based on features that provide in this dataset


## Machine Learning Modelling
After missing value and multivariate outlier handled, then I have to select which columns to become a features in machine learning model using some statistical method, that is Chi-Squared testing.

These are the steps to produce Machine Learning Model that I use,
1. Feature Engineering
2. Scaling Data
3. Balancing Data with SMOTE
3. Cross Validation to avoid overfitting model
4. Selecting Best Model based on Cross Validation Score
5. Modelling with Default Parameter
6. HyperParameter Tuning with GridSearchCV Methods
5. Evaluation Model

Based on those steps, I use RandomForestClassifier after HyperParameter tuning for classification model to predict either homeowner received the program or no.

**Model evaluation result:** 
- Accuracy: 0.7154837036396645
- Precision: 0.9059472350573856
- Recall: 0.6955825131609064
- F1 Score: 0.7869489221208001
- AUC Score: 0.84

## Dashboard

I use Flask to create this dashboard. There are 5 pages:

**1. Home**

[![home.png](https://i.postimg.cc/8k0q68zt/home.png)](https://postimg.cc/Bt2hrVDK)

**2. Predict**

[![predict.png](https://i.postimg.cc/13Bx48nN/predict.png)](https://postimg.cc/bZZVBNRz)

**3. Result**

[![result.png](https://i.postimg.cc/NFD8Rv1b/result.png)](https://postimg.cc/fS30hFq0)

**4. Data Visualization**

[![visualization.png](https://i.postimg.cc/CMss3kWD/visualization.png)](https://postimg.cc/qggKnhBM)

**5. Sample Dataset**

[![dataset.png](https://i.postimg.cc/gJq3PbBd/dataset.png)](https://postimg.cc/xJ8XKh2F)









