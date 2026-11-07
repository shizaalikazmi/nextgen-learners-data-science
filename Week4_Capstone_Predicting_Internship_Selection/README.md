# Week 4 Capstone: Predicting Internship Selection Outcomes

A Machine Learning project that explores factors associated with internship selection outcomes using applicant data from the NextGenLearners Data Science Internship Program.

## 1. Project Objective

The objective of this project is to build a simple classification model that predicts whether an internship applicant will be Selected or Rejected.

The project combines data cleaning, exploratory analysis, feature preparation, machine learning, and model evaluation to demonstrate how predictive analytics can support recruitment-related decision-making.

## 2. Dataset Description

The original dataset contains **73 applicant records** with information such as:

- Applicant Name
- Email
- Phone
- Domain Applied
- University
- Application Date
- Selection Status

After excluding 34 applicants whose status was Under Review, **39 confirmed applicant records** were used for model training and testing.

The confirmed records include:
- 23 Selected applicants
- 16 Rejected applicants

### Additional Features

Four additional features were generated using NumPy for educational purposes:

1. Number of Skills Listed
2. Portfolio Availability
3. Previous Hackathon Participation
4. Statement Quality Score

**Important:** These four features are simulated and do not represent actual historical applicant information or behaviour. They were generated to demonstrate feature engineering and machine learning techniques.

## 3. Methodology

The project followed these main steps:

1. **Data Cleaning:** Prepared the applicant dataset by handling missing values, duplicates, and inconsistent records.
2. **Feature Engineering:** Generated four simulated applicant features.
3. **Feature Preparation:** Converted Yes/No values into numerical values, created the target variable, removed applicants with Under Review status, and applied One-Hot Encoding to application domains.
4. **Data Splitting:** Divided the confirmed dataset into 80% training data and 20% testing data.
5. **Model Training:** Trained a Logistic Regression classification model using Scikit-learn.
6. **Model Evaluation:** Evaluated predictions using accuracy, precision, recall, and a confusion matrix.
7. **Feature Interpretation:** Examined Logistic Regression coefficients to understand positive and negative associations between features and predicted selection outcomes.

## 4. Model Results

The Logistic Regression model was evaluated on 8 testing records.

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 62.50% |
| Precision | 66.67% |
| Recall | 80.00% |

### Results in Plain English

- **Accuracy (62.50%):** The model correctly predicted 5 out of 8 applicants.
- **Precision (66.67%):** Of the applicants predicted as Selected, approximately 67% were actually Selected.
- **Recall (80.00%):** The model correctly identified 80% of the applicants who were actually Selected.

The model showed positive associations with features such as Graphic Design domain and portfolio availability. However, these patterns should not be interpreted as actual recruitment criteria.

## 5. Limitations and Ethical Considerations

- The dataset is small, with only 39 confirmed applicant records.
- The testing set contains only 8 records, so evaluation metrics may change significantly with a different data split.
- Four features were artificially generated rather than collected from real applicants.
- The model may reflect or repeat biases present in historical selection decisions.
- The results are illustrative and do not guarantee real-world prediction performance.

This model should be treated as an educational decision-support demonstration, not as an automatic recruitment or rejection system. Final selection decisions must remain under human review.

## 6. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## 7. Project Files

The project folder contains:

- `Week4_Capstone_YourName.ipynb` — Complete project notebook and analysis.
- `applicants_cleaned.csv` — Cleaned applicant dataset used as the starting point.

## 8. How to Run the Project

You can run this project using Google Colab or Jupyter Notebook.

**Using Google Colab:**

1. Download the project notebook and `applicants_cleaned.csv`.
2. Open [Google Colab](https://colab.research.google.com/).
3. Upload the notebook.
4. Upload `applicants_cleaned.csv` to the Colab session.
5. Make sure the dataset is in the same working directory as the notebook.
6. Run all cells from top to bottom.

**Required Python Libraries:**

```python
pip install pandas numpy matplotlib scikit-learn
```

## 9. Recorded Project Walkthrough

A short video walkthrough explaining the project, methodology, results, and limitations:

**Video Link:** [Add Your Google Drive or YouTube Walkthrough Link Here]

## 10. Conclusion

This capstone demonstrates the application of basic machine learning techniques to an internship selection prediction problem.

It highlights the importance of data preparation, model evaluation, feature interpretation, and responsible use of predictive systems.

The project also demonstrates that trustworthy data science requires understanding not only model performance but also data limitations, fairness, and ethical considerations.
