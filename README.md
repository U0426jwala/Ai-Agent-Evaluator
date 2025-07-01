# Ai-Agent-Evaluator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A powerful and flexible AI agent service that combines search capabilities with mathematical computation tools. Built with FastAPI for high performance and Streamlit for an intuitive user interface.

## ✨ Features

- 🔍 **Web Search Integration** - Real-time web search using SerpAPI
- 🧮 **Mathematical Computation** - Advanced math calculations with SymPy
- 🚀 **FastAPI Backend** - High-performance async API
- 🎨 **Streamlit Interface** - Beautiful web UI for easy interaction
- 🧪 **Comprehensive Testing** - Full test suite with pytest
- 📊 **Evaluation Framework** - Built-in performance evaluation system
- 🔧 **Tool-based Architecture** - Modular and extensible design

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Streamlit UI   │───▶│   FastAPI API   │───▶│   AI Agent      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                               ┌─────────────────┐
                                               │     Tools       │
                                               │  ┌───────────┐  │
                                               │  │Search Tool│  │
                                               │  └───────────┘  │
                                               │  ┌───────────┐  │
                                               │  │Math Tool  │  │
                                               │  └───────────┘  │
                                               └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- SerpAPI key (for web search functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-agent-service.git
   cd ai-agent-service
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your SERPAPI_KEY
   ```

4. **Run the FastAPI server**
   ```bash
   python main.py
   ```

5. **Launch the Streamlit interface**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📖 Usage

### API Endpoints

#### POST `/agent`
Send a prompt to the AI agent and receive a structured response.

**Request:**
```json
{
  "prompt": "Calculate the square root of 144"
}
```

**Response:**
```json
{
  "response": "Calculation result: 12",
  "tools_used": ["math_tool"],
  "metadata": {
    "calculation": "12"
  }
}
```

### Supported Queries

#### Mathematical Calculations
```
Calculate 2 + 3 * 4
Find the square root of 16
What is 15% of 200?
```

#### Web Search
```
Search for latest AI news
Who is the current president?
What is the weather like today?
```

## 🛠️ Tools

### Math Tool
- Powered by SymPy for symbolic mathematics
- Supports basic arithmetic, algebra, calculus
- Handles complex mathematical expressions
- Error handling for invalid expressions

### Search Tool
- Integration with SerpAPI for real-time web search
- Extracts relevant snippets from search results
- Handles API failures gracefully
- Configurable search parameters

## 🧪 Testing

Run the test suite:
```bash
# Unit tests
pytest test_agent.py -v

# Evaluation framework
python evaluation.py
```

### Test Coverage

The project includes comprehensive tests for:
- ✅ Mathematical calculations
- ✅ Web search functionality
- ✅ Input validation
- ✅ Error handling
- ✅ API endpoints

## 📊 Evaluation

The built-in evaluation framework tests various scenarios:

```python
# Run evaluation
python evaluation.py
```

Results are saved to `evaluation_results.json` with detailed pass/fail analysis.

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SERPAPI_KEY` | API key for SerpAPI web search | Yes |

### Customization

The agent can be easily extended with new tools:

1. Create a new tool in `app/tools/`
2. Import and integrate in `agent.py`
3. Add corresponding tests
4. Update evaluation framework

## 📁 Project Structure

```
ai-agent-service/
├── app/
│   ├── tools/
│   │   ├── math_tool.py      # Mathematical computation tool
│   │   └── search_tool.py    # Web search tool
│   ├── agent.py              # Main agent logic
│   └── models.py             # Pydantic models
├── main.py                   # FastAPI application
├── streamlit_app.py          # Streamlit web interface
├── evaluation.py             # Evaluation framework
├── test_agent.py            # Unit tests
└── README.md                # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Streamlit](https://streamlit.io/) for the beautiful UI framework
- [SymPy](https://www.sympy.org/) for symbolic mathematics
- [SerpAPI](https://serpapi.com/) for web search capabilities

## 📞 Support

If you have any questions or need help getting started, please open an issue or contact us at [ujwalakusma26@gmail.com).

---

<div align="center">
  <strong>⭐ Star this repository if you find it helpful! ⭐</strong>
</div>
