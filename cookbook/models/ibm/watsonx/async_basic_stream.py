import asyncio

from agno.agent import Agent, RunResponseEvent  # noqa
from agno.models.ibm import WatsonX

agent = Agent(
    model=WatsonX(id="ibm/granite-20b-code-instruct"), debug_mode=True, markdown=True
)

# Get the response in a variable
# run_response: Iterator[RunResponseEvent] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
