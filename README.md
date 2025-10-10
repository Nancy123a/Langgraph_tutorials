# 🌟 LangGraph\_tutorials: Advanced AI Agent Architectures

A comprehensive repository and tutorial series demonstrating how to build **stateful, production-ready AI agents** using **LangGraph**, **LangChain**, and high-speed LLM inference via **Groq**.

This project provides step-by-step notebooks to evolve a simple LLM wrapper into a complex, multi-agent system capable of dynamic tool use, human collaboration, and persistent memory.

## 🚀 Key Features

This repository is structured for progressive learning, covering the full spectrum of modern agent development:

  * **⚡ High-Speed Inference:** All agents utilize **Groq** for lightning-fast, high-performance LLM responses.
  * **🧠 Stateful Memory & Persistence:** Implementation of conversation history and persistent state management using LangGraph's checkpointers.
  * **🛠️ Dynamic Tool Use (ReAct):** Demonstrations of the **Reasoning and Acting (ReAct)** pattern, allowing agents to decide when and how to use external tools (like web search and custom functions).
  * **👥 Multi-Agent Systems:** Creation of complex workflows where specialized agents cooperate to achieve sophisticated goals (e.g., automated research and analysis).
  * **🚶 Human-in-the-Loop:** Examples of implementing **interruptions** to allow for human feedback and decision-making within the agent's graph loop.
  * **📊 Structured Output:** Focus on ensuring agents return reliable data using **Pydantic schemas** for improved downstream processing.

-----

## 📂 Repository Structure

The project is broken down into modular folders, each focusing on a core agentic concept:

| Folder | Core Functionality | Key Concepts Demonstrated |
| :--- | :--- | :--- |
| **`BasicChatbot`** | **Foundational Agents & State Management.** Builds the initial graph, introduces LLM streaming, state update logic, and includes the **Human-in-the-Loop** pattern. | `StateGraph`, Streaming, `MemorySaver`, `interrupt` Command. |
| **`Langgraph_tools`** | **Dynamic Tool Calling.** Details the integration of multiple external capabilities, including **Tavily Search** for RAG/grounding and custom tools. | `ToolNode`, `tools_condition`, Tool Bindings. |
| **`Multiagent`** | **Cooperative AI Systems.** Focuses on orchestrating a **crew of specialized agents** (e.g., Researcher, Analyst, Writer) that pass state and information to solve complex queries. | Multi-Agent Orchestration, Conditional Routing, State Transitions. |
| **`Pydantic`** | **Reliable Output Generation.** Shows how to force the LLM to adhere to specific output formats using Pydantic, vital for reliable API interactions. | Pydantic Schema Enforcement, Type Safety. |
| **`Debugging`** | **Observability for Agents.** Includes setup and code snippets for integrating tracing and monitoring tools to debug complex graph execution paths. | **LangSmith** or equivalent Tracing Setup. |
| **`Langgraph_Basics`** | **Core Graph Primitives.** (Includes code from the notebooks) Essential tutorials on defining nodes, edges, state dictionaries, and compiling simple graphs. | `StateGraph`, `TypedDict`, `Annotated`, `START`/`END` Edges. |

-----

## ⚙️ Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd Langgraph_tutorials
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables:**
    Create a file named **`.env`** in the root directory and add your API keys:

    ```
    # Required for LLM inference
    GROQ_API_KEY="your-groq-api-key"

    # Required for web search tool
    TAVILY_API_KEY="your-tavily-api-key"
    ```
4.  **Run the Notebooks:**
    Navigate to the individual folders and open the `.ipynb` files to start exploring the agents\!
