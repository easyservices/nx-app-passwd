# Contributing to Nextcloud App Password Manager

Thank you for your interest in contributing to the Nextcloud App Password Manager! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Environment](#development-environment)
4. [Coding Standards](#coding-standards)
5. [Submitting Changes](#submitting-changes)
6. [Pull Request Process](#pull-request-process)
7. [Testing](#testing)
8. [Documentation](#documentation)
9. [Issue Reporting](#issue-reporting)
10. [Feature Requests](#feature-requests)

## Code of Conduct

This project is committed to providing a welcoming and inclusive experience for everyone. We expect all participants to adhere to the following principles:

- Be respectful and considerate of different viewpoints and experiences
- Use welcoming and inclusive language
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```
   git clone https://github.com/YOUR-USERNAME/nextcloud-app-passwd.git
   cd nextcloud-app-passwd
   ```
3. Add the original repository as an upstream remote:
   ```
   git remote add upstream https://github.com/ORIGINAL-OWNER/nextcloud-app-passwd.git
   ```
4. Create a new branch for your changes:
   ```
   git checkout -b feature/your-feature-name
   ```

## Development Environment

### Prerequisites

- Python 3.6 or higher
- PowerShell 7.1 or higher (for Windows users)
- Git

### Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install development dependencies:
   ```
   pip install -r requirements-dev.txt
   ```

### Running the Application

Run the application using Streamlit:

```
streamlit run streamlit_app.py
```

## Coding Standards

This project follows PEP 8 style guidelines for Python code. Additionally:

- Use 4 spaces for indentation (no tabs)
- Maximum line length of 88 characters
- Use docstrings for all functions, classes, and modules
- Write clear, descriptive variable and function names
- Include type hints where appropriate
- Keep functions focused on a single responsibility
- Add comments for complex logic

We use the following tools to maintain code quality:

- Black for code formatting
- Flake8 for linting
- isort for import sorting
- mypy for type checking

Run the formatting tools before submitting changes:

```
black .
isort .
flake8
mypy .
```

## Submitting Changes

1. Make your changes in your feature branch
2. Add and commit your changes with a descriptive commit message:
   ```
   git add .
   git commit -m "Add feature: brief description of changes"
   ```
3. Keep your fork in sync with the upstream repository:
   ```
   git fetch upstream
   git rebase upstream/main
   ```
4. Push your changes to your fork:
   ```
   git push origin feature/your-feature-name
   ```
5. Create a pull request from your fork to the original repository

## Pull Request Process

1. Ensure your code follows the project's coding standards
2. Update documentation as necessary
3. Include tests for new features or bug fixes
4. Ensure all tests pass
5. Update the CHANGELOG.md with details of your changes
6. Your pull request will be reviewed by maintainers who may request changes
7. Once approved, your changes will be merged

## Testing

We encourage test-driven development. Please include tests for new features and ensure existing tests pass.

To run tests:

```
pytest
```

For coverage report:

```
pytest --cov=. --cov-report=html
```

## Documentation

Good documentation is essential. Please update the following as needed:

- Code comments and docstrings
- README.md for user-facing changes
- TECHNICAL.md for implementation details
- API_DOCUMENTATION.md for API changes
- USER_GUIDE.md for user interface changes

## Issue Reporting

If you find a bug or have a suggestion, please create an issue on GitHub:

1. Check if the issue already exists
2. Use a clear, descriptive title
3. Provide detailed steps to reproduce the issue
4. Include expected and actual behavior
5. Add screenshots if applicable
6. Mention your environment (OS, Python version, etc.)

## Feature Requests

We welcome feature requests! When submitting a feature request:

1. Use a clear, descriptive title
2. Explain the problem the feature would solve
3. Describe the solution you'd like
4. Consider alternative solutions
5. Provide context on who would benefit from this feature

---

Thank you for contributing to the Nextcloud App Password Manager!

Copyright 2025 harokku999@gmail.com | MIT License