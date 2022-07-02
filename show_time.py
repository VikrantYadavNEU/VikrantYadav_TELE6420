from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S, %m/%d/%Y - %A")
print("Time =", current_time)