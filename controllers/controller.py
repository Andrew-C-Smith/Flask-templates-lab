from flask import render_template,request
from app import app
from models.event_list import add_new_event, events 
from models.event import Event

@app.route('/')
def home():
    return "home"


@app.route('/getevents')
def index():
    return render_template('index.html',title='events', events=events)

@app.route('/addevents',methods=['POST'])
def add_events():
    print(request.form)   #will print to terminal -server- the post return
    date = request.form["dates"]
    name_of_event = request.form["name_of_event"]
    num_of_guests = request.form["num_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    recurring = request.form["recurring"]
    new_event = Event(date, name_of_event, num_of_guests, room_location, description, recurring )
    add_new_event(new_event)   #imported from models
    print(name_of_event)
    # print(task_title)
    # print(task_description)
    return render_template('index.html',title='home',events=events) #renders return on index page

# @app.route('/events/delete/<index>,methods=['POST'])
# def delete_event():
#     print(request.form
#     name_of_event = request.form["name_of_event"]
#     return render_template('index.html',title='home',events=events)