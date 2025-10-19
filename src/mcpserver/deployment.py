from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers together
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtracts two numbers from each other
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiplies two numbers together
    """
    return a * b