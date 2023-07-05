from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from third_parties.linkedin import scrape_linkedin_profile_direct

if __name__ == '__main__':
    print("Hello LangChain!")

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template
        )
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    prescraped_gist_json = "https://gist.githubusercontent.com/jsqvl/9759002822158f1f2d787fd842d2d97e/raw/8f43b7cc1d4fc66ff804f437488503cf0876a773/jaysqvl.json"
    linkedin_data_prescraped = scrape_linkedin_profile_direct(prescraped_gist_json)

    print(chain.run(information=linkedin_data_prescraped))

    # my_linkedin_profile_url = "https://www.linkedin.com/in/jaysqvl/"
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url=my_linkedin_profile_url)
    # print(linkedin_data.json())