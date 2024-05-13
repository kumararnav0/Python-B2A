# Import required libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load data with error handling
data_path = "C:\\Users\\arnav\\Downloads\\Adjusted_Data_for_Predicting_with_Averages.csv"
try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    print(f"Error: The file at {data_path} was not found.")
    raise

# Define the feature names and target variable
features = ['avg_gdp_growth', 'avg_gdp_percapita', 'avg_net_migration', 'avg_crime_rate', 
            'avg_inflation_rate', 'avg_life_expectancy']
target = 'avg_students'

# Prepare the data
X = df[features]
y = df[target]

# Impute missing values for feature columns
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Handle missing values in the target variable
y_clean = y.dropna()
X_clean = X_imputed[~y.isna()]

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_clean)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y_clean, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict on the validation data
y_pred_lr = lr_model.predict(X_val)

# Calculate evaluation metrics for validation
mse_lr = mean_squared_error(y_val, y_pred_lr)
mae_lr = mean_absolute_error(y_val, y_pred_lr)
r2_lr = r2_score(y_val, y_pred_lr)

print(f"Linear Regression Validation Metrics:\nMSE: {mse_lr:.2f}\nMAE: {mae_lr:.2f}\nR²: {r2_lr:.2f}")

# Forecast for the next decade (2023-2032) using Linear Regression
years_ahead = 10
X_forecast = np.tile(np.mean(X_train, axis=0), (years_ahead, 1))
y_forecast_lr = lr_model.predict(X_forecast)
print("Linear Regression Forecast (2023-2032):", y_forecast_lr)

# Check stationarity of the target variable using the Augmented Dickey-Fuller test
adf_test = sm.tsa.adfuller(y_train)
print(f"\nADF Test Results:\nADF Statistic: {adf_test[0]:.4f}\np-value: {adf_test[1]:.4f}")
for key, value in adf_test[4].items():
    print(f"Critical Value ({key}): {value:.4f}")

# Initialize ARIMA model for time series forecasting
arima_model = ARIMA(y_train, order=(5, 1, 0))
arima_fit = arima_model.fit()

# Forecast with ARIMA for the next decade
forecast_results = arima_fit.get_forecast(steps=years_ahead)
y_forecast_arima = forecast_results.predicted_mean
conf_int = forecast_results.conf_int()

print("ARIMA Forecast (2023-2032):", y_forecast_arima)

# Create date ranges for visualization
actual_years = pd.date_range(start=2010, periods=len(y_clean), freq='YE')
future_years = pd.date_range(start=actual_years[-1] + pd.DateOffset(years=1), periods=years_ahead, freq='YE')

# Plot forecasts with labels and confidence intervals
plt.figure(figsize=(10, 6))
plt.plot(actual_years, y_clean, label='Actual', color='blue')
plt.plot(future_years, y_forecast_lr, label='LR Forecast', color='orange')
plt.plot(future_years, y_forecast_arima, label='ARIMA Forecast', color='green')
plt.fill_between(future_years, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='gray', alpha=0.2, label='ARIMA Conf. Interval')

plt.xlabel('Year')
plt.ylabel('Average Students')
plt.title('Forecasting Average Students for the Next Decade')
plt.legend()
plt.grid(True)
plt.show()
