from models.event import *



event1 = Event( "tomorrow", "Bonanza", 10, "room1", "BYOB", True)
event2 = Event( "day after tomorrow", "Boring Bash", 3, "Zoom", "online event", False)
events = [event1, event2]
        

def add_new_event(new_event):
    events.append(new_event)