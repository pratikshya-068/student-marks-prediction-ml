import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Create student data
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 25, 35, 45, 50, 60, 70, 85]
}

# Step 2: Convert data into a DataFrame
df = pd.DataFrame(data)

# Step 3: Select input and output
X = df[["Hours"]]
y = df["Marks"]

# Step 4: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Take input from the user
print("=" * 40)
print("     STUDENT MARKS PREDICTION")
print("=" * 40)

try:
    hours = float(input("Enter study hours (0 to 8): "))

    if 0 <= hours <= 8:
        # Step 6: Predict marks
        input_data = pd.DataFrame({"Hours": [hours]})
        prediction = model.predict(input_data)

        print(f"\nStudy Hours: {hours}")
        print(f"Predicted Marks: {prediction[0]:.2f} / 100")

    else:
        print("Please enter hours between 0 and 8.")

except ValueError:
    print("Invalid input! Please enter a number.")

print("\nThank you for using our project!")