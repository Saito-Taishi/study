from typing import Annotated

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from .agent_supervisor import AgentState

llm =ChatOpenAI(model="gpt-4o-mini")
en_prompt = ChatPromptTemplate([
    ("system","英語に翻訳して下さい"),
    ("user","{user_input}")
])

sum_prompt = ChatPromptTemplate([
    ("system","英語で要約して下さい"),
    ("user","{user_input}")
])


def translate_node(state:AgentState):
    """英語ではない文章が来たときに、英語の翻訳を実行するために使う。"""
    try:
        en_chain = en_prompt | llm
        en_content = en_chain.invoke({"user_input":state["messages"]})
    except Exception as e:
        return f"Translation failed: {str(e)}"

    return en_content

def summarize_node():
    """英語の文章を要約する."""
    try:
        sum_chain = sum_prompt | llm
        sum_content = sum_chain.invoke({})
    except Exception as e:
        return f"summary failed :{str(e)}"

    return sum_content