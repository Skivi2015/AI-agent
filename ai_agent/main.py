import sys
import argparse
from ai_agent.core import Agent
from ai_agent.plugins import load_plugins

def main():
    parser = argparse.ArgumentParser(description='AI Agent with GitHub Integration')
    parser.add_argument('--demo', action='store_true', help='Run GitHub integration demo')
    parser.add_argument('--test-connection', action='store_true', help='Test GitHub connection only')
    
    args = parser.parse_args()
    
    agent = Agent()
    plugins = load_plugins(agent)
    
    if args.test_connection:
        # Just test connection and exit
        github_plugin = next((p for p in plugins if p.__class__.__name__ == 'GitHubPlugin'), None)
        if github_plugin:
            github_plugin.initialize(agent)
            success = github_plugin.test_connection()
            sys.exit(0 if success else 1)
        else:
            print("GitHub plugin not found")
            sys.exit(1)
    
    agent.start(plugins)
    
    if args.demo:
        print("\n=== AI Agent GitHub Integration Demo ===")
        github_plugin = next((p for p in plugins if p.__class__.__name__ == 'GitHubPlugin'), None)
        if github_plugin and github_plugin.github_token:
            print("GitHub plugin is available and configured!")
            print("You can extend this agent to perform various GitHub operations.")
        else:
            print("GitHub plugin is not configured. Set GITHUB_TOKEN environment variable.")

if __name__ == "__main__":
    main()
