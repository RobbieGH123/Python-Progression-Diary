#import requests           # requests is a package, that allows us to browser search, from within Python
#import sys                # For using the command line argument vector function

#if len(sys.argv) != 2:    # If the only input is the file name, or there is more than one artist name
#    sys.exit              # Jum ship (exit the program)

#response = requests.get("https://apple.itunes.com/search?entity=song&limit=1&term=" + sys.argv[2]) # Response = Itunes search, 1 song, by artist typed on Command Line
 
#o = response.json()             # Store in Json format, otherwise it'll be something like <Response [200]> 
#for result in 0["results"]:     # 'results' is a nested dictionary within the answer
#    print(result["trackName"])  # Print each value from the Key: (trackName) - Which was seen when printing response.json() as the one containing a song

import random

results = {"Heads": 0, "Tails": 0}

for _ in range(20):
    flip = random.choice(["Heads", "Tails"])
    results[flip] += 1

print(results)
