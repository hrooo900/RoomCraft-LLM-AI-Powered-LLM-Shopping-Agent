################################### HELPING FUNCTIONS ########################

from hidden_file import tools
from MODEL import model


################################ Agent ####################################
# Memory
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
# Agent
from langgraph.prebuilt import create_react_agent
agent_executor = create_react_agent(model, tools, checkpointer=memory)