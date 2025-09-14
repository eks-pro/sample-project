# Sample Project - Python Development Guide

This is a comprehensive sample repository created for demonstration purposes with detailed instructions for Python development.

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Creating New Python Files](#creating-new-python-files)
- [Updating Python Files](#updating-python-files)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Best Practices](#best-practices)
- [Testing](#testing)
- [Contributing](#contributing)

## 🔍 Overview

This repository serves as a learning resource and template for Python development. It includes examples, best practices, and step-by-step guides for creating and managing Python projects.

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+**: Download from [python.org](https://www.python.org/downloads/)
- **Git**: Download from [git-scm.com](https://git-scm.com/)
- **Text Editor/IDE**: Such as VS Code, PyCharm, or Sublime Text

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/eks-pro/sample-project.git
cd sample-project
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Run the Sample Application

```bash
python app.py
```

## 📝 Creating New Python Files

### Step 1: Plan Your File Structure

Organize your files logically:
```
sample-project/
├── src/                 # Source code
├── tests/               # Test files
├── docs/                # Documentation
├── scripts/             # Utility scripts
└── examples/            # Example files
```

### Step 2: Create a New Python File

#### Method 1: Using Command Line
```bash
# Create a new Python file
touch calculator.py

# Or create with initial content
echo "# Calculator Module" > calculator.py
```

#### Method 2: Using Your IDE
1. Right-click in your project directory
2. Select "New File"
3. Name it with `.py` extension (e.g., `calculator.py`)

### Step 3: Add Basic Structure

```python
#!/usr/bin/env python3
"""
Module: calculator.py
Description: A simple calculator module
Author: Your Name
Date: 2025-09-14
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract second number from first and return the result."""
    return a - b

def main():
    """Main function for testing."""
    print("Calculator Module")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")

if __name__ == "__main__":
    main()
```

### Step 4: Test Your New File

```bash
# Run the new Python file
python calculator.py

# Or import it in another file
python -c "import calculator; print(calculator.add(10, 5))"
```

## 🔄 Updating Python Files

### Step 1: Open the File for Editing

```bash
# Using your preferred editor
code calculator.py        # VS Code
nano calculator.py        # Nano (Linux/macOS)
notepad calculator.py     # Notepad (Windows)
```

### Step 2: Add New Functions

Example of adding multiplication and division:

```python
def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide first number by second and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
```

### Step 3: Update the main() Function

```python
def main():
    """Main function for testing."""
    print("Calculator Module - Updated Version")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
```

### Step 4: Add Error Handling

```python
def safe_calculate(operation, a, b):
    """Safely perform calculations with error handling."""
    try:
        if operation == "add":
            return add(a, b)
        elif operation == "subtract":
            return subtract(a, b)
        elif operation == "multiply":
            return multiply(a, b)
        elif operation == "divide":
            return divide(a, b)
        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        print(f"Error: {e}")
        return None
```

### Step 5: Test Your Updates

```bash
# Run the updated file
python calculator.py

# Test specific functions
python -c "
import calculator
print('Testing updated calculator:')
print(f'10 * 2 = {calculator.multiply(10, 2)}')
print(f'10 / 2 = {calculator.divide(10, 2)}')
"
```

### Step 6: Add Documentation

Update your docstrings and add comments:

```python
def advanced_calculator(expression):
    """
    Evaluate a mathematical expression.
    
    Args:
        expression (str): Mathematical expression like "5 + 3 * 2"
    
    Returns:
        float: Result of the calculation
        
    Example:
        >>> advanced_calculator("5 + 3 * 2")
        11.0
    """
    try:
        # Use eval carefully - only for trusted input
        result = eval(expression)
        return float(result)
    except Exception as e:
        print(f"Invalid expression: {e}")
        return None
```

## 📁 Project Structure

Recommended structure for larger projects:

```
sample-project/
├── README.md
├── requirements.txt
├── .gitignore
├── app.py                 # Main application
├── calculator.py          # Calculator module
├── src/
│   ├── __init__.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── modules/
│       ├── __init__.py
│       └── advanced_calc.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── docs/
│   └── api_reference.md
└── examples/
    └── usage_examples.py
```

## 🔧 Development Workflow

### 1. Before Making Changes

```bash
# Check current status
git status

# Pull latest changes
git pull origin main

# Create a new branch (optional)
git checkout -b feature/calculator-improvements
```

### 2. Making Changes

```bash
# Edit your Python files
code calculator.py

# Test your changes
python calculator.py
```

### 3. Committing Changes

```bash
# Add your changes
git add calculator.py

# Commit with descriptive message
git commit -m "Add multiply and divide functions

- Added multiply() function with validation
- Added divide() function with zero-division handling
- Updated main() to test new operations
- Added comprehensive error handling"
```

### 4. Pushing Changes

```bash
# Push to repository
git push origin main
```

## ✨ Best Practices

### 1. Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused (max 20 lines)

### 2. File Organization
```python
# Good: Organized imports
import os
import sys
from typing import List, Dict

# Good: Constants at the top
DEFAULT_PRECISION = 2
MAX_INPUT_SIZE = 1000

# Good: Helper functions before main logic
def validate_input(value):
    """Validate numeric input."""
    # Implementation here
    pass

def format_output(result):
    """Format calculation result."""
    # Implementation here
    pass
```

### 3. Error Handling
```python
def safe_file_operation(filename):
    """Safely read a file with proper error handling."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### 4. Documentation
```python
def complex_calculation(x: float, y: float, operation: str) -> float:
    """
    Perform complex mathematical operations.
    
    Args:
        x (float): First operand
        y (float): Second operand
        operation (str): Operation type ('add', 'multiply', etc.)
    
    Returns:
        float: Result of the calculation
        
    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If division by zero is attempted
        
    Example:
        >>> complex_calculation(5.0, 3.0, 'add')
        8.0
    """
    # Implementation here
    pass
```

## 🧪 Testing

### Create Test Files

Create `test_calculator.py`:

```python
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
```

### Run Tests

```bash
# Run all tests
python test_calculator.py

# Run with verbose output
python -m unittest test_calculator.py -v

# Run specific test
python -m unittest test_calculator.TestCalculator.test_add
```

## 🔍 Debugging

### Using Print Statements
```python
def debug_function(a, b):
    """Function with debug information."""
    print(f"Debug: Input values a={a}, b={b}")
    result = a + b
    print(f"Debug: Result = {result}")
    return result
```

### Using Python Debugger
```python
import pdb

def complex_function(data):
    pdb.set_trace()  # Debugger breakpoint
    # Your code here
    processed_data = process_data(data)
    return processed_data
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Contribution Guidelines
- Write clear, documented code
- Include tests for new features
- Follow the existing code style
- Update documentation as needed

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

If you have questions or need help:
- Open an issue on GitHub
- Check the documentation in the `docs/` folder
- Review examples in the `examples/` folder

## 🎯 Next Steps

1. Try creating your own Python modules
2. Experiment with the calculator functions
3. Add new features like scientific calculations
4. Write comprehensive tests
5. Explore advanced Python concepts

---

Happy coding! 🐍✨