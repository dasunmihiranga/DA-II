# 🚀 DevAssist MCP Server

An advanced development workflow automation system using Model Context Protocol (MCP) that provides AI-driven tools for developers to enhance their coding workflow.

## 🌟 Features

- **Code Review Tool**: Multi-language code quality analysis with severity levels
- **Documentation Generator**: Auto-generate comprehensive project documentation
- **Test Case Generator**: Intelligent test case generation with coverage analysis
- **Bug Report Analyzer**: Smart bug report analysis and categorization
- **API Documentation Tool**: Automated API documentation generation

## 🛠️ Technology Stack

- Python 3.9+
- MCP (Model Context Protocol)
- LangChain + Ollama for local LLM integration
- FastAPI for web interface
- Pydantic for data validation
- Tree-sitter for code parsing

## 📋 Prerequisites

- Python 3.9 or higher
- Ollama installed and running locally
- Git

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/devassist-mcp-server.git
cd devassist-mcp-server
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure it:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Start the server:
```bash
python src/main.py
```

## 🛠️ Available Tools

### 1. Code Review Tool
```python
async def code_review(file_path: str, language: str, severity_filter: str = "all")
```
Analyzes code quality, suggests improvements, and identifies potential issues.

### 2. Documentation Generator
```python
async def generate_documentation(project_path: str, doc_type: str, output_format: str)
```
Generates comprehensive project documentation in various formats.

### 3. Test Case Generator
```python
async def generate_tests(file_path: str, test_framework: str, coverage_target: float)
```
Creates test cases with coverage analysis and edge case handling.

### 4. Bug Report Analyzer
```python
async def analyze_bug_report(report_data: str, format_type: str)
```
Analyzes and categorizes bug reports with priority assignment.

### 5. API Documentation Tool
```python
async def generate_api_docs(code_path: str, framework: str, output_type: str)
```
Generates API documentation with OpenAPI/Swagger specifications.

## 📚 Documentation

Detailed documentation is available in the `docs/` directory:
- [Installation Guide](docs/installation.md)
- [Configuration Guide](docs/configuration.md)
- [Usage Guide](docs/usage.md)
- [API Reference](docs/api_reference.md)
- [Contributing Guide](docs/contributing.md)

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](docs/contributing.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://github.com/ollama/ollama)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Tree-sitter](https://github.com/tree-sitter/tree-sitter) 