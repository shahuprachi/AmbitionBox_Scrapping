import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ambitionbox.com/list-of-companies"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
companies = soup.find_all("div", class_="companyCardWrapper")

company_data = []

for i, company in enumerate(companies, start=1):
    name_tag = company.find("h2")
    salary_insigths_tag = company.find("div", class_="viewSalaryInsights")
    rating_tag = company.find("span", class_="companyCardWrapper__rating")
    if not rating_tag:
        rating_tag = company.find("div", class_="rating_text")

    name = name_tag.get_text(strip=True) if name_tag else "Not Available"
    salary_insigths_tag = salary_insigths_tag.get_text(strip=True) if salary_insigths_tag else "Not Available"
    rating = rating_tag.get_text(strip=True) if rating_tag else "Not Rated"

    print(f"🔹 {i}. {name}")
    print(f"   ⭐ Rating: {rating}")
    print(f"   📝 Description: {salary_insigths_tag}\n")

    company_data.append({
        "Company Name": name,
        "Rating": rating,
        "Description": salary_insigths_tag
    })
df = pd.DataFrame(company_data)
df.to_csv("ambitionbox_companies.csv", index=False)
print("✅ Data saved to 'ambitionbox_companies.csv'")
