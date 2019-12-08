from requests import get
from bs4 import BeautifulSoup
from extractJobInfo import JobInfoExtractor
import time

class GetJobs:
    is_posted_last_day_res = False

    def __init__(self):
        self.start = time.time()

    def timer(self, comment):
        end = time.time()
        print(comment + str(round(end - self.start, 4)))

    def isPostedLastDay(self, timeposted):
        if (len(timeposted) > 1):
            if (timeposted[1] == "minutes" or timeposted[1] == "hour" or timeposted[1] == "hours"):
                self.is_posted_last_day_res = True
            else:
                self.is_posted_last_day_res = False
        elif timeposted[0] == "yesterday":
            self.is_posted_last_day_res = True
        else:
            self.is_posted_last_day_res = False
        return self.is_posted_last_day_res

    def handle(self):
        self.timer("starting ")

        #Create a list with url for specific city's to loop over
        url_list = []

        url_berlin = 'https://www.toplanguagejobs.com/All-jobs-in-Germany?LocationId=51&TownOrCity=Berlin%2C%20Germany&search_location=Germany&GeoPlaceId=31000&DistanceMultiplier=0.62137&FullPlaceName=Berlin%2C%20Germany'
        url_amsterdam = 'https://www.toplanguagejobs.com/All-jobs-in-Netherlands?LocationId=52&TownOrCity=Amsterdam%2C%20Netherlands&search_location=Netherlands&FromMainSearchForm=true&GeoPlaceId=100433&DistanceMultiplier=0.62137&FullPlaceName=Amsterdam%2C%20Netherlands'
        url_prague = 'https://www.toplanguagejobs.com/All-jobs-in-Czech-Republic?LocationId=113&TownOrCity=Prague%2C%20Czech%20Republic&search_location=Czech-Republic&GeoPlaceId=30747&DistanceMultiplier=0.62137&FullPlaceName=Prague%2C%20Czech%20Republic'

        url_list.append(url_prague)
        url_list.append(url_berlin)
        url_list.append(url_amsterdam)

        list_all_jobs =[]
        for url in url_list:
            response = get(url)
            self.timer("retrieved url ")

            soup = BeautifulSoup(response.text, "html.parser")

            self.timer("Mapped all html with BeautifulSoup ")

            # First get a list of all urls and add the latest added jobs urls to a list
            jobitems = soup.find_all('div',{'class':'job-list-item'})
            self.timer("Retrieved jobitems and start to loop ")
            list_all_urls = []

            #Sometimes there are some priority advertisements with older dates on the top, we should then continue the loop
            priority_count = 2

            for jobitem in jobitems:
                item = jobitem.find('div',{'class':'posted-on'})
                posted_on = item.em.text.split(' ')
                if self.isPostedLastDay(posted_on) == False:
                    priority_count = priority_count = 1
                    if priority_count <= 0:
                        break
                    continue
                link = jobitem.find('a', href=True)
                complete_link = 'https://www.toplanguagejobs.com' + link['href']
                list_all_urls.append(complete_link)

            # Loop over all job urls and extract the right information    
            for item in list_all_urls:
                job_info_extractor = JobInfoExtractor(item)
                list_all_jobs.append(job_info_extractor.handle())
            
        return list_all_jobs











        
    
    


  
