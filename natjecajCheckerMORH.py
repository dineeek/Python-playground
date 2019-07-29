import requests
from bs4 import BeautifulSoup as BS
import re

def dohvatiStranicu():
    url = "https://www.morh.hr/kategorija/karijera-u-morh-u/natjecaji-i-oglasi/"
    link = requests.get(url)
    data = link.text
    content = BS(data, "html.parser")
    return content

def scrapSiteForJobs():
    siteContent = dohvatiStranicu()
    jobs = siteContent.find_all('a')
    allJobs = ','.join(str(v) for v in jobs).split("</a>")

    allJobsArray = []
    for job in allJobs:
        result = re.search('<a href="(.*)">', job) #re.search('title="(.*)">', job)
        if result is not None:
            allJobsArray.append(result.group(1))

    jobsForMe = []
    for job in allJobsArray:
        if job.__contains__("Javni natječaj za prijam kandidata/kandidatkinja za časnike/časnice"):
            job = job.replace('rel="bookmark" title=', "")
            jobsForMe.append(job)

    return  jobsForMe
def checkForJob():
    jobsFinded = scrapSiteForJobs()

    if len(jobsFinded) > 0:
        print("Pronađeni su natječaji:")
        for job in jobsFinded:
            print(job)


checkForJob()
