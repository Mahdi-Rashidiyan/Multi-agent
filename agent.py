from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_ibm import WatsonXLLM
import os

os.environ["WATSONX_API_KEY"] = "your_api_key"
os.environ["SERPER_API_KEY"] = "your_api_key"

PARAMETERS = ("decoding_method":"greedy", "max_new_tokens":500)

#CREATE THE FIRST LLM
llm = WatsonXLLM(
    model_id="",
    url="",
    params="PARAMETERS",
    project_id="",
)

function_llm = WatsonXLLM(
    model_id="",
    url="",
    params="PARAMETERS",
    project_id="",
)
search = SerperDevTool()

researcher = Agent(
    llm=llm,
    function_calling_llm=function_llm,
    role="",
    goal="",
    backstory="",
    allow_delegation=False,
    tools=[search],
    verbose=1,
)

task1 = Task(
    description="",
    expected_output="",
    output_file="task1output.txt",
    agent="",
)

crew = Crew(
    agents=[researcher],
    tasks=[task1],
    verbose=1,
)


print(crew.kickoff())
