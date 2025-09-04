# AI-agent
AI Assistant with GitHub Integration

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure GitHub Integration
Copy the example environment file and configure your GitHub token:
```bash
cp .env.example .env
```

Edit `.env` and add your GitHub personal access token:
```
GITHUB_TOKEN=your_github_token_here
GITHUB_USERNAME=your_github_username
GITHUB_REPO=your_default_repo
```

**How to get a GitHub token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select required scopes (repo, user, etc.)
4. Copy the token to your `.env` file

### 3. Run the AI Agent
```bash
python -m ai_agent.main
```

## Features

- **GitHub Integration**: Connect with GitHub API to manage repositories, issues, and more
- **Plugin System**: Extensible architecture for adding new capabilities
- **Environment Configuration**: Easy setup with `.env` file support
- **Logging**: Comprehensive logging for monitoring and debugging

## GitHub Plugin Capabilities

The GitHub plugin provides:
- User authentication and profile information
- Repository listing and management
- Issue creation and management
- Basic API operations

## Development

The project structure:
```
ai_agent/
├── __init__.py          # Package initialization
├── main.py              # Entry point
├── core.py              # Core Agent class
├── plugins.py           # Plugin loading system
└── github_plugin.py     # GitHub integration
```

## License

GNU Affero General Public License v3.0
