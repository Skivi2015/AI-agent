"""
Plugin loading system for the AI Agent.
"""

import logging
import importlib
from typing import List, Any


class BasePlugin:
    """Base class for all AI Agent plugins."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.agent = None
        
    def initialize(self, agent):
        """Initialize the plugin with the agent instance."""
        self.agent = agent
        self.logger.info(f"Initializing {self.__class__.__name__} plugin")
        
    def start(self):
        """Start the plugin."""
        self.logger.info(f"Starting {self.__class__.__name__} plugin")
        
    def stop(self):
        """Stop the plugin."""
        self.logger.info(f"Stopping {self.__class__.__name__} plugin")


def load_plugins(agent) -> List[BasePlugin]:
    """Load all available plugins for the agent."""
    logger = logging.getLogger(__name__)
    plugins = []
    
    # List of available plugins
    plugin_modules = [
        'ai_agent.github_plugin',
    ]
    
    for module_name in plugin_modules:
        try:
            module = importlib.import_module(module_name)
            
            # Look for plugin classes in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, BasePlugin) and 
                    attr != BasePlugin):
                    
                    plugin_instance = attr()
                    plugins.append(plugin_instance)
                    logger.info(f"Loaded plugin: {attr_name}")
                    
        except ImportError as e:
            logger.warning(f"Could not load plugin module {module_name}: {e}")
        except Exception as e:
            logger.error(f"Error loading plugin from {module_name}: {e}")
            
    return plugins