from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='path/to/templates')
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        tasks.append({'title': title, 'done': False})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    tasks[task_id]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
