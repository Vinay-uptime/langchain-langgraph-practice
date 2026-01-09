from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from pprint import pprint
# Create the LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    temperature = 0
)

response = llm.invoke(
 [HumanMessage(content="What's the capital of the Moon?")]
)

pprint(response)
print(response.content)

