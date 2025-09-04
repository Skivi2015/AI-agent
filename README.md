# AI-agent
AI Assistant with GitHub plugin support

## Usage

Run the AI agent:
```bash
cd AI-agent
pip install -r requirements.txt
python -m ai_agent.main
```

## GitHub Plugin

The agent includes a GitHub plugin that supports the following commands:

- `github list` - List your GitHub repositories (requires GITHUB_TOKEN environment variable)
- `github clone <repo>` - Clone a specific repository (e.g., `github clone Skivi2015/AI-agent`)
- `github clone all` - Clone all predefined repositories

### Setting up GitHub Token (Optional)

To use the `github list` command, set your GitHub token:
```bash
export GITHUB_TOKEN=your_github_token_here
```

### Predefined Repositories

The following repositories are cloned when using `github clone all`:
- Skivi2015/AImanager-AIM
- Skivi2015/Omniscope
- Skivi2015/Godmode
- Skivi2015/AI-agent
- Skivi2015/android-ci-bootstrap
