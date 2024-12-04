from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/',methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/products',methods=['GET'])
def products():
    return '<h1>This is Products Page............</h1>'

@app.route('/success/<int:score>',methods=['GET'])
def success(score):
    return '<h1>The person has passed and the score is '+ str(score)+"</h1>"

@app.route('/fail/<int:score>',methods=['GET'])
def failure(score):
    return '<h1>The person has Failed and the score is '+ str(score)+"</h1>"


@app.route('/forms',methods=['GET','POST'])
def forms():
    if request.method=='GET':
        return render_template('form.html')
    else:
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        english=float(request.form['english'])

        averageMarks=(science+maths+english)/3
        res=''
        if averageMarks>=50:
            res="success"
        else:
            res="failure"

        return redirect(url_for(res,score=averageMarks))
    # render_template('form.html',score=round(averageMarks))




if __name__=="__main__":
    app.run(debug=True)

