from flask import Flask,render_template
app = Flask(__name__)
def findaddress():
    phone_number="09083456788"
    emailaddress="df@gmail.com"
    comp="4 Ojo road Ogba,Lagos"
@app.route("/")
def home():
    return "welcome to my webpage"

@app.route("/vision")
def vision():
    name="John"
    email="abc@nbc.com"
    contact="404-111-8888"
    #return str(name),str(email),str(contact)
    return render_template('vision.html',name=name, email=email, contact=contact)


    
@app.route("/aboutUs")
def aboutUs():
    phone_number,emailaddress,comp=findaddress()
    return render_template('aboutUs.html',phoneno=phone_number, email=emailaddress, address=comp)
    
    return str(phone_number),str(emailaddress),str(comp)
@app.route("/services")
def services():
    service1="DevOps Cloud Development"
    service2="Netowrk Security"
    service3="Nework and application support"
    return render_template('services.html',service1=service1,service2=service2, service3=service3)

@app.route("/addition")
def addition():
    a=22
    b=4
    c=19
    total=a+b+c
    return "The sum of the numbers are: "+ str(total)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)