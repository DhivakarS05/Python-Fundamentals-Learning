import time

n = int(input("Enter time in seconds: "))

for i in range(n,0,-1):
    seconds = i % 60
    minutes = int(i/60)%60
    hours = int(i/3600)
    print(f"{hours:02}.{minutes:02}.{seconds:02}")
    time.sleep(1)
print("Time is up")
