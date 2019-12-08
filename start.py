import requests
import json

from subprocess import call
from getJobs import GetJobs

call(["clear"])

print("this is")
print("JOBSEARCHBOT\n")

class MenuHandler: 

    def retrieveJobs(self):
        job_handler = GetJobs()
        self.jobs = job_handler.handle()

    def showJobs(self):
        print("Jobs to add:")
        
        for job in self.jobs:
            print("title: " + job['title'].lstrip())
            print("salary: " + job['salary'].lstrip())
            print("short_description: " + job['short_description'].lstrip() + "\n")  
       
    def saveJob(self):
        url = 'http://localhost/api/jobs'
        headers = {'Content-type': 'application/json'}
    
        for job in self.jobs:
            data = {}
            data['title'] = job['title']
            data['city'] = job['city']
            data['country'] = job['country'] 
            data['short_description'] = job['short_description']
            data['url'] = job['url']
            data['language'] = job['language']
            data['sector'] = job['sector']
            data['salary'] = job['salary'].lstrip() 
            data['description'] = str(job['description'])
            data['user_id'] = 1

            data_json = json.dumps(data)

            print(data_json)

            response = requests.post(url, headers=headers, data=data_json)
            print(response)

    def menu(self):
        print("\n")
        print("---Menu---")
        print("1: Save jobs")
        print("2: Write jobs to file")
        print("3: Show jobs")
        print("4: Load jobs")
        print("5: Exit")
        
        choice = input("What is your choice? ")
    
        if choice.strip() == "1":
            self.saveJob()
        elif choice.strip() == "2":
            print("You choose 2")
            print("This option is not working yet..")
            self.menu()
        elif choice.strip() == "3":
            print("You choose 3")
            self.showJobs()
            self.menu()
        elif choice.strip() == "4":
            self.retrieveJobs()
            print("You choose 4")
            print("Jobs loaded")
            self.menu()
        elif choice.strip() == "5":
            print("You choose 5")
            exit()
        else:
            print("\n")
            print(str(choice) + " Is not a valid choice. Try again, you can do it!")
            self.menu()

menu_handler = MenuHandler()
menu_handler.menu()