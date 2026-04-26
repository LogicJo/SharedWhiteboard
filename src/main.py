from flask import Flask, url_for, render_template, session, redirect, request
from flask_socketio import SocketIO
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "1610bffdafabbe5837d4b4fa53bc53def57afc7682ca2a4c7ee78898e85d168e"
socketio = SocketIO(app)

rooms = []

@app.route("/")
def index():
    if not session.get('name'):
        return redirect(url_for('login'))
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            room = form.room.data
            if form.join.data:
                pass
            if form.create.data:
                pass
            session['name'] = name
            session['room'] = room

    return render_template("login.html", form=form)