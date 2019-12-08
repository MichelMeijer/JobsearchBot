from extractJobInfo import JobInfoExtractor

testurl = 'https://www.toplanguagejobs.com/Top-Language-Jobs/Customer-Service-Jobs/German-Speaking-Customer-Service-Fashion-related/Details/10116410'


job_info_extractor = JobInfoExtractor(testurl)
print(job_info_extractor.handle())