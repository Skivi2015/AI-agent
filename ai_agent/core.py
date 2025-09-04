class Agent:
    def __init__(self):
        self.plugins = []
        self.running = False

    def start(self, plugins):
        self.plugins = plugins
        self.running = True
        print("AI Agent started. Type 'quit' to exit.")
        
        while self.running:
            try:
                cmd = input(">>> ").strip()
                if cmd.lower() in ['quit', 'exit']:
                    self.running = False
                    print("Goodbye!")
                    break
                
                response = self.handle_command(cmd)
                print(response)
            except KeyboardInterrupt:
                self.running = False
                print("\nGoodbye!")
                break
            except EOFError:
                self.running = False
                print("\nGoodbye!")
                break

    def handle_command(self, cmd):
        if not cmd:
            return "Please enter a command."
        
        for plugin in self.plugins:
            if plugin.can_handle(cmd):
                return plugin.handle(cmd)
        
        return f"Command not recognized: {cmd}"