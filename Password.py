from flask import Flask, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    """Generate a random password with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""
    message = ""

    if request.method == 'POST':
        user_input = request.form.get('length', '')
        try:
            length = int(user_input)
            if length > 0:
                password = generate_password(length)
            else:
                message = "Please enter a number greater than 0."
        except ValueError:
            message = "Invalid input. Please enter a valid number."
    return f"""
        <html>
            <head>
                <title>Password Generator</title>
                <style>
                    body {{
                        text-align: center;
                        font-family: Calibri, sans-serif;
                        padding: 20px;
                        max-width: 500px;
                        margin: auto;
                        background-color: #f4f4f4;
                        content: center;
                    }}
                    h2 {{
                        color: #333;
                    }}
                    input, button {{
                        padding: 10px;
                        margin-top: 10px;
                        font-size: 16px;
                        color: green;
                    }}
                    p {{
                        font-weight: bold;
                        color: green;
                    }}
                    .error {{
                        color: red;
                    }}
                </style>
            </head>
            <body>
                <h2>Password Generator</h2>
                <form method="POST">
                    <label for="length">Enter password length:</label><br>
                    <input type="number" name="length" min="1" required><br>
                    <button type="submit">Generate</button>
                </form>
                {"<p>Your Password: " + password + "</p>" if password else "NO Password Generated"}
                {"<p class='error'>" + message + "</p>" if message else ""}
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
