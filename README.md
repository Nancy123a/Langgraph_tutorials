## **LangGraph Tutorials: Building Stateful, Multi-Tool AI Agents**

A comprehensive repository and tutorial series demonstrating the architecture of advanced AI agents using **LangGraph**, **LangChain**, and **Groq**. This project evolves a simple chatbot into a complex, multi-agent system capable of dynamic tool use, human collaboration, and persistence.

---

## 📂 **Project Structure & Key Features**

This repository is organized to showcase a progressive complexity of agent design, using high-speed LLM inference via **Groq** throughout.

| Folder | Core Functionality | Key Technologies / Concepts |
| :--- | :--- | :--- |
| **`BasicChatbot`** | **Foundational Agents & Tool-Use.** Builds a simple LLM wrapper, then integrates web search (`Tavily`) and custom tools (`multiply`) within a conditional graph. It also demonstrates **streaming** and **stateful memory** (`MemorySaver`). | **LangGraph Basics**, `ReAct` pattern, Tool Calling, Conversation History, Streaming, **Human-in-the-Loop** (`interrupt`). |
| **`Langgraph_tools`** | **Advanced Tool Use & Flow Control.** Likely focuses entirely on integrating different types of external APIs and functions into a robust decision-making loop. | **Conditional Edges**, **ToolNode**, Custom Tool Implementation. |
| **`Multiagent`** | **Cooperative AI Systems.** (Based on commit messages) Contains code for building a team of specialized agents (e.g., Researcher, Analyst, Writer) that collaborate on complex tasks. | **Multi-Agent Systems**, **CrewAI** or Custom Graph Structure, State Orchestration. |
| **`Pydantic`** | **Structured Output & Data Integrity.** Focuses on using Pydantic schemas to ensure agents return reliable, structured data for downstream tasks and tool calls. | **Pydantic Schemas**, Structured Output, Reliability in LLM-powered systems. |
| **`Debugging`** | **Monitoring and Traceability.** Contains code/setup for integrating an observability platform to debug and trace complex agent flows. | **LangSmith** or similar tracing tools, Monitoring Agent Performance. |

### **Why Use This Project?**

* **Progressive Learning:** Start with basic graph construction and build up to complex, multi-tool, and cooperative architectures.
* **Production Focus:** Features like **streaming**, **memory management**, and **structured output** are critical for production-ready applications.
* **Cutting-Edge Architecture:** Detailed implementation of the **ReAct** (Reasoning and Acting) pattern and **Human-in-the-Loop** workflows.
