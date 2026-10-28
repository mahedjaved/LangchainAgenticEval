from models import model

from tools import *

from dotenv import load_dotenv

from langchain.agents import create_agent
from prompts import agent_system_prompt
from objects import Answer

from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage

from uuid import uuid4

# Load env vars
load_dotenv()

# Create the agent
agent = create_agent(
    model=model,
    system_prompt=agent_system_prompt,
    tools=[
        calculate_right_refund,
        get_user_purchase_history,
        get_today_date,
        issue_refund_ticket,
    ],
    response_format=Answer,
    checkpointer=InMemorySaver(),
)


def run_covnersation():
    config = {"configurable": {"thread_id": str(uuid4)}}
    question = HumanMessage(content="I would like to request a refund")
    conversation = True

    while conversation:
        response = agent.invoke({"messages": question}, config=config)
        structured_response = response["structured_response"]
        print(structured_response.answer)

        conversation = structured_response.conversation
        if conversation:
            user_input = input("reply: \n")
            question = HumanMessage(content=user_input)
    print(f"Ending conversation ...")


# run_covnersation()
