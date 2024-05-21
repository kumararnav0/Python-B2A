import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the adjusted dataset
data_path = "C:\\Users\\arnav\\Downloads\\Data_for_predicting - Sheet1.csv"
df = pd.read_csv(data_path)

# Specify features and target based on the adjusted dataset
features = ['Average_GDP_Growth', 'Average_Net_Migration', 'Average_Crime_Rate', 'Average_Inflation_Rate', 'Average_Life_Expectancy']
target = 'Average_Number_of_Students'

# Prepare the data
X_train = df[features]
y_train = df[target]

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and calculate errors
y_pred = model.predict(X_train)
mse = mean_squared_error(y_train, y_pred)

print("MSE:", mse)
