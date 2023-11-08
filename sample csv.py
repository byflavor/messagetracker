from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# Define a dictionary to store the last message time for each person
last_message_time = {}

reply_times = []

csv_data = [
    "Alice,1:30",
    "Alice,1:31",
    "Alice,2:10",
    "Bob,2:15",
    "Bob,2:17",
    "Alice,8:05",
    "Bob,8:09",
    "Bob,8:10",
    "Alice,10:01"
]

for line in csv_data:
    name, time_str = line.split(',')
    time = datetime.strptime(time_str, "%H:%M")

    if name == 'Alice':
        alice_time = time
    else:
        if 'Alice' in last_message_time:
            time_difference = (time - last_message_time['Alice']).total_seconds()
            reply_times.append(time_difference)

    last_message_time[name] = time

#plot indexes
indices = np.arange(len(reply_times))

# Create the line plot - i dont know if this will work
plt.plot(indices, reply_times, marker='o')
plt.title('alice - bob reply time')
plt.xlabel('Message Index')
plt.ylabel('Time Difference (seconds)') #need to change to mins later
plt.grid(True)

plt.show()
