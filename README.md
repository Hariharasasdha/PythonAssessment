# Heart Disease Prediction Script - Machine Learning Integration 

## Purpose
This Python script aims to predict the presence of heart disease in individuals based on various health-related features. It utilizes the K-nearest neighbors (KNN) classification algorithm to make predictions.

## Dataset
The dataset used in this script is the "Heart Disease UCI" dataset, sourced from the UCI Machine Learning Repository. The dataset contains various attributes such as age, sex, chest pain type, resting blood pressure, cholesterol levels, and other health-related features. The target variable is binary, indicating the presence (1) or absence (0) of heart disease.

**Dataset Source:** [Heart Disease UCI](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)

## Script Overview
1. **Loading the Dataset:** The script loads the Heart Disease UCI dataset from a CSV file.

2. **Data Exploration:** Displays the shape of the dataset and the first few rows to provide an initial understanding.

3. **Data Preprocessing:** Separates the features (X) and the target variable (y) for model training.

4. **Train-Test Split:** The dataset is split into training and testing sets using the `train_test_split` function from scikit-learn.

5. **Model Selection:** The chosen model is the K-nearest neighbors classifier (`KNeighborsClassifier`), initialized with a specified number of neighbors (in this case, 3).

6. **Model Training:** The model is trained on the training set using the `fit` method.

7. **Prediction:** Predictions are made on the test set.

8. **Evaluation:** The script evaluates the model performance using accuracy and a classification report.



# Top Rated Tamil Movies - Web Scraping and Visualization

## Purpose
This Python script aims to scrape information about the top-rated Tamil movies from the Times of India website and visualize their ratings using matplotlib.

## Script Overview
1. **Web Scraping:** The script sends a GET request to the Times of India website's page for top-rated Tamil movies and uses BeautifulSoup to parse the HTML content.

2. **Data Extraction:** It extracts information about movie titles and ratings from specific HTML elements (divs with class "mr_lft_box").

3. **Data Visualization:** The script utilizes matplotlib to create a bar chart displaying the ratings of the top-rated Tamil movies.

4. **Display:** The resulting plot is displayed, showing the movie titles on the x-axis and their respective ratings on the y-axis.

## How to Use
To run the script, make sure you have Python installed along with the required libraries (pandas, scikit-learn,beautifulsoup4, requests, matplotlib). You can install the dependencies using the following command:

```bash
pip install beautifulsoup4 requests matplotlib pandas scikit-learn

python Web_Scraping.py
python Machine_Learning.py
