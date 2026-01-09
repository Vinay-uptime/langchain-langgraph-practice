from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from pprint import pprint
from langchain.messages import AIMessage
# Create the LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    temperature = 0
)
response = llm.invoke(
    [HumanMessage(content="What's the capital of the Moon?"),
    AIMessage(content="The capital of the Moon is Luna City."),
    HumanMessage(content="Interesting, tell me more about Luna City")]
)



pprint(response)
print(response.content)

