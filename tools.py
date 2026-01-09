from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


@tool("square_root", description="Calculate the square root of a number")
def square_root(x: float) -> float:
    return x ** 0.5


result = square_root.invoke({"x": 467})
print("Square root of 467:", result)


llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    temperature=0
)


prompt = f"""
You are an arithmetic assistant.

The square root of 467 is {result}.
Explain this result in one sentence.
"""

response = llm.invoke(prompt)
print(response.content)


