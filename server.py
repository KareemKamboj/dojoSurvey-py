from flask import render_template, request, session, redirect
from flask import Flask
app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def get_survey():
    return render_template("index.html")

@app.route('/info_page', methods=['POST'])
def info_page():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/info_page/info')

@app.route('/info_page/info')
def submitted_info():
    context = {
        'name': session['name'],
        'location':session['location'],
        'language':session['language'],
        'comments':session['comments']
    }
    
    return render_template('info.html', **context)


@app.route('/info_page')
def go_back():
    return render_template('/')

if __name__ =="__main__":
    app.run(debug=True)
    