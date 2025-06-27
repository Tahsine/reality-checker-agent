# reality-checker-agent

## **reality-checker-agent** is a modern conversational agent created with [LangGraph](https://www.langchain.com/langgraph), designed to answer your questions in real time through web search with [Tavily](https://www.tavily.com/). It is based on the latest LLM technologies and provides up-to-date, reliable and sourced answers.

## 🚀 Features

- Real-time web search (Tavily)
- Natural and up-to-date conversational responses
- Systematic source citations
- Modular and easily expandable

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/ton-utilisateur/reality-checker-agent.git
cd reality-checker-agent
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure your API keys**

Create an `.env` file at the root of the project (use `.env.example` as a guide):

```
GROQ_API_KEY=<secret_key>
TAVILY_API_KEY=<secret_key>
```

---

## 🧑‍💻 Quick Use (CLI)

Simply launch:

```bash
python main.py
```

### 🧠 Example interaction

```bash
> User: What's the latest news about SpaceX?

> Agent:
The latest news about SpaceX is that the company launched 27 Starlink satellites on a Falcon 9 rocket from Cape Canaveral Station in Florida. However, there was an incident during a ground test of the Starship rocket, which exploded during a series of preparatory tests for its tenth test flight. The explosion was confirmed by SpaceX, which assured that all safety protocols had been followed.

Source :
"Live coverage: SpaceX to launch 27 Starlink satellites on Falcon 9 rocket from Cape Canaveral - Spaceflight Now" - https://spaceflightnow.com/2025/06/25/live-coverage-spacex-to-launch-27-starlink-satellites-on-falcon-9-rocket-from-cape-canaveral-3/
"SpaceX traces Starship test-stand explosion to failure of pressurized nitrogen tank - Space" - https://www.space.com/space-exploration/launches-spacecraft/spacex-traces-starship-test-stand-explosion-to-failure-of-pressurized-nitrogen-tank
"SpaceX calls last minute abort of Starlink 10-23 due to signal issue - Spaceflight Now" - https://spaceflightnow.com/2025/06/21/live-coverage-spacex-to-launch-27-starlink-satellites-on-falcon-9-rocket-from-cape-canaveral-2/
"SpaceX launches 27 Starlink satellites from Florida (video) - Space" - https://www.space.com/space-exploration/launches-spacecraft/spacex-starlink-10-23-b1069-ccsfs-asog
"Spectacular explosion during SpaceX Starship test - Techno-Science.net" - https://www.techno-science.net/en/news/spectacular-explosion-during-spacex-starship-test-N27180.html

```

---

## 🛠️ Coming soon

- Telegram bot integration
- Discord bot integration
- Adding Wikipedia as a search source
- Simple web interface

---

**reality-checker-agent** — A simple, effective, and always up-to-date chatbot.
