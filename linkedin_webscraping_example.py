import requests, pandas
from bs4 import BeautifulSoup


r = requests.get("https://www.linkedin.com/jobs/search?keywords=Software Engineer&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("li", {"class": "job-result-card"})

count = 1

for item in all:
    content = item.find("div", {"class": "result-card__contents"})
    jobId = item['data-id']     
    link = "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position="+ str(count) +"&pageNum=0&currentJobId="+ str(jobId)
    job_name = content.find("h3", {"class": "job-result-card__title"}).text
    enterprise_name = content.find("a", {"class": "job-result-card__subtitle-link"}).text
    location = content.find("span", {"class": "job-result-card__location"}).text
    try:
        open_since = content.find("time", {"class": "job-result-card__listdate--new"}).text
    except:
        try:
            open_since = content.find("time", {"class": "job-result-card__listdate"}).text
        except:
            open_since = "Now"
    
    print("Job Id: %s" % str(jobId))
    print("Job: %s" % job_name)
    print("Enterprise: %s" % enterprise_name)
    print("Location: %s" % location)
    print("Open since: %s" % open_since)
    print("For more info go to: %s" % link)
    print()
    count+=1
    
    
    
    

