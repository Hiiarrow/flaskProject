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

    if mode == "hybrid":
        mst1 = float(request.form['mst1']) / 4
        mst2 = float(request.form['mst2']) / 4
        practical = float(request.form['practical']) / 2
        quiz = float(request.form['quiz']) / 2
        assignment = float(request.form['assignment']) / 2
        surprise = float(request.form['surprise']) / 3
        experiments = sum(float(request.form[f'exp{i}']) / 12 for i in range(1, 11))
        total = round(mst1 + mst2 + practical + quiz + assignment + surprise + experiments + attendance_bonus / 2, 2)
        return render_template("result.html", total=total, mode="Hybrid")

    elif mode == "theory":
        mst1 = float(request.form['mst1']) / 2
        mst2 = float(request.form['mst2']) / 2
        surprise = float(request.form['surprise']) / 3
        total = round(mst1 + mst2 + surprise + attendance_bonus / 2, 2)
        return render_template("result.html", total=total, mode="Theory")

    return "Invalid input"


if __name__ == "__main__":
    app.run()

