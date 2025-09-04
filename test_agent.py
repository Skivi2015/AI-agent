#!/usr/bin/env python3
"""
Simple test script to validate AI Agent functionality.
"""

import os
import sys
import tempfile
import subprocess

def test_basic_import():
    """Test that the package can be imported."""
    try:
        import ai_agent
        import ai_agent.core
        import ai_agent.plugins
        import ai_agent.github_plugin
        print("✓ All modules import successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_agent_creation():
    """Test that an Agent can be created."""
    try:
        from ai_agent.core import Agent
        agent = Agent()
        print("✓ Agent created successfully")
        return True
    except Exception as e:
        print(f"✗ Agent creation failed: {e}")
        return False

def test_plugin_loading():
    """Test that plugins can be loaded."""
    try:
        from ai_agent.core import Agent
        from ai_agent.plugins import load_plugins
        
        agent = Agent()
        plugins = load_plugins(agent)
        
        if plugins:
            print(f"✓ Loaded {len(plugins)} plugins")
            return True
        else:
            print("✗ No plugins loaded")
            return False
    except Exception as e:
        print(f"✗ Plugin loading failed: {e}")
        return False

def test_main_module():
    """Test that the main module can be run."""
    try:
        result = subprocess.run([
            sys.executable, '-m', 'ai_agent.main', '--help'
        ], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0 and 'AI Agent with GitHub Integration' in result.stdout:
            print("✓ Main module runs successfully")
            return True
        else:
            print(f"✗ Main module failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Main module test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("=== AI Agent Test Suite ===\n")
    
    tests = [
        test_basic_import,
        test_agent_creation,
        test_plugin_loading,
        test_main_module,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())