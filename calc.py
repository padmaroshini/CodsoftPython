from flask import Flask, request, render_template_string
app = Flask(__name__)

def calculate(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        if b != 0:
            return a / b
        else:
            return "Can't divide by zero"
    else:
        return "Invalid operation"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["operation"]
            result = calculate(a, b, op)
        except:
            result = "Enter valid numbers"

    return render_template_string("""
    <html>
    <head>
        <title>My Calculator</title>
        <style>
            body {
                font-family: sans-serif;
                background: #eee;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .box {
                background: white;
                padding: 20px;
                border-radius: 10px;
                width: 300px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            input, select, button {
                width: 100%;
                margin: 10px 0;
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                background: purple;
                color: white;
                border: none;
            }
            .res {
                margin-top: 15px;
                font-weight: bold;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2 style="text-align:center;">Calculator</h2>
            <form method="POST">
                <input type="number" name="a" placeholder="Enter number A" required>
                <input type="number" name="b" placeholder="Enter number B" required>
                <select name="operation">
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select>
                <button type="submit">Get Result</button>
            </form>
            {% if result != "" %}
                <div class="res">Result: {{ result }}</div>
            {% endif %}
        </div>
    </body>
    </html>
    """, result=result)

if __name__ == "__main__":
    app.run(debug=True)
