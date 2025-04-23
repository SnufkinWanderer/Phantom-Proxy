import time, random

def stealth_delay(min_delay=0.2, max_delay=0.7):
    time.sleep(random.uniform(min_delay, max_delay))

def log_request(msg):
    print(msg)
    with open("phantom.log", "a") as f:
        f.write(msg + "\n")