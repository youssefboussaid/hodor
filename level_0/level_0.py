#!/usr/bin/python3
import requests
vote = {
        "id" : "3280",
        "holdthedoor" : "submit"
        }
if __name__ == "__main__":
    for i in range(1024):
        requests.post("http://158.69.76.135/level0.php", data = vote)
