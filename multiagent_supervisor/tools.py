from typing import Annotated

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm =ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate([
    ("system","英語に翻訳して下さい"),
    ("user","{user_input}")
])


def translate_node():
    """英語ではない文章が来たときに、英語の翻訳を実行するために使う。"""
    try:
        en_chain = prompt | llm
        en_content = en_chain.invoke({"user_input":use_input})
    except Exception as e:
        return f"Translation failed: {str(e)}"

    return en_content

def summarize_node():
    """英語の文章を要約する."""    
    try:
        sum_chain = summary_prompt | llm
        sum_content = sum_chain.invoke({})