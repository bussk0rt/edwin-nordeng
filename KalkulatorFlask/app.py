from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = float(request.form.get("num1"))
        operator = request.form.get("operator")
        num2 = float(request.form.get("num2"))

        if operator == "add":
            result = num1 + num2
        elif operator == "subtract":
            result = num1 - num2
        elif operator == "multiply":
            result = num1 * num2
        elif operator == "divide":
            result = num1 - num2

        return render_template("result", result=result)

    return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)