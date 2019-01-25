import subprocess
import csv

with open('topics.csv', 'r') as csvFile:
    topics = csv.reader(csvFile)

    for i in topics:
        subprocess.run(["python", "crawl_links.py", i[0]])



