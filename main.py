import asyncio
# from src.devassist.server import DevAssistServer

from mcp.server.fastmcp import FastMCP

# Import actual tool logic functions
from src.devassist.tools.code_review import run_code_review
from src.devassist.tools.doc_generator import generate_documentation
from src.devassist.tools.test_generator import generate_test_cases
from src.devassist.tools.bug_analyzer import analyze_bug_report
from src.devassist.tools.api_docs import generate_api_docs

# Create an MCP server instance
mcp = FastMCP("devassist")

@mcp.tool()
def code_review(code: str, file_path: str = None) -> str:
    """Analyze code quality and suggest improvements"""
    return run_code_review(code, file_path)

@mcp.tool()
def generate_docs(project_path: str) -> str:
    """Auto-generate README files and project documentation"""
    return generate_documentation(project_path)

@mcp.tool()
def generate_tests(code: str, file_path: str = None) -> str:
    """Create comprehensive unit tests from code"""
    return generate_test_cases(code, file_path)

@mcp.tool()
def analyze_bug(report: str) -> str:
    """Categorize and prioritize bug reports"""
    return analyze_bug_report(report)

@mcp.tool()
def generate_api_docs(code: str, file_path: str = None) -> str:
    """Generate API documentation from code"""
    return generate_api_docs(code, file_path)

# Remove the old main function
# def main():
#     server = DevAssistServer()
#     asyncio.run(server.run())

# Start the MCP server
if __name__ == "__main__":
    print("Starting DevAssist MCP server...")
    mcp.run()
    print("DevAssist MCP server stopped.")
