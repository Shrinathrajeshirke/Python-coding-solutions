# Using ChainMap:

# Create a configuration system
# 3 levels: defaults, user_prefs, runtime
# Runtime overrides user, user overrides defaults
# Show which level provides each value

from collections import ChainMap

class ConfigSystem:
    def __init__(self):
        self.runtime = {}
        self.user = {}
        self.defaults = {}
        self.config = ChainMap(self.runtime, self.user, self.defaults)

    def set_default(self, key, value):
        self.defaults[key] = value

    def set_user(self, key, value):
        self.user[key] = value

    def set_runtime(self, key, value):
        self.runtime[key] = value

    def get(self, key):
        return self.config.get(key)
    
    def find_source(self, key):
        if key in self.runtime:
            return "runtime"
        elif key in self.runtime:
            return "user preference"
        elif key in self.defaults:
            return "defaults"
        else:
            return "Not found"
    
    def show(self):
        print('Output:')
        print('Configuration')

        for key in self.config:
            source = self.find_source(key)
            print(f"{key}: {self.config[key]} (from {source})")

        print("\nAll levels:")
        print(f"runtime: {self.runtime}")
        print(f"user: {self.user}")
        print(f"defaults: {self.defaults}")

config = ConfigSystem()
config.set_default("theme", "dark")
config.set_default("font_size", 14)
config.set_user("theme", "light")
config.set_runtime("font_size", 16)
config.show()
