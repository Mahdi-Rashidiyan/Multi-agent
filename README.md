# Multi-agent
Muti agent 
# CrewAI Project with IBM WatsonX

This project demonstrates the use of CrewAI framework integrated with IBM WatsonX for creating and orchestrating AI agents.

## Prerequisites

- Python 3.8 or higher
- IBM WatsonX API credentials
- Serper API key for search functionality

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install crewai crewai-tools langchain-ibm
```

## Configuration

Before running the project, you need to set up your API keys:

1. Set your IBM WatsonX API key:
```python
os.environ["WATSONX_API_KEY"] = "your_api_key"
```

2. Set your Serper API key:
```python
os.environ["SERPER_API_KEY"] = "your_api_key"
```

## Project Structure

- `agent.py`: Main script containing the CrewAI agent configuration and execution
- `task1output.txt`: Output file for the first task (generated during execution)

## Usage

1. Configure your IBM WatsonX model parameters in `agent.py`:
   - Set the `model_id`
   - Set the `url`
   - Set the `project_id`

2. Customize the agent and task configurations:
   - Define the agent's role, goal, and backstory
   - Configure the task description and expected output

3. Run the script:
```bash
python agent.py
```

## Features

- Integration with IBM WatsonX LLM
- Search capabilities using SerperDev
- Customizable agent roles and tasks
- Task output logging to files

## Dependencies

- crewai
- crewai-tools
- langchain-ibm
- os (built-in)

