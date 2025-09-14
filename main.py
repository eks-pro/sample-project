#!/usr/bin/env python3
"""
Sample Python application for demonstration purposes.
"""

def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to the sample project."

def main():
    """Main function."""
    print(greet("World"))
    print("This is a sample Python application.")
    print("Feel free to modify and extend it!")

if __name__ == "__main__":
    main()
