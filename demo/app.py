from flask import Flask , render_template,request,jsonify,session, redirect
from firebase import firebase


#   import run 

firebase = firebase.FirebaseApplication(
    'https://fit-game-92ad4.firebaseio.com/', None)

app = Flask(__name__)
app.debug = True
app.secret_key = "password"

@app.route('/')
def home():
    return render_template('index.html',check=check)

@app.route('/inf')
def inf():
    return render_template('systom.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    if "email" in session: 
        return render_template('dashboard/dashboard.html')
    return render_template('login.html')

@app.route('/check')
def check():
    return render_template('login.html')

@app.route('/map')
def map():
    if "email" in session : 
        return render_template('dashboard/map.html')
    else:
        return render_template('login.html')
@app.route('/dash')
def dash():
    if "email" in session : 
        value = 0
        games = 0
        val = firebase.get("/ethbalance",None)
        for i in val:
            if val[i]['email']==session['email']:
                value = val[i]['balance']
                games+=1

        return render_template('dashboard/dashboard.html',val=value,games=games)
    else: 
        return render_template("login.html")
@app.route('/update')
def update():
    if "email" in session : 
        return render_template('dashboard/user.html')
    else: return render_template('login.html')
@app.route('/register')
def register():

    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    if email and name and password :
        return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    email = request.form['email']
    name = request.form['name']

    if name and email :
        data = {'name':name,'email':email}
        output = "Result has been inserted"
        return jsonify({'name' : output})

    return jsonify({'error' : 'Missing data!'})

@app.route('/register_action',methods=['POST'])
def register_action():
    email = request.form['email']
    password = request.form['password']
    res = firebase.get('/login', None)
    for i in res:
        if res[i]['email'] == email:
            return "asd"
        else:
            print("record inserted")
            print(email)
            name = "anmol"
            firebase.post('/login', {'email':email,'name': name, 'pass': password})
            return "ads"


@app.route('/login_action',methods=['POST'])
def login_action():
    email = request.form['email']
    password = request.form['password']
    #print(email,password)
    res = firebase.get('/login', None)
    for i in res:
        if res[i]['email'] == email:
            if res[i]['pass'] == password:
                print("Session Started")
                session['email'] = email
                return "asd"   
    return "Works"

@app.route('/publickey',methods=['POST'])
def publickey():
    public = request.form['public']
    print(public, session['email'])
    firebase.post('/ethdata',{'email':session['email'], 'public_key':public})
    return "asda"



@app.route('/recipt',methods=['POST'])
def recipt():
    publicrec = request.form['rec']
    print(publicrec)
    firebase.post('/ethtransdata',{'email':session['email'], 'transaction_key':publicrec})
    return "asda"


@app.route('/route')
def route():
    return render_template('route.html')


@app.route('/route_process', methods=['POST'])
def route_process():
    distance = request.form['distance']
    latitude = request.form['lati']
    longitude = request.form['longi']
    print(distance,latitude,longitude)
    if distance:
        return jsonify({'distance': distance, 'latitude': latitude, 'longitude': longitude})
    else:
        return jsonify({'error': 'Please enter the  distance!'})


@app.route('/challyou', methods=['POST'])
def challyou():
    money = request.form['money']
    firebase.post('/chal_yourself', {'email':session['email'], 'value':money})
    print(money)
    return "asd"

@app.route('/frchall', methods=['POST'])
def frchall():
    gameId = request.form['gameid']
    firebase.post('/chal_friends', {'email':session['email'], 'gameId':gameId})
    print(gameId)
    return "123"

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'),404

if __name__ == "__main__":
	app.run()
