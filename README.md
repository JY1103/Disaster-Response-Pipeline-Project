# Disaster-Response-Pipeline-Project
### 1. Installation
The program is running on python 3.6.5

### 2. Project Motivation
This code is for Data Engineering course of Data Scientist Nanodegree on Udacity. In this project, In this project, ETL, NLP and machine learning skills are applied to disaster data from [Figure Eight](https://www.figure-eight.com) to build a model for an API that classifies disaster messages.  A web app is built where an emergency worker can input a new message and get classification results in several categories. You can access the web in this [link](https://view6914b2f4-3001.udacity-student-workspaces.com).

### 3. File Description
**notebook**: includes python notebook for ETL and model training. </br>
**data**: The process_data.py contains code for ETL pipeline. The code does below steps:
* Loads data from disaster_categories.csv and disaster_messages.csv.
* Expands the category column so that each message category will take one column.
* Merges the category and message dataframes.
* Droppes any duplicates.
* Saves the cleaned data in a SQLite database.

**models**: The train_classifier.py contains code for model training. The code does below steps:
* Loads data from the SQLite database.
* Splits the dataset into training and test sets.
* Uses NLTK to tokenize and lemmanize raw message text, generate tf-idf for each message and uses scikit-learn's Pipeline to bulid machine learning pipeline.
* Trains and tunes a model using GridSearchCV.
* Outputs results on the test set.
* Exports the final model as classifier.pkl.

**app**:
* templates: htmls for generating web app
* run.py: 
  * Loads the data and loads the model saved before.
  * Prepares two visualizations (Distributions of Message Genres and Distributions of Message Categories)

### 4. How to Use
* Run the following commands in the project's root directory to set up the database and model.
  * To run ETL pipeline that cleans data and stores in database </br>
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
  * To run ML pipeline that trains classifier and saves </br>
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

* Run the following command in the app's directory to run web app. </br>
    `python run.py`
* Access the web app in this [link](https://view6914b2f4-3001.udacity-student-workspaces.com).
