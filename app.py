from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    mode = request.form['mode']
    attendance = float(request.form['attendance'])
    attendance_bonus = 2 if attendance > 90 else 0

    if mode == "hybrid":
        mst1 = float(request.form['hybrid_mst1'])
        mst2 = float(request.form['hybrid_mst2'])
        practical = float(request.form['practical'])
        quiz = float(request.form['hybrid_quiz'])
        assignment = float(request.form['hybrid_assignment'])
        surprise = float(request.form['hybrid_surprise'])
        experiments = sum(float(request.form[f'exp{i}']) for i in range(1, 11))

        # Calculate total for hybrid mode
        total = round(mst1 / 4 + mst2 / 4 + practical / 2 + quiz / 2 + assignment / 2 + surprise / 3 + experiments / 12 + attendance_bonus / 2, 2)
        return render_template("result.html", total=total, mode="Hybrid")

    elif mode == "theory":
        mst1 = float(request.form['theory_mst1'])
        mst2 = float(request.form['theory_mst2'])
        quiz = float(request.form['theory_quiz'])
        assignment = float(request.form['theory_assignment'])
        surprise = float(request.form['theory_surprise'])

        # Calculate total for theory mode
        total = round(mst1 / 2 + mst2 / 2 + surprise / 3 + attendance_bonus + quiz + assignment, 2)
        return render_template("result.html", total=total, mode="Theory")

if __name__ == "__main__":
    app.run(debug=True)
