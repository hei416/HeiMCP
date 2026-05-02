from fastmcp import FastMCP

# Import your independent modules
from src.code_review import evaluate_pr_logic
from src.unit_testing import evaluate_test_quality
from src.nn_architecture import check_architecture

# Initialize the MCP Server
mcp = FastMCP("StaffEngineerSkills")

@mcp.tool()
async def skill_code_review_logic(pr_description: str, code_diff: str) -> str:
    """
    Applies 'Drama-Free' Code Review rules. 
    Checks if context is provided and prepares the model to give feedback as questions.
    """
    return evaluate_pr_logic(pr_description, code_diff)

@mcp.tool()
async def skill_evaluate_unit_tests(test_code: str) -> str:
    """
    Evaluates unit tests based on the 'Right Way' principles:
    - Single Assertion
    - Testing Behavior vs Implementation
    - Simple Setup/Isolation
    """
    return evaluate_test_quality(test_code)

@mcp.tool()
async def skill_nn_architecture_check(layers_info: str) -> str:
    """
    [NOT YET FINISHED]
    Backlog: Automated shape verification for PyTorch deconv_blocks.
    """
    return check_architecture(layers_info)

if __name__ == "__main__":
    mcp.run()