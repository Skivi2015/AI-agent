import sys
from ai_agent.core import Agent
from ai_agent.plugins_loader import load_plugins

def main():
    agent = Agent()
    plugins = load_plugins(agent)
    agent.start(plugins)

if __name__ == "__main__":
    main()
