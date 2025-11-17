# MCP Integration Patterns

Guide for integrating Model Context Protocol (MCP) servers into agent architectures. MCP provides standardized integrations to external services.

## Understanding MCP

MCP servers expose tools that Claude agents can use to interact with external services:
- GitHub operations (repos, issues, PRs)
- Trello board management
- Database queries
- Slack messaging
- Custom API integrations

## MCP Tool Naming Convention

MCP tools follow this pattern:
```
mcp__<server-name>__<tool-name>
```

Examples:
- `mcp__github__list_repos`
- `mcp__github__create_issue`
- `mcp__trello__create_card`
- `mcp__slack__send_message`

## Configuring MCP in Agents

### Programmatic Configuration (Python)

```python
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    mcp={
        'servers': [
            {
                'url': 'https://api.github.com/mcp',
                'name': 'github',
                'headers': {
                    'Authorization': 'Bearer token'
                }
            }
        ],
        'strict_mcp_config': True  # Only use configured servers
    },
    allowed_tools=['Read', 'Write', 'mcp__github__list_repos']
)

async for message in query(prompt="List my repositories", options=options):
    print(message)
```

### Programmatic Configuration (TypeScript)

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk';

const options = {
  mcp: {
    servers: [
      {
        url: 'https://api.github.com/mcp',
        name: 'github',
        headers: {
          Authorization: 'Bearer token'
        }
      }
    ],
    strictMcpConfig: true
  },
  allowedTools: ['Read', 'Write', 'mcp__github__list_repos']
};

for await (const message of query({
  prompt: "List my repositories",
  options
})) {
  console.log(message);
}
```

### Filesystem Configuration

MCP servers can be configured at the project level in `.claude/` directory or user level in `~/.claude/`.

**Example: `.claude/mcp.json`**
```json
{
  "servers": {
    "github": {
      "url": "https://api.github.com/mcp",
      "headers": {
        "Authorization": "Bearer ${GITHUB_TOKEN}"
      }
    },
    "trello": {
      "url": "https://api.trello.com/mcp",
      "headers": {
        "Authorization": "Bearer ${TRELLO_TOKEN}"
      }
    }
  }
}
```

## Common MCP Server Integrations

### GitHub MCP Server

**Available Tools:**
- `mcp__github__list_repos` - List user repositories
- `mcp__github__get_file_contents` - Read file from repository
- `mcp__github__create_issue` - Create GitHub issue
- `mcp__github__create_pr` - Create pull request
- `mcp__github__list_issues` - List repository issues
- `mcp__github__update_issue` - Update existing issue

**Subagent Example:**
```markdown
---
name: github-integration
description: Use for GitHub operations
tools: Read, Write, mcp__github__list_repos, mcp__github__create_issue, mcp__github__get_file_contents
model: sonnet
---

You manage GitHub operations. Available tools:
- List repositories with mcp__github__list_repos
- Create issues with mcp__github__create_issue
- Read files with mcp__github__get_file_contents

Always handle rate limiting and authentication errors gracefully.
```

### Trello MCP Server

**Available Tools:**
- `mcp__trello__list_boards` - List user boards
- `mcp__trello__create_card` - Create card on board
- `mcp__trello__update_card` - Update existing card
- `mcp__trello__move_card` - Move card between lists
- `mcp__trello__add_checklist` - Add checklist to card

**Subagent Example:**
```markdown
---
name: trello-integration
description: Use for Trello board management
tools: Read, Write, mcp__trello__create_card, mcp__trello__list_boards
model: sonnet
---

You manage Trello boards. When creating cards:
1. Use mcp__trello__list_boards to find target board
2. Use mcp__trello__create_card with proper format
3. Include full context in card description
4. Add relevant labels and due dates
```

### Slack MCP Server

**Available Tools:**
- `mcp__slack__send_message` - Send message to channel
- `mcp__slack__list_channels` - List available channels
- `mcp__slack__upload_file` - Upload file to channel
- `mcp__slack__get_channel_history` - Read channel messages

**Subagent Example:**
```markdown
---
name: slack-integration
description: Use for Slack messaging and notifications
tools: Read, mcp__slack__send_message, mcp__slack__list_channels
model: haiku
---

You send Slack messages. Format messages clearly:
- Use markdown for formatting
- @ mention relevant people
- Include context and action items
- Use threads for follow-ups
```

### Database MCP Server

**Available Tools:**
- `mcp__database__query` - Execute SQL queries
- `mcp__database__list_tables` - List database tables
- `mcp__database__describe_table` - Get table schema
- `mcp__database__transaction` - Execute transaction

**Subagent Example:**
```markdown
---
name: database-integration
description: Use for database queries and data retrieval
tools: Read, Write, mcp__database__query, mcp__database__list_tables
model: sonnet
---

You execute database operations safely:
1. Always use parameterized queries
2. Verify read vs write operations
3. Use mcp__database__list_tables to discover schema
4. Limit result sets to prevent memory issues
5. Handle connection errors gracefully
```

## MCP Security Best Practices

### Authentication

1. **Environment Variables**: Store tokens in environment variables
   ```bash
   export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
   export TRELLO_TOKEN=xxxxxxxxxxxx
   ```

2. **Secure Token Storage**: Never hardcode tokens in configuration files
   ```json
   {
     "headers": {
       "Authorization": "Bearer ${GITHUB_TOKEN}"  // ✓ Good
       // "Authorization": "Bearer ghp_xxx"       // ✗ Bad
     }
   }
   ```

3. **Scope Limiting**: Request minimum necessary permissions for tokens

### Tool Restrictions

Limit subagent access to only required MCP tools:

```yaml
# Too permissive - avoid this
tools: Read, Write, mcp__github__*

# Properly scoped - prefer this
tools: Read, Write, mcp__github__list_repos, mcp__github__get_file_contents
```

### Rate Limiting

Handle API rate limits gracefully:

```python
# In subagent prompt
"""
When you encounter rate limiting:
1. Log the rate limit status
2. Wait for reset time
3. Retry the operation
4. Report rate limit issues to orchestrator
"""
```

## Custom MCP Server Creation

### In-Process MCP Server (SDK)

Create custom tools without separate processes:

```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("calculate_sum", "Add two numbers", {"a": int, "b": int})
async def calculate_sum(args):
    result = args['a'] + args['b']
    return {
        "content": [
            {"type": "text", "text": f"Sum: {result}"}
        ]
    }

# Create MCP server with tool
server = create_sdk_mcp_server(
    name="calculator",
    version="1.0.0",
    tools=[calculate_sum]
)

# Use in agent
options = ClaudeAgentOptions(
    mcp_servers={"calc": server},
    allowed_tools=["mcp__calc__calculate_sum"]
)
```

### External MCP Server

For complex integrations, create standalone MCP servers:

```python
# mcp_server.py
from mcp_sdk import create_server, tool

@tool("custom_operation")
async def custom_operation(params):
    # Complex operation logic
    return {"result": "success"}

app = create_server(
    name="custom-service",
    tools=[custom_operation]
)

if __name__ == "__main__":
    app.run(port=8080)
```

Configure in `.claude/mcp.json`:
```json
{
  "servers": {
    "custom": {
      "command": "python",
      "args": ["mcp_server.py"],
      "name": "custom-service"
    }
  }
}
```

## Troubleshooting MCP Integration

### Common Issues

**1. Tool Not Found**
```
Error: mcp__github__list_repos not found
```
Solution: Verify MCP server is configured and tool name is correct

**2. Authentication Failed**
```
Error: 401 Unauthorized
```
Solution: Check token validity and environment variables

**3. Rate Limited**
```
Error: 429 Too Many Requests
```
Solution: Implement retry logic with exponential backoff

**4. Timeout**
```
Error: Request timeout
```
Solution: Increase timeout or optimize query

### Debugging MCP Integration

1. **Verify Server Configuration**
   ```bash
   # Check MCP server config
   cat .claude/mcp.json
   ```

2. **Test Tool Availability**
   ```python
   # List available tools
   async with ClaudeSDKClient(options=options) as client:
       tools = await client.list_tools()
       print(tools)
   ```

3. **Enable Debug Logging**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

4. **Test Server Directly**
   ```bash
   # For HTTP-based servers
   curl -X POST https://api.service.com/mcp/tool \
     -H "Authorization: Bearer token" \
     -d '{"params": {}}'
   ```

## MCP Integration Checklist

When integrating MCP servers into agents:

- [ ] Identify required external services
- [ ] Configure MCP servers (programmatic or filesystem)
- [ ] Store authentication tokens securely
- [ ] Specify exact tool names in subagent YAML
- [ ] Test authentication and tool availability
- [ ] Implement error handling for rate limits
- [ ] Document required environment variables
- [ ] Test with real API calls before deployment
- [ ] Set up monitoring for API usage
- [ ] Plan for token rotation and updates

## Resources

- **MCP Documentation**: https://modelcontextprotocol.io
- **Claude Agent SDK MCP Guide**: https://docs.claude.com/en/docs/agent-sdk/mcp
- **Available MCP Servers**: Check community registry for pre-built servers
