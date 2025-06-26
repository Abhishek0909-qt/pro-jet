from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Define your own tasks list
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:  # Only add non-empty tasks
            tasks.append(task.strip())
        return redirect('/')

    return render_template('index.html', tasks=enumerate(tasks))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)