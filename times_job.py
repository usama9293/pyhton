from bs4 import BeautifulSoup
import requests

print("print some skills that you are not faimar with")
unfaimlar_skill = input(">")
print(f"filtering out {unfaimlar_skill}")

def find_job():
    html = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    ).text
    soup = BeautifulSoup(html, "html.parser")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    with open('jobs.txt','w') as f:
        for index, job in enumerate(jobs):
            time = job.find("span", class_="sim-posted").text.replace(" ", "")
            if "few" in time:
                name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
                skills = job.find("span", class_="srp-skills").text.replace(" ", "")
                link = job.header.h2.a["href"]
                if unfaimlar_skill not in skills:
                    f.write(f"""
                    ---- Job {index + 1} ----
                    Company name: {name.strip()}
                    Required Skills: {skills.strip()}
                    More Info: {link}
                    \n""")  # Extra newline for separation between jobs

        print(f'All filtered jobs saved in jobs.txt')
                   
find_job()              
