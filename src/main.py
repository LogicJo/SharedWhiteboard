from flask import Flask, url_for, render_template, session, redirect, request, flash, get_flashed_messages
from flask_socketio import SocketIO, join_room
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "1610bffdafabbe5837d4b4fa53bc53def57afc7682ca2a4c7ee78898e85d168e"
socketio = SocketIO(app)

rooms = []

@app.route("/")
def index():
    if not(session.get('name') and session.get('room')):
        return redirect(url_for('login'))
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            room = form.room.data
            if form.join.data:
                if not room in rooms:
                    error = "Room doesn't exist"
            if form.create.data:
                if room in rooms:
                    error = "Room already exists"
            if not error:
                session['name'] = name
                session['room'] = room
                return redirect(url_for('index'))
    return render_template("login.html", form=form, error=error)

@socketio.on('connect')
def connect(data):
    room = session['room']
    join_room(room)
    print(f"connected to room: {room}")