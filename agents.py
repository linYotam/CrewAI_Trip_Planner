import os
from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

# load_dotenv()
# os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
# os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

# sonnet = "claude-3-5-sonnet-20240620"


# """
# Creating Agents Cheat Sheet:
# - Think like a boss. Work backwards from the goal and think which employee 
#     you need to hire to get the job done.
# - Define the Captain of the crew who orient the other agents towards the goal. 
# - Define which experts the captain needs to communicate with and delegate tasks to.
#     Build a top down structure of the crew.

# Goal:
# - Create a 7-day travel itinerary with detailed per-day plans,
#     including budget, packing suggestions, and safety tips.

# Captain/Manager/Boss:
# - Expert Travel Agent

# Employees/Experts to hire:
# - City Selection Expert 
# - Local Tour Guide


# Notes:
# - Agents should be results driven and have a clear goal in mind
# - Role is their job title
# - Goals should actionable
# - Backstory should be their resume
# """

# # Set AWS profile
# os.environ["AWS_PROFILE"] = "yotamL"

# # Bedrock client
# bedrock_client = boto3.client(
#     service_name='bedrock-runtime',
#     region_name='us-east-1',
# )

# # Set model id from bedrock
# modelID = "anthropic.claude-3-sonnet-20240229-v1:0"

# # Create an instance of BedrockLLM
# llm = Bedrock(
#     credentials_profile_name="default", 
#     model_id=modelID
# )



class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
        # self.anthropic_llm = ChatAnthropic(temperature=0.7, model_name="claude-3-5-sonnet-20240620")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                f"""Expert in travel planning and logistics. 
                I have decades of expereince making travel iteneraries."""),
            goal=dedent(f"""
                        Create a 7-day travel itinerary with detailed per-day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, and traveler interests"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information
        about the city, it's attractions and customs"""),
            goal=dedent(
                f"""Provide the BEST insights about the selected city"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4,
        )