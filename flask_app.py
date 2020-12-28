from flask import Flask,render_template, request
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'Pawar2002Mayur'
@app.route('/',methods=['GET','POST'])
def index():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit:
        allValue = request.form
        name = allValue['name']
        email = allValue['email']
        subject = allValue['subject']
        message = allValue['message']
        print(allValue)
        print(name,email,subject,message)
        if name=='' or email=='' or subject=='' or message=='':
            return render_template('error.html',form=form)
        
        return render_template('thankYou.html',form = form)

    return render_template('index.html',form = form)

if __name__ == "__main__":
    app.run(debug = True)
