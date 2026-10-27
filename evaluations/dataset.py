# Setup the test cases - convert golden to test cases
from deepeval.dataset import EvaluationDataset, Golden
from deepeval.test_case import ToolCall

# considers multiple scenarios and user journeys
dataset = EvaluationDataset(
    goldens=[
        Golden(
            input="I am user123, I would like a refund for the book",
            expected_output="A refund ticket for $37 has been issued successfully",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date"),
            ],
        ),
        Golden(
            input="I am user123, I would like no refund, I just want to know what I purchased",
            expected_output="No refund tickets were issued, only a list of what the user brought is returned",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
            ],
        ),
        Golden(
            input="I am user999, I would like a refund for the book",
            expected_output="Tell the user that the username is not valid and ask for username again before giving info about a refund",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
            ],
        ),
        Golden(
            input="I am user126, I would like a refund for the water bottle",
            expected_output="No refund given because it is outside of 30 day limit guideline",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="get_today_date"),
            ],
        ),
        Golden(
            input="I am user126, I would like a refund for the backpack and water bottle",
            expected_output="A refund ticket of $45 has been issued successfully only for the backpack. The water bottle is not eligible for a refund because it is outside of the 30 days refund policy",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date"),
            ],
        ),
        Golden(
            input="I am user126, I would like a refund for the sneakers",
            expected_output="No refund was given because the user has not purchased the item requested for refund",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="get_today_date"),
            ],
        ),
    ]
)
