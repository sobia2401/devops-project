
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Scholarship Eligibility Finder</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2ff;
            text-align: center;
            padding: 40px;
        }
        .box {
            background: white;
            padding: 25px;
            margin: auto;
            max-width: 400px;
            border-radius: 12px;
        }
        input, button {
            padding: 10px;
            margin: 10px;
            width: 85%;
        }
        button {
            background: #3157c8;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Scholarship Eligibility Finder</h2>
        <p>Enter your academic details</p>
        <form method="POST">
            <input type="number" name="marks"
                   placeholder="Marks percentage" min="0"
                   max="100" step="any" required>
            <input type="number" name="income"
                   placeholder="Annual family income (Rs.)"
                   min="0" required>
            <button type="submit">Check Eligibility</button>
        </form>
        <h3>{{ result }}</h3>
        <p>Sample criteria: Marks 75% or above
        and family income up to Rs. 300000.</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        marks = float(request.form["marks"])
        income = float(request.form["income"])

        if marks >= 75 and income <= 300000:
            result = "You are eligible for the sample scholarship!"
        else:
            result = "You are not eligible under the sample criteria."

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
