## I want a visualizer for arcprize.org problems

## Design

### HTML Files

**problems.html**

- Main page displaying a list of problems.
- Provides a button to create a new problem.
- Links to the details page for each problem.

**create_problem.html**

- Form for creating a new problem.
- Fields include problem name, description, and difficulty level.

**problem_details.html**

- Displays the details of a specific problem.
- Includes the problem name, description, difficulty level, and a visualization of the problem.

### Routes

**@app.route('/problems', methods=['GET', 'POST'])**

- GET: Renders the problems.html page with a list of all problems.
- POST: Processes the form data to create a new problem.

**@app.route('/create_problem', methods=['GET'])**

- GET: Renders the create_problem.html page for creating a new problem.

**@app.route('/problem/<int:problem_id>', methods=['GET'])**

- GET: Renders the problem_details.html page for a specific problem with the given ID.