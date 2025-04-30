from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
from flask import request, render_template

def safe_float(value, default=0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def result():
    mode = request.form.get('mode', '').lower()
    attendance = safe_float(request.form.get('attendance'))
    attendance_bonus = 2 if attendance > 90 else 0

    if mode == "hybrid":
        mst1 = safe_float(request.form.get('mst1')) / 4
        mst2 = safe_float(request.form.get('mst2')) / 4
        practical = safe_float(request.form.get('practical')) / 2
        quiz = safe_float(request.form.get('quiz')) / 2
        assignment = safe_float(request.form.get('assignment')) / 2
        surprise = safe_float(request.form.get('surprise')) / 3
        experiments = sum(safe_float(request.form.get(f'exp{i}')) / 12 for i in range(1, 11))
        total = round(mst1 + mst2 + practical + quiz + assignment + surprise + experiments + attendance_bonus / 2, 2)
        return render_template("result.html", total=total, mode="Hybrid")

    elif mode == "theory":
        mst1 = safe_float(request.form.get('mst1')) / 2
        mst2 = safe_float(request.form.get('mst2')) / 2
        quiz = safe_float(request.form.get('quiz'))
        assignment = safe_float(request.form.get('assignment'))
        surprise = safe_float(request.form.get('surprise')) / 3
        total = round(mst1 + mst2 + surprise + attendance_bonus + quiz + assignment, 2)
        return render_template("result.html", total=total, mode="Theory")

    else:
        return "Invalid mode selected", 400


if __name__ == "__main__":
    app.run()

