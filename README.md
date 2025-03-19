# Solar-output-prediction-using-machine-learning
by Pranav Jain graduate from Indian Institute of Technology(BHU) Varanasi.
This is our final year project.

Language:Python

Goal:Predicting solar panel output power using time-series weather data with machine learning models for efficient energy management.

This project can be divided into  parts:
1. Data Pre-processing: We processed the raw weather data files(input) form the National Oceanographic and Atmospheric Administration and the power production data files(output) from Urbana-Champaign solar farm to get meaningful numeric values on an hourly basis.
2. Feature Selection: We run correlation analysis between the weather features and energy output to discard useless features, we also implemented Principal Component Analysis to reduce the dimension of out dataset.
3. Machine Learning Models: We compared the performance of diffferent ML algorithms. Implemented models include weighted Linear Regression with and without dimension reduction, Boosting Gradient Boosting, and Artificial Neural Networks with and without vanishing temporal gradient.
4. Accuracy: We used various metrics score to analyse the perfomance of our models.

