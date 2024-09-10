from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample candidates
candidates = ['Alice', 'Bob', 'Charlie']
votes = {candidate: 0 for candidate in candidates}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_candidate = request.form.get('candidate')
        if selected_candidate in votes:
            votes[selected_candidate] += 1
            return redirect(url_for('result'))
    return render_template('vote.html', candidates=candidates)

@app.route('/result')
def result():
    return render_template('result.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
