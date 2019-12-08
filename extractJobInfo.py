from requests import get
from bs4 import BeautifulSoup

class JobInfoExtractor:
    
    def __init__(self, url):
        self.url = url

    def prepareData(self):
        response = get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        self.jobinfo = soup.find('div',{'id':'content-container'})
        self.content = self.jobinfo.find('div',{'class':'container'})

    def getTitle(self):
        title = self.content.find('a',{'href': "#"}).findNext('span').text
        title = title.split('-')      
        return title[0]
    
    def getCity(self):
        city = self.content.find('strong', text = "Location").findNext('div').text
        city = city.split(',')
        return city[0]
    
    def getCountry(self):
        location = self.content.find('strong', text = "Location").findNext('div').text
        country_list = location.split(',')
        country = "Unknown"

        for item in country_list:
            if (item.strip() == "Netherlands"):
                country = item
            elif (item.strip() == "Germany"):
                country = item
            elif (item.strip() == "Czech Republic"):
                country = item

        return country

    def getJobDescription(self):
        description = self.content.find('div',{'class':'job-description'})
       
        return description

    def getShortDescription(self):
        short_description = self.description.text[:200]
        short_description = short_description.split('.')
        return short_description[0]

    def getLanguage(self):
        general_info = self.content.find('a',{'href': "#"})
        language_list = general_info.text.split(' ')

        language = "unknown"

        for item in language_list:
            if (item.strip() == "German"):
                language = item
            elif (item.strip() == "Finnish"):
                language = item
            elif (item.strip() == "Danish"):
                language = item
            elif (item.strip() == "Dutch"):
                language = item

        return language

    def getSalary(self):
        salary = self.content.find('strong', text = "Salary/Rate").findNext('div').text
        salary = salary.split('\n')
             
        for item in salary:
            if item:
                salary = item
                break
        
        if salary == "salary not specified":
            salary = "not specified" 
        
        if salary == "Up to £1 per annum":
            salary = "not specified" 

        return salary

    def extractData(self):
        self.title = self.getTitle()
        self.city = self.getCity()
        self.country = self.getCountry().strip()
        self.description = self.getJobDescription()
        self.short_description = self.getShortDescription()
        self.language = self.getLanguage()
        self.salary = self.getSalary()
        self.sector = "Unknown"

    def createKeyPairObject(self):
        job_object = {
            "title" :self.title,
            "salary" : self.salary,
            "short_description" : self.short_description,
            "city" : self.city,
            "sector" : self.sector,
            "country" : self.country,
            "language" : self.language,
            "description" : self.description,
            "url" : self.url
        }
        return job_object

        
    def handle(self):
        self.prepareData()
        self.extractData()

        return self.createKeyPairObject()
