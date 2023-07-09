from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from third_parties.linkedin import scrape_linkedin_profile_direct

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    print("Hello LangChain!")
    
    # URL Finding Stage
    # Option 1: Pre-given URL
    my_linkedin_profile_url = "https://www.linkedin.com/in/jaysqvl/"

    # Option 2: Pre-given URL Cached JSON
    prescraped_gist_json = "https://gist.githubusercontent.com/jsqvl/9759002822158f1f2d787fd842d2d97e/raw/8f43b7cc1d4fc66ff804f437488503cf0876a773/jaysqvl.json"    

    # Option 3: Using an agent to find the URL for us
    found_linkedin_profile_url = linkedin_lookup_agent(name="Jay Esquivel Jr")

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # Scraping Stage (ONLY CHOOSE ONE NOT BOTH)
    # Option 1: Using ProxyCurl to get data given a url
    linkedin_data_found = scrape_linkedin_profile(linkedin_profile_url=my_linkedin_profile_url)

    # Option 2: Using a pre-saved JSON of a users linkedin page
    # linkedin_data_prescraped = scrape_linkedin_profile_direct(prescraped_gist_json)

    # Change based on the scraping stage
    print(chain.run(information=linkedin_data_found))
