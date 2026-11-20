from flask import Flask, render_template, request
from sklearn.tree import DecisionTreeClassifier
import numpy as np

app = Flask(__name__)

# Small illustrative training dataset: [marks percentage, attendance percentage, task score]
# Replace with an authorised real dataset for meaningful academic use.
X = np.array([
    [90, 95, 92], [82, 88, 85], [75, 80, 78], [68, 72, 70],
    [55, 65, 58], [48, 55, 50], [35, 45, 40], [25, 35, 30],
    [95, 90, 96], [78, 75, 80], [62, 68, 65], [42, 50, 45],
    [88, 82, 90], [58, 60, 62], [30, 40, 35], [70, 85, 74]
])
y = np.array([
    "Excellent", "Excellent", "Good", "Good",
    "Needs Improvement", "Needs Improvement", "At Risk", "At Risk",
    "Excellent", "Good", "Needs Improvement", "At Risk",
    "Excellent", "Needs Improvement", "At Risk", "Good"
])

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    values = {"marks": "", "attendance": "", "tasks": ""}
    error = None

    if request.method == "POST":
        try:
            values = {
                "marks": request.form.get("marks", "").strip(),
                "attendance": request.form.get("attendance", "").strip(),
                "tasks": request.form.get("tasks", "").strip()
            }
            marks = float(values["marks"])
            attendance = float(values["attendance"])
            tasks = float(values["tasks"])

            if not all(0 <= value <= 100 for value in [marks, attendance, tasks]):
                raise ValueError("Enter values between 0 and 100.")

            prediction = model.predict([[marks, attendance, tasks]])[0]
        except ValueError as exc:
            error = str(exc) or "Please enter valid numeric values."

    return render_template(
        "index.html", prediction=prediction, values=values, error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
