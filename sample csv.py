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
            reply_times.append(round(time_difference / 60)) #reply times in minutes instead of seconds - use round to get rid of decimals

    last_message_time[name] = time

#plot indexes
indices = np.arange(len(reply_times))

# Create the line plot
plt.plot(indices, reply_times, marker='o')
plt.title('A->B reply time')
plt.xlabel('Message Index')
plt.ylabel('Time Difference')
plt.grid(True)

plt.show()
