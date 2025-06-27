import logging
import os
from datetime import datetime
from typing import Annotated
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import create_react_agent
from typing_extensions import TypedDict

from .prompt import REALITY_CHECKPOINT_PROMPT

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class State(TypedDict):
    messages: Annotated[list, add_messages]

class RealityChecker:
    def __init__(
        self,
        model_name: str = "llama-3.3-70b-versatile",
        checkpointer: MemorySaver = None
    ):
        self.llm = ChatGroq(model=model_name, groq_api_key=os.getenv("GROQ_API_KEY"), max_tokens=12000)
        self.system_prompt = REALITY_CHECKPOINT_PROMPT.format(
            current_date=datetime.now().strftime("%Y-%m-%d")
        )
        self.checkpointer = checkpointer
        self.tavily_search_tool = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))

        self.tools = [self.tavily_search_tool]
   
    def build_graph(self):
        """Build and compile the graph"""
        graph_builder = StateGraph(State)

        react_agent =create_react_agent(
            model=self.llm.with_config({"tags": ["react_agent"]}),
            tools=self.tools,
            prompt=self.system_prompt,
        )

        graph_builder.add_node("react_agent", react_agent)
        graph_builder.add_edge(START, "react_agent")
        graph_builder.add_edge("react_agent", END)

        compiled_graph = graph_builder.compile(checkpointer=self.checkpointer)
        return compiled_graph
