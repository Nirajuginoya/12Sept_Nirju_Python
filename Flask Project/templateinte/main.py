from flask import Flask
from flask import render_template


app=Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def errorpage():
    return render_template('404.html')

@app.route('/blogsingle')
def blogsingle():
    return render_template('blogsingle.html')



if __name__=='__main__':
    app.run(debug=True)
    