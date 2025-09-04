import os
import importlib
import pkgutil


def load_plugins(agent):
    """Load all plugins from the plugins directory."""
    plugins = []
    
    # Create plugins directory if it doesn't exist
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    if not os.path.exists(plugins_dir):
        os.makedirs(plugins_dir)
        # Create __init__.py for plugins package
        init_file = os.path.join(plugins_dir, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write("")
    
    # Try to import plugins package
    try:
        plugins_package = importlib.import_module('ai_agent.plugins')
        
        # Load all plugin modules
        for importer, modname, ispkg in pkgutil.iter_modules(plugins_package.__path__, 
                                                            plugins_package.__name__ + "."):
            if not ispkg:  # Only load modules, not sub-packages
                try:
                    module = importlib.import_module(modname)
                    if hasattr(module, 'Plugin'):
                        plugin = module.Plugin(agent)
                        plugins.append(plugin)
                        print(f"Loaded plugin: {modname}")
                except Exception as e:
                    print(f"Error loading plugin {modname}: {e}")
    
    except ImportError:
        print("No plugins package found.")
    
    return plugins