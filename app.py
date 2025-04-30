from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    mode = request.form['mode']
    attendance = float(request.form['attendance'])
    attendance_bonus = 2 if attendance > 90 else 0

    # Normalize the attendance bonus (since it can be either 2 or 0)
    normalized_attendance = attendance_bonus / 2

    if mode == "hybrid":
        # Normalize the Hybrid Mode Inputs
        mst1 = float(request.form['mst1']) / 4
        mst2 = float(request.form['mst2']) / 4
        practical = float(request.form['practical']) / 2
        quiz = float(request.form['quiz']) / 2  # Add this field
        assignment = float(request.form['assignment']) / 2  # Add this field
        surprise = float(request.form['surprise']) / 6

        # Normalize Experiment Marks (assuming there are 10 experiments)
        experiments = sum(float(request.form[f'exp{i}']) / 12 for i in range(1, 11))

        # Calculate the Total for Hybrid Mode
        total = round(mst1 + mst2 + practical + quiz + assignment + surprise + experiments + normalized_attendance, 2)

        return render_template("result.html", total=total, mode="Hybrid")

    elif mode == "theory":
        # Normalize the Theory Mode Inputs
        mst1 = float(request.form['t_mst1']) / 2
        mst2 = float(request.form['t_mst2']) / 2
        quiz = float(request.form['t_quiz'])
        assignment = float(request.form['t_assignment'])
        surprise = float(request.form['t_surprise']) / 3

        # Calculate the Total for Theory Mode
        total = round(mst1 + mst2 + quiz + assignment + surprise + normalized_attendance, 2)

        return render_template("result.html", total=total, mode="Theory")

    return "Invalid input"


if __name__ == "__main__":
    app.run(debug=True)
