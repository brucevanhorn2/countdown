import time
from sys import argv

def countdown(t: int, file_name: str):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        with open(file_name, 'w') as out:
            out.write(timeformat)
        #  print(timeformat)
        time.sleep(1)
        t -= 1
    print("Time's Up")


print("Running")
script, secs, file = argv
seconds = int(secs)
countdown(t=seconds, file_name=file)