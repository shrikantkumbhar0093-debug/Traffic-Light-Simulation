import time

# Simulate traffic light colors
colors = ['Red', 'Yellow', 'Green']
durations = [3, 1, 3]  # seconds

while True:
    for color, duration in zip(colors, durations):
        print(f"Traffic light: {color}")
        time.sleep(duration)