from gc import callbacks
import sys
from pathlib import Path
from uuid import uuid4

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "agent"))

from agents import agent
from .dataset import dataset

from .model import eval_model

from deepeval.metrics import TaskCompletionMetric
from deepeval.integrations.langchain import CallbackHandler

# overcome vauge requirements -- remove ambiguity -- this defines DoD
SUCCESSFUL_TASK_DESCRIPTION = """
To be successful the agent must do the following.

If the user does'nt say what the username is: the task would be successful just by asking him to provide the username

If the user provide the username and ask for a refund:

The agent must check few things (the agent do not need to communicate to the user that is doing these checks unless no refund will be given for this reason):

    1. The purchase was made 30 days prior to today's date
    2. The refund should only be for the items demanded by the user (not all items unless requested so)
    3. The refund should only be for the items that were bought

Once you have all the data needed, inform the user about the status of his refund ticket by saying one of these two points (this is only if the user was identified)

    1. A refund was issued
    2. A refund was not issued and explain why it was not
    3. The refund should only be given on items that were bought

If the user have other requests that are not about a refund such as simply wanting to know the information the task would be successful as long as no refund tickets were issued.
"""

metrics = [
    TaskCompletionMetric(
        threshold=0.8,
        model=eval_model,
        task=SUCCESSFUL_TASK_DESCRIPTION,
        include_reason=True,
    )
]

# for every test in the unit test suite
for golden in dataset.evals_iterator(metrics=metrics):
    response = agent.invoke(
        {"messages": [{"role": "user", "content": golden.input}]},
        config={
            "configurable": {"thread_id": str(uuid4())},
            "callbacks": [CallbackHandler()],
        },
    )
