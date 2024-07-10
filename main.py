
# main.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

problems = []

@app.route('/problems', methods=['GET', 'POST'])
def problems():
    if request.method == 'POST':
        problem = request.form['problem']
        problems.append(problem)
        return redirect(url_for('problems'))
    return render_template('problems.html', problems=problems)

@app.route('/create_problem', methods=['GET'])
def create_problem():
    return render_template('create_problem.html')

@app.route('/problem/<int:problem_id>', methods=['GET'])
def problem_details(problem_id):
    problem = problems[problem_id]
    return render_template('problem_details.html', problem=problem)

if __name__ == '__main__':
    app.run(debug=True)
