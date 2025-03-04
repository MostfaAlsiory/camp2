from flask import Flask, render_template,request,jsonify
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
   
    return render_template('file.htm')





@app.route('/call')
def call():
   
    return render_template('call.html')




@app.route('/dark')
def park():
   
    return render_template('dark.html')



@app.route('/home2')
def home2():
   
    return render_template('home2.html')


@app.route('/car')
def car():
   
    return render_template('car.html')



@app.route('/clouth')
def clouth():
   
    return render_template('clouth.html')



@app.route('/leksan')
def leksan():
   
    return render_template('leksan.html')





@app.route('/swim')
def swim():
   
    return render_template('swim.html')



@app.route('/set1')
def set1():
   
    return render_template('set.html')


@app.route('/school')
def school():
   
    return render_template('school.html')


@app.route('/mosq')
def mosq():
   
    return render_template('mosq.html')












@app.route('/swater1')
def swater():
   
    return render_template('swater.html')



@app.route('/swater2')
def swater2():
   
    return render_template('swater2.html')



@app.route('/swater3')
def swater3():
   
    return render_template('swater3.html')



@app.route('/shop')
def shop():
   
    return render_template('shop.html')


@app.route('/bergoal')
def bergoal():
   
    return render_template('bergoal.html')


@app.route('/fix')
def fix():
   
    return render_template('fix.html')



if __name__ == '__main__':
    app.run(debug=True)




