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
- [Help](#help)
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

## 🆘 Help

### Common Issues and Solutions

#### 1. Python Not Found Error
**Problem**: `python: command not found` or `'python' is not recognized`

**Solutions**:
```bash
# Try using python3 instead
python3 app.py

# Check Python installation
which python3
python3 --version

# On Windows, try:
py app.py
```

#### 2. Module Import Errors
**Problem**: `ModuleNotFoundError: No module named 'calculator'`

**Solutions**:
```bash
# Ensure you're in the correct directory
pwd
ls -la

# Add current directory to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or use relative imports
python -m calculator
```

#### 3. Virtual Environment Issues
**Problem**: Packages not found after installing

**Solutions**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Verify you're in the right environment
which python
pip list

# Reinstall packages if needed
pip install -r requirements.txt
```

#### 4. Permission Denied Errors
**Problem**: `PermissionError: [Errno 13] Permission denied`

**Solutions**:
```bash
# Check file permissions
ls -la filename.py

# Make file executable
chmod +x filename.py

# Run with appropriate permissions
sudo python app.py  # Use with caution
```

### Getting Help

#### 1. GitHub Issues
- Open an issue on the [sample-project repository](https://github.com/eks-pro/sample-project/issues)
- Use the issue templates provided
- Include error messages and system information
- Provide steps to reproduce the problem

#### 2. Documentation Resources
- **Python Official Documentation**: [docs.python.org](https://docs.python.org/3/)
- **Git Documentation**: [git-scm.com/doc](https://git-scm.com/doc)
- **Virtual Environments**: [python.org/tutorial/venv](https://docs.python.org/3/tutorial/venv.html)
- **PEP 8 Style Guide**: [pep8.org](https://pep8.org/)

#### 3. Community Support
- **Stack Overflow**: Tag your questions with `python` and `sample-project`
- **Python Discord**: [discord.gg/python](https://discord.gg/python)
- **Reddit**: [r/learnpython](https://reddit.com/r/learnpython)

### Troubleshooting Checklist

Before seeking help, try these steps:

1. **Verify Installation**:
   ```bash
   python --version
   git --version
   pip --version
   ```

2. **Check Project Structure**:
   ```bash
   tree .  # or ls -la for basic listing
   ```

3. **Test Basic Functionality**:
   ```bash
   python -c "print('Python is working!')"
   ```

4. **Review Error Messages**:
   - Read the full error traceback
   - Identify the line causing the issue
   - Check for typos in variable names and imports

5. **Clean and Restart**:
   ```bash
   # Remove Python cache
   find . -name "*.pyc" -delete
   find . -name "__pycache__" -delete
   
   # Restart terminal/IDE
   ```

### System Requirements

#### Minimum Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.7 or higher
- **RAM**: 2GB available memory
- **Storage**: 100MB free space

#### Recommended Setup
- **Python**: 3.9 or higher
- **IDE**: VS Code with Python extension
- **Git**: Latest version
- **Terminal**: PowerShell (Windows) or Terminal (macOS/Linux)

### Quick Reference Commands

```bash
# Project setup
git clone https://github.com/eks-pro/sample-project.git
cd sample-project
python -m venv venv
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt

# Running code
python app.py
python calculator.py
python -m unittest test_calculator.py

# Development
git status
git add .
git commit -m "Your commit message"
git push origin main

# Debugging
python -i calculator.py  # Interactive mode
python -m pdb calculator.py  # Debugger mode
```

### Contact Information

For additional support:
- **Repository Owner**: [@eks-pro](https://github.com/eks-pro)
- **Project Repository**: [sample-project](https://github.com/eks-pro/sample-project)
- **Issue Tracker**: [GitHub Issues](https://github.com/eks-pro/sample-project/issues)

Remember to provide detailed information when asking for help:
- Your operating system and version
- Python version (`python --version`)
- Complete error message
- Steps you've already tried
- Code that's causing the issue

## 🤝 Contributing

We welcome contributions to the sample-project! Your input helps make this resource better for everyone learning Python development.

### How to Contribute

1. **Fork the Repository**
   ```bash
   # Click the 'Fork' button on GitHub or use GitHub CLI
   gh repo fork eks-pro/sample-project --clone
   cd sample-project
   ```

2. **Create Your Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   # or
   git checkout -b bugfix/fix-calculator-issue
   # or
   git checkout -b docs/improve-readme
   ```

3. **Make Your Changes**
   - Write clean, documented code
   - Follow the existing code style
   - Add tests for new features
   - Update documentation as needed

4. **Test Your Changes**
   ```bash
   # Run existing tests
   python -m unittest discover tests/
   
   # Test your specific changes
   python test_calculator.py
   
   # Run your new code
   python your_new_file.py
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add amazing feature
   
   - Detailed description of what you changed
   - Why the change was necessary
   - Any breaking changes or migration notes"
   ```

6. **Push to Your Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template with details

### Contribution Guidelines

#### Code Standards
- **Follow PEP 8**: Use consistent Python style guidelines
- **Write Docstrings**: Document all functions, classes, and modules
- **Add Type Hints**: Use type annotations where appropriate
- **Keep Functions Small**: Aim for functions under 20 lines
- **Use Meaningful Names**: Variables and functions should be self-documenting

Example of good code style:
```python
def calculate_compound_interest(
    principal: float, 
    rate: float, 
    time: int, 
    compounds_per_year: int = 12
) -> float:
    """
    Calculate compound interest using the standard formula.
    
    Args:
        principal: Initial amount of money
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Time period in years
        compounds_per_year: Number of times interest compounds per year
    
    Returns:
        Final amount after compound interest
        
    Example:
        >>> calculate_compound_interest(1000, 0.05, 2, 12)
        1104.89
    """
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
```

#### Testing Requirements
- **Write Tests**: All new features must include unit tests
- **Test Coverage**: Aim for at least 80% test coverage
- **Test Edge Cases**: Include tests for error conditions and boundary values
- **Use Descriptive Test Names**: Test names should explain what they're testing

#### Documentation Standards
- **Update README**: Add documentation for new features
- **Add Examples**: Include practical usage examples
- **Comment Complex Logic**: Explain non-obvious code sections
- **Keep Examples Current**: Ensure all examples work with current code

### Types of Contributions

#### 🐛 Bug Fixes
- Fix calculation errors in existing functions
- Resolve import or dependency issues
- Correct documentation typos or inaccuracies
- Fix test failures or improve test reliability

#### ✨ New Features
- Add new mathematical functions or utilities
- Create additional example scripts
- Implement new testing utilities
- Add support for new Python versions

#### 📚 Documentation
- Improve README sections
- Add inline code comments
- Create additional tutorials or guides
- Translate documentation to other languages

#### 🧪 Testing
- Add missing test cases
- Improve test coverage
- Create integration tests
- Add performance benchmarks

#### 🎨 Code Quality
- Refactor existing code for better readability
- Improve error handling
- Optimize performance
- Add type hints to existing code

### Community Guidelines

#### Be Respectful
- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community

#### Be Collaborative
- Help newcomers get started
- Share knowledge and resources
- Provide constructive feedback
- Celebrate others' contributions

### Recognition

Contributors will be recognized in:
- Repository contributor list
- Release notes for significant contributions
- Special mentions in documentation

### Questions?

If you have questions about contributing:
- Check existing issues and discussions
- Open a new issue with the "question" label
- Reach out to maintainers directly
- Join community discussions

Thank you for contributing to sample-project! 🎉

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Next Steps

1. Try creating your own Python modules
2. Experiment with the calculator functions
3. Add new features like scientific calculations
4. Write comprehensive tests
5. Explore advanced Python concepts

---

Happy coding! 🐍✨