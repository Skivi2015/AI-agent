"""
GitHub integration plugin for the AI Agent.
"""

import os
import requests
from typing import Optional, Dict, Any
from .plugins import BasePlugin


class GitHubPlugin(BasePlugin):
    """Plugin for GitHub API integration."""
    
    def __init__(self):
        super().__init__()
        self.github_token = None
        self.github_username = None
        self.github_repo = None
        self.base_url = "https://api.github.com"
        
    def initialize(self, agent):
        """Initialize the GitHub plugin with agent configuration."""
        super().initialize(agent)
        
        self.github_token = agent.config.get('github_token')
        self.github_username = agent.config.get('github_username')
        self.github_repo = agent.config.get('github_repo')
        
        if not self.github_token:
            self.logger.warning("No GitHub token provided. Set GITHUB_TOKEN environment variable.")
            return
            
        # Test GitHub connection
        self.test_connection()
        
    def test_connection(self) -> bool:
        """Test the GitHub API connection."""
        if not self.github_token:
            self.logger.error("Cannot test connection: No GitHub token")
            return False
            
        try:
            response = self.make_github_request("GET", "/user")
            if response and response.status_code == 200:
                user_data = response.json()
                self.logger.info(f"Connected to GitHub as: {user_data.get('login')}")
                
                # Store username if not provided
                if not self.github_username:
                    self.github_username = user_data.get('login')
                    
                return True
            else:
                self.logger.error(f"GitHub API test failed: {response.status_code if response else 'No response'}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error testing GitHub connection: {e}")
            return False
            
    def make_github_request(self, method: str, endpoint: str, data: Optional[Dict[Any, Any]] = None) -> Optional[requests.Response]:
        """Make a request to the GitHub API."""
        if not self.github_token:
            self.logger.error("Cannot make GitHub request: No token")
            return None
            
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'AI-Agent/0.1.0'
        }
        
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=headers, json=data)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                self.logger.error(f"Unsupported HTTP method: {method}")
                return None
                
            return response
            
        except Exception as e:
            self.logger.error(f"Error making GitHub request to {endpoint}: {e}")
            return None
            
    def get_user_repos(self) -> Optional[list]:
        """Get repositories for the authenticated user."""
        response = self.make_github_request("GET", "/user/repos")
        if response and response.status_code == 200:
            return response.json()
        return None
        
    def get_repo_info(self, owner: str, repo: str) -> Optional[dict]:
        """Get information about a specific repository."""
        response = self.make_github_request("GET", f"/repos/{owner}/{repo}")
        if response and response.status_code == 200:
            return response.json()
        return None
        
    def create_issue(self, owner: str, repo: str, title: str, body: str = "") -> Optional[dict]:
        """Create a new issue in a repository."""
        data = {
            "title": title,
            "body": body
        }
        
        response = self.make_github_request("POST", f"/repos/{owner}/{repo}/issues", data)
        if response and response.status_code == 201:
            return response.json()
        return None
        
    def start(self):
        """Start the GitHub plugin."""
        super().start()
        
        if self.github_token:
            self.logger.info("GitHub plugin ready for API calls")
            
            # Demonstrate some basic functionality
            self.demo_functionality()
        else:
            self.logger.warning("GitHub plugin started but no token available")
            
    def demo_functionality(self):
        """Demonstrate basic GitHub functionality."""
        try:
            # Get user info
            response = self.make_github_request("GET", "/user")
            if response and response.status_code == 200:
                user = response.json()
                self.logger.info(f"User: {user.get('name', 'N/A')} (@{user.get('login')})")
                self.logger.info(f"Public repos: {user.get('public_repos', 0)}")
                
            # Get some repositories
            repos = self.get_user_repos()
            if repos:
                self.logger.info(f"Found {len(repos)} repositories")
                for repo in repos[:3]:  # Show first 3 repos
                    self.logger.info(f"  - {repo['name']} ({repo['visibility']})")
                    
        except Exception as e:
            self.logger.error(f"Error in demo functionality: {e}")
            
    def stop(self):
        """Stop the GitHub plugin."""
        super().stop()
        self.logger.info("GitHub plugin stopped")