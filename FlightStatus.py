# Shows the flight status

#Shows flight status given two time slots.
def flight_status(scheduled_time, estimated_time):
    if (scheduled_time >= 25 or estimated_time >= 25) or (scheduled_time < 1 or estimated_time < 1):
        print ("please input a value between 01 and 24")
    elif scheduled_time == estimated_time:
        print ("on", "time")
    elif scheduled_time < estimated_time:
        print ("Delayed")
    elif scheduled_time > estimated_time:
        print ("Early")

#Shows flight status by taking datetime into consideration.
def flight_status_2(scheduled, estimated):
    if not isinstance(scheduled, datetime) or not isinstance(estimated, datetime):
        print("Enter a datetime")
        return
    if scheduled < estimated:
        print ("Delayed")
    elif estimated < scheduled:
        print ("Early")
    else:
        print ("On Time")
