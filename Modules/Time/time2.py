from datetime import datetime
import pytz

current_time=datetime.now(pytz.timezone('Asia/Kolkata'))

print("The current time in India is: ", end=" ")
print(current_time)