from typing_extensions import TypedDict
from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from langgraph.graph import MessagesState, START, END

class AgentState(MessagesState):
    next: str


members = ["translator","summarize"]
options = members +["FINISH"]

class Router(TypedDict):
    next:Literal[*options]



system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    f" following workers: {members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH."
)

prompt = ChatPromptTemplate([
    ("system",system_prompt),
])

llm = ChatOpenAI(model="gpt-4o")

def supervisor(state:AgentState) -> AgentState:
    messages = prompt + state["messages"]
    print("messagesの内容は", messages)
    structured_llm = llm.with_structured_output(Router)
    res = prompt | structured_llm
    res.invoke(messages)
    next_ = res["next"]
    if next =="FINISHED":
        next_ = END

    return {"next": next_}