---
name: agent-builder
description: Meta-skill for constructing specialized multi-agent systems using Claude Agent SDK. Use when users request "build me an agent that...", "create an agent for...", "how can an agent help me...", or any request to automate workflows with AI agents. Constructs subagent-based architectures with research capabilities, proper tool restrictions, and SDK compliance.
---

# Agent Builder (AB)

A meta-skill that constructs specialized multi-agent systems following Claude Agent SDK best practices. AB orchestrates research subagents to gather documentation, then builds task-specific agents with appropriate tools and configurations.

## When This Skill Triggers

AB automatically activates when users request agent creation or workflow automation:
- "Build me an agent that..."
- "Create an agent for..."
- "How can an agent help me..."
- "I need an automated workflow for..."
- "Can you make an agent to..."

## Core Capabilities

1. **Task Analysis** - Understand user intent and identify required capabilities
2. **Documentation Research** - Spawn subagents to fetch relevant SDK documentation
3. **Agent Design** - Architect multi-agent systems within SDK constraints
4. **Agent Construction** - Generate markdown files or programmatic configurations
5. **Validation** - Ensure SDK compliance and best practices

## Critical SDK Constraints

Before designing any agent system, understand these hard constraints:

- **2 Layers Maximum**: Main orchestrator → Subagents (subagents CANNOT spawn other subagents)
- **Flat File Structure**: All subagents as markdown files in `.claude/agents/`
- **YAML Configuration**: Use YAML frontmatter, not JSON config files
- **No Nested Directories**: Each subagent is a single `.md` file at the root of `.claude/agents/`

## Workflow

### Phase 1: Task Analysis

Evaluate the user's request:

1. **User Intent**: What problem are they trying to solve?
2. **Required Capabilities**: What tools/skills/knowledge does this need?
3. **Available Skills**: Check `.claude/skills/` for relevant existing skills
4. **Complexity Assessment**: Can this be done with 2 layers? (Main agent → Subagents)
5. **Architecture Type**: Programmatic (SDK code) or Filesystem (markdown files)?

If the task requires more than 2 layers of agents, explain the SDK constraint and suggest alternative architectures.

### Phase 2: Documentation Research

Spawn research subagents to gather relevant documentation. Each research subagent:

1. Reads documentation skill URL maps (e.g., `.claude/skills/anthropic-agent-docs/SKILL.md`)
2. Uses `web_fetch` to retrieve specific documentation pages
3. Extracts relevant information (tool names, patterns, examples, best practices)
4. Writes comprehensive findings to `.claude/scratchpad/<topic>-research.md`
5. Reports file location back to orchestrator

**Common Research Topics:**
- Claude Agent SDK subagents documentation
- Available MCP tools and servers
- Hooks and event systems
- Tool permissions and restrictions
- Relevant domain-specific patterns

**Scratchpad Output Pattern:**
```
.claude/scratchpad/
  ├── agent-sdk-research.md
  ├── mcp-tools-research.md
  ├── domain-patterns-research.md
  └── security-best-practices.md
```

### Phase 3: Agent Design & Approval

Present the proposed architecture to the user:

```
PROPOSED AGENT ARCHITECTURE
===========================
Name: <agent-name>
Purpose: <clear description>
Implementation: [Programmatic | Filesystem]

STRUCTURE (2 Layers per SDK):
- Main Agent (Orchestrator): <responsibilities>
  - Subagent 1: <name> - <responsibilities>
  - Subagent 2: <name> - <responsibilities>
  - Subagent 3: <name> - <responsibilities>

FILE STRUCTURE:
.claude/agents/
  ├── <subagent-1-name>.md
  ├── <subagent-2-name>.md
  └── <subagent-3-name>.md

TOOLS PER SUBAGENT:
- <subagent-1>: Read, Grep, Bash
- <subagent-2>: WebFetch, Write
- <subagent-3>: mcp__github__list_repos, Read, Write

SKILLS REQUIRED:
- <skill 1>
- <skill 2>

APPROVE THIS DESIGN? (yes/no/modify)
```

Wait for user approval before proceeding to construction.

### Phase 4: Agent Construction

After approval, construct the agent system by reading all scratchpad research files and using findings to inform decisions.

#### For Filesystem Agents (Recommended for Most Cases)

Create markdown files in `.claude/agents/`:

**File Structure Template:**
```markdown
---
name: <agent-name>
description: <When to use this agent. Use PROACTIVELY for automatic invocation>
tools: <comma-separated tool list from research>
model: sonnet
---

# <Agent Role>

You are a specialized agent for <purpose>.

## Capabilities (from research)
- <capability 1 from scratchpad research>
- <capability 2 from scratchpad research>

## Tools Available
<List tools from scratchpad research with descriptions>

## Workflow
1. <step informed by research>
2. <step informed by research>
3. Write results to .claude/scratchpad/<output-name>.md
4. Report completion to orchestrator

## Best Practices (from research)
- <practice 1>
- <practice 2>
```

**Critical Construction Steps:**

1. **Read ALL scratchpad research files**
2. **Extract tool names** from research (exact names like `mcp__github__list_repos`)
3. **Copy relevant patterns** from documentation into system prompts
4. **Embed best practices** discovered during research
5. **Validate tool names** exist in research documentation
6. **Use kebab-case** for file names

#### For Programmatic Agents (Complex Cases)

Generate Python/TypeScript code:

```python
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    agents={
        'subagent-name': {
            'description': 'Clear when-to-use description',
            'prompt': '''System prompt referencing research findings...''',
            'tools': ['Read', 'Write', 'mcp__service__tool'],
            'model': 'sonnet'
        }
    }
)

async for message in query(prompt="Task description", options=options):
    print(message)
```

### Phase 5: Validation

Before delivering, validate:

1. **SDK Compliance**: 2 layers max, flat structure, YAML frontmatter
2. **Tool Names**: All tools referenced exist in research
3. **Clear Descriptions**: Each subagent has precise delegation trigger
4. **Complete Prompts**: System prompts include workflow and best practices
5. **File Naming**: kebab-case, descriptive names

## Tool Selection Guidelines

### Read-Only Agents (Analysis, Review)
```yaml
tools: Read, Grep, Glob
```

### Write Agents (Creation, Editing)
```yaml
tools: Read, Write, Edit, MultiEdit
```

### Execution Agents (Running Commands)
```yaml
tools: Read, Write, Bash
```

### Research Agents (Documentation Fetching)
```yaml
tools: Read, Write, WebFetch, WebSearch
```

### MCP Integration
```yaml
tools: Read, Write, mcp__server__tool_name
```

## Common Patterns

### Pattern 1: Research → Analysis → Report
```
Main Agent
├── research-agent.md (gathers information)
├── analysis-agent.md (processes findings)
└── report-agent.md (generates output)
```

### Pattern 2: Monitor → Detect → Act
```
Main Agent
├── monitor-agent.md (watches for events)
├── detector-agent.md (identifies issues)
└── action-agent.md (takes corrective steps)
```

### Pattern 3: Fetch → Transform → Store
```
Main Agent
├── fetcher-agent.md (retrieves data)
├── transformer-agent.md (processes data)
└── storage-agent.md (persists results)
```

## Troubleshooting

### User wants 3+ layers
- Explain SDK constraint: subagents cannot spawn subagents
- Suggest flattening hierarchy: use parallelism instead of nesting
- Offer to redesign with 2-layer architecture

### Unclear tool requirements
- Spawn additional research subagents
- Fetch MCP server documentation
- Provide tool options to user for selection

### Complex domain logic
- Create reference file in `.claude/agents/references/`
- Link from subagent system prompt
- Keep core workflow in markdown, details in reference

## References

For detailed patterns and examples, see:
- `references/subagent-examples.md` - Common subagent configurations
- `references/mcp-integration.md` - MCP server setup patterns
- `references/debugging-agents.md` - Troubleshooting guide

## Official Claude Agent Documentation

- Claude Agent SDK: https://docs.claude.com/en/docs/agent-sdk/overview
- Subagents Guide: https://docs.claude.com/en/docs/agent-sdk/subagents
- Claude Code Subagents: https://docs.claude.com/en/docs/claude-code/sub-agents
