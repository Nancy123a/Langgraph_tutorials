from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import END,START
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langchain_groq import ChatGroq
load_dotenv()

os.environ['LANGSMITH_PROJECT']="TestProject"
os.environ['GROQ_API_KEY']=os.environ['GROQ_API_KEY']
os.environ['LANGCHAIN_API_KEY']=os.environ['LANGCHAIN_API_KEY']
os.environ['LANGSMITH_TRACING']='true'

llm=ChatGroq(model='openai/gpt-oss-20b')

class State(TypedDict):
    ## messages have the type list. the add messages function in the annotation defines how this state key should be updated
    ## in this case it append message to the list instead of overwriting it
    messages:Annotated[list[BaseMessage],add_messages]

def make_tool_graph():
    ## Graph with tool call
    @tool
    def add(a:float,b:float):
        """
        Add two numbers
        """
        return a+b

    tool_list=[add]
    llm_with_tools=llm.bind_functions([add])

    def call_llm_model(state:State):
        return {'messages':[llm_with_tools.invoke(state['messages'])]}

    builder = StateGraph(State)
    builder.add_node('tool_calling_llm',call_llm_model)
    builder.add_node('tools',ToolNode(tool_list))

    builder.add_edge(START,'tool_calling_llm')
    builder.add_conditional_edges('tool_calling_llm',tools_condition,{True:'tools',False:END})
    builder.add_edge('tools','tool_calling_llm')

    graph=builder.compile()

    return graph


tool_agent=make_tool_graph()

