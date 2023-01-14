from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

@app.route("/")
def index():
    return render_template("expense_tracker.html", expenses=expenses)

@app.route("/add_expense", methods=["POST"])
def add_expense():
    amount = request.form.get("amount")
    category = request.form.get("category")
    date = request.form.get("date")
    expenses.append({'amount': amount, 'category': category, 'date': date})
    return redirect("/")

@app.route("/total_expenses")
def total_expenses():
    total = 0
    for expense in expenses:
        total += expense['amount']
    return str(total)

@app.route("/expenses_by_category/<category>")
def expenses_by_category(category):
    total = 0
    for expense in expenses:
        if expense['category'] == category:
            total += expense['amount']
    return str(total)

if __name__ == "__main__":
    app.run(debug=True)