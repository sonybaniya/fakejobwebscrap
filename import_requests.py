import requests
from bs4 import BeautifulSoup as bs
import itertools


url="https://realpython.github.io/fake-jobs/"
html=requests.get(url)
s=bs(html.content,"html.parser")

results=s.find(id="ResultsContainer")
job_title=results.find_all("h2",class_="title is-5")
posted_by=results.find_all("h3",class_="subtitle is-6 company")
location=results.find_all("p",class_="location")
posted_on=results.find_all("time")

for(job,post,loc,time)in zip(job_title,posted_by,location,posted_on):
    print(f"job:{job.text}")
    print(f"company:{post.text}")
    print(f"location:{loc.text.strip()}")
    print(f"posted on{time.text}")
    print()
