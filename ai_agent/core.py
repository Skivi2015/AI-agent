"""
Core Agent class for the AI Agent.
"""

import logging
import os


class Agent:
    """Main AI Agent class that manages plugins and GitHub integration."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_logging()
        self.config = self.load_config()
        self.plugins = []
        
    def setup_logging(self):
        """Setup basic logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
    def load_config(self):
        """Load configuration from environment variables."""
        # Try to load .env file if it exists
        self.load_env_file()
        
        config = {
            'github_token': os.getenv('GITHUB_TOKEN'),
            'github_username': os.getenv('GITHUB_USERNAME'),
            'github_repo': os.getenv('GITHUB_REPO'),
        }
        
        # Check for required config
        if not config['github_token']:
            self.logger.warning("GITHUB_TOKEN not set. GitHub functionality will be limited.")
            
        return config
        
    def load_env_file(self):
        """Load environment variables from .env file if it exists."""
        env_file = '.env'
        if os.path.exists(env_file):
            try:
                with open(env_file, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            key, value = line.split('=', 1)
                            os.environ[key.strip()] = value.strip()
                self.logger.info("Loaded environment variables from .env file")
            except Exception as e:
                self.logger.warning(f"Could not load .env file: {e}")
        
    def start(self, plugins=None):
        """Start the agent with loaded plugins."""
        self.logger.info("Starting AI Agent...")
        
        if plugins:
            self.plugins = plugins
            self.logger.info(f"Loaded {len(plugins)} plugins")
            
            # Initialize and start each plugin
            for plugin in plugins:
                try:
                    plugin.initialize(self)
                    plugin.start()
                except Exception as e:
                    self.logger.error(f"Error starting plugin {plugin.__class__.__name__}: {e}")
        else:
            self.logger.info("No plugins loaded")
            
        self.logger.info("AI Agent started successfully")
        
        # Basic GitHub integration test
        self.test_github_connection()
        
    def test_github_connection(self):
        """Test basic GitHub connection."""
        if self.config['github_token']:
            self.logger.info("GitHub token found - GitHub integration enabled")
            # TODO: Add actual GitHub API test here
        else:
            self.logger.warning("No GitHub token - please set GITHUB_TOKEN environment variable")
            
    def stop(self):
        """Stop the agent and all plugins."""
        self.logger.info("Stopping AI Agent...")
        
        for plugin in self.plugins:
            try:
                plugin.stop()
            except Exception as e:
                self.logger.error(f"Error stopping plugin {plugin.__class__.__name__}: {e}")
                
        self.logger.info("AI Agent stopped")