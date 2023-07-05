import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape infromation from LinkedIn Profiles,
    Mnaually scrape the information from the LinkedIn profile"""

    # what holds our JSON
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    pseudo_json_endpoint = "https://gist.githubusercontent.com/jsqvl/9759002822158f1f2d787fd842d2d97e/raw/8f43b7cc1d4fc66ff804f437488503cf0876a773/jaysqvl.json"

    header_dic = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, 
        params={"url": linkedin_profile_url}, 
        headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

def scrape_linkedin_profile_direct(linkedin_profile_url: str):
    response = requests.get(linkedin_profile_url)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
            
    return data