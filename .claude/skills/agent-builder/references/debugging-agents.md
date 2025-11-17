# Debugging Agents

Troubleshooting guide for diagnosing and fixing issues in Claude Agent SDK multi-agent systems.

## Common Issues and Solutions

### 1. Subagent Not Being Invoked

**Symptoms:**
- Main agent doesn't delegate to subagent
- Tasks handled by main agent instead of specialist
- No mention of subagent in conversation

**Diagnosis:**
```bash
# Check if subagent file exists
ls -la .claude/agents/

# Verify YAML frontmatter format
head -n 10 .claude/agents/your-agent.md
```

**Common Causes:**

**A. Weak Description Field**
```yaml
# ❌ Too vague
description: Helps with code

# ✅ Clear and specific
description: Use PROACTIVELY for code review tasks including security analysis, style checking, and best practice validation
```

**B. Missing PROACTIVELY Keyword**
```yaml
# ❌ No automatic invocation
description: Code review specialist

# ✅ Enables automatic invocation
description: Use PROACTIVELY for code review after any code changes
```

**C. Tool Mismatch**
```yaml
# Agent needs WebFetch but only has Read
tools: Read, Write  # ❌ Missing WebFetch

# Should be
tools: Read, Write, WebFetch  # ✅ Correct
```

**Solutions:**
1. Strengthen description with specific triggers
2. Add "Use PROACTIVELY" or "MUST BE USED" to description
3. Verify tools list includes all required tools
4. Check task matches description closely

### 2. Subagent Errors or Failures

**Symptoms:**
- Error messages from subagent
- Subagent crashes or hangs
- Incomplete results

**Diagnosis:**
```bash
# Check recent logs
tail -f .claude/logs/agent.log

# Verify tool permissions
cat .claude/agents/your-agent.md | grep "tools:"

# Test tool availability
# Try using the tool directly in main conversation
```

**Common Causes:**

**A. Tool Restrictions**
```yaml
# Agent tries to write but only has read access
tools: Read, Grep  # ❌ No Write

# Should be
tools: Read, Grep, Write  # ✅ Has Write
```

**B. Invalid MCP Tool Names**
```yaml
# Wrong tool name format
tools: github_list_repos  # ❌ Wrong format

# Correct MCP tool format
tools: mcp__github__list_repos  # ✅ Correct
```

**C. Missing Dependencies**
```yaml
# Agent needs bash but only has read
tools: Read, Write  # ❌ No Bash

# For Python scripts, need Bash
tools: Read, Write, Bash  # ✅ Has Bash
```

**Solutions:**
1. Add missing tools to tools list
2. Verify MCP tool names use correct format
3. Check tool requirements in error messages
4. Test tools individually before full workflow

### 3. Context Overflow

**Symptoms:**
- "Context limit exceeded" errors
- Slow agent responses
- Incomplete processing

**Diagnosis:**
```bash
# Check scratchpad file sizes
du -h .claude/scratchpad/

# Count total tokens (rough estimate)
wc -w .claude/scratchpad/*.md
```

**Common Causes:**

**A. Large Research Files**
```bash
# Research file too detailed
-rw-r--r-- 1 user user 500K api-research.md  # ❌ Too large
```

**B. No Context Management**
```markdown
# Agent reads everything without filtering
You are a research agent.
Read all files and provide complete details.  # ❌ No limits
```

**Solutions:**
1. **Implement Progressive Disclosure:**
```markdown
You are a research agent.

## Workflow
1. Read file headers/summaries first
2. Identify relevant sections only
3. Load detailed content as needed
4. Summarize findings concisely
```

2. **Limit Research Scope:**
```markdown
When researching:
- Extract only relevant sections (not entire docs)
- Summarize long content (>1000 words)
- Focus on actionable information
- Write concise findings to scratchpad
```

3. **Use Compact Command:**
```bash
# In Claude Code, compact context
/compact
```

### 4. Scratchpad Communication Issues

**Symptoms:**
- Main agent can't find subagent results
- Subagent doesn't write to scratchpad
- File paths don't match

**Diagnosis:**
```bash
# Check scratchpad contents
ls -la .claude/scratchpad/

# Verify file was created
cat .claude/scratchpad/expected-file.md
```

**Common Causes:**

**A. Inconsistent File Paths**
```markdown
# Subagent A writes to:
.claude/scratchpad/research.md  # ❌ Generic name

# Main agent looks for:
.claude/scratchpad/github-research.md  # ❌ Different name
```

**B. Missing Write Instructions**
```yaml
# No instruction to write to scratchpad
---
name: research-agent
description: Research GitHub APIs
tools: Read, WebFetch
---

You research GitHub APIs.  # ❌ No output instructions
```

**Solutions:**
1. **Standardize File Naming:**
```markdown
You are a research agent.

## Output Location
ALWAYS write findings to:
.claude/scratchpad/<topic>-research.md

Example: If researching GitHub APIs:
.claude/scratchpad/github-api-research.md
```

2. **Explicit Write Instructions:**
```markdown
## Your Process
1. Gather information
2. Analyze findings
3. Write to .claude/scratchpad/<topic>-research.md
4. Report file path: "Research complete: .claude/scratchpad/<topic>-research.md"
```

3. **Template Output Format:**
```markdown
Write your findings using this format:

# [Topic] Research
Source: [URL]
Date: [Today's date]

## Key Findings
[Concise bullet points]

## Detailed Information
[Relevant details]

## References
[Links and citations]
```

### 5. Tool Permission Errors

**Symptoms:**
- "Permission denied" errors
- "Tool not allowed" messages
- Operations fail silently

**Diagnosis:**
```bash
# Check permission mode in agent config
grep -r "permission_mode" .claude/

# Verify tool allowlist
grep "allowed_tools" .claude/agents/
```

**Common Causes:**

**A. Write Protection**
```python
# Permission mode too restrictive
options = ClaudeAgentOptions(
    permission_mode='readOnly'  # ❌ Can't write
)
```

**B. Tool Not in Allowlist**
```yaml
# Agent needs Edit but only has Write
tools: Read, Write  # ❌ Missing Edit
```

**Solutions:**
1. **Set Appropriate Permissions:**
```python
# For editing operations
options = ClaudeAgentOptions(
    permission_mode='acceptEdits',  # ✅ Auto-accept edits
    allowed_tools=['Read', 'Write', 'Edit', 'MultiEdit']
)
```

2. **Expand Tool Allowlist:**
```yaml
# Include all needed tools
tools: Read, Write, Edit, MultiEdit, Bash, Grep, Glob
```

### 6. MCP Server Connection Issues

**Symptoms:**
- "MCP server not responding"
- "Connection timeout"
- MCP tools unavailable

**Diagnosis:**
```bash
# Test MCP server connection
curl -X POST https://api.service.com/mcp/health

# Check MCP config
cat .claude/mcp.json

# Verify environment variables
echo $GITHUB_TOKEN
```

**Common Causes:**

**A. Missing Authentication**
```json
{
  "headers": {
    "Authorization": "Bearer ${GITHUB_TOKEN}"
  }
}
```
But `GITHUB_TOKEN` not set in environment.

**B. Wrong Server URL**
```json
{
  "url": "https://api.github.com/mcp"  // ❌ Wrong endpoint
}
```

**C. Network Issues**
- Server down
- Firewall blocking
- Rate limiting

**Solutions:**
1. **Verify Environment Variables:**
```bash
# Set missing tokens
export GITHUB_TOKEN=ghp_xxxxxxxxx
export TRELLO_TOKEN=xxxxxxxxx
```

2. **Test Server Manually:**
```bash
# Test GitHub API
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/user/repos
```

3. **Check Server Status:**
- Visit status page
- Check logs for errors
- Verify credentials are current

### 7. Subagent Infinite Loops

**Symptoms:**
- Agent keeps repeating same action
- Never reports completion
- Context fills up with repeated content

**Diagnosis:**
```bash
# Check for repeated patterns in logs
tail -n 100 .claude/logs/agent.log | grep "pattern"

# Monitor resource usage
top  # Check if agent is consuming resources
```

**Common Causes:**

**A. No Exit Condition**
```markdown
You monitor files for changes.
When you see a change, analyze it and monitor again.  # ❌ Infinite loop
```

**B. Unclear Success Criteria**
```markdown
Keep trying until it works.  # ❌ No definition of "works"
```

**Solutions:**
1. **Define Clear Exit Conditions:**
```markdown
You monitor files for changes.

## Exit Conditions
- Report after finding change
- Stop after 10 checks if no changes
- Maximum monitoring time: 5 minutes
```

2. **Set Iteration Limits:**
```markdown
## Process
1. Check for changes (max 10 iterations)
2. If found: analyze and report
3. If not found after 10 checks: report no changes
4. EXIT after reporting
```

## Debugging Workflow

### Step 1: Identify the Problem
1. Read error messages carefully
2. Check which agent is failing (main or subagent)
3. Note the specific operation that fails

### Step 2: Isolate the Cause
1. Test in isolation:
   - Can subagent run alone?
   - Does tool work independently?
   - Is MCP server reachable?

2. Check configurations:
   - YAML frontmatter format
   - Tool permissions
   - File paths

3. Review logs:
   - Error messages
   - Stack traces
   - Tool invocations

### Step 3: Test the Fix
1. Make minimal change
2. Test specific scenario
3. Verify fix doesn't break other features
4. Document the solution

### Step 4: Prevent Recurrence
1. Add validation to agent prompt
2. Improve error messages
3. Add safeguards
4. Document known issues

## Debugging Tools

### 1. File Inspection
```bash
# Check agent configuration
cat .claude/agents/your-agent.md

# View scratchpad contents
ls -la .claude/scratchpad/
cat .claude/scratchpad/research.md

# Check agent structure
tree .claude/agents/
```

### 2. Log Analysis
```bash
# View recent logs
tail -f .claude/logs/agent.log

# Search for errors
grep -i error .claude/logs/agent.log

# Filter by agent name
grep "research-agent" .claude/logs/agent.log
```

### 3. Tool Testing
```bash
# Test bash tool
bash -c "echo 'test'"

# Test file operations
ls -la /home/claude/

# Test web fetch
curl -I https://docs.anthropic.com
```

### 4. Configuration Validation
```bash
# Validate YAML frontmatter
head -n 10 .claude/agents/agent.md

# Check for syntax errors
python -c "import yaml; yaml.safe_load(open('.claude/agents/agent.md').read().split('---')[1])"
```

## Prevention Best Practices

### 1. Clear Descriptions
```yaml
# ✅ Good description
description: Use PROACTIVELY after code changes to run test suite, analyze failures, and suggest fixes. Expert in pytest, jest, and unittest frameworks.

# ❌ Bad description
description: Runs tests
```

### 2. Explicit Exit Conditions
```markdown
## Process
1. Execute operation
2. Verify success
3. Write results to scratchpad
4. Report completion: "Task complete at <file-path>"
5. EXIT
```

### 3. Error Handling
```markdown
## Error Handling
If operation fails:
1. Log error with context
2. Try alternative approach (once)
3. If still failing, report to orchestrator
4. DO NOT retry indefinitely
```

### 4. Validation Checks
```markdown
## Validation
Before proceeding:
- Verify required files exist
- Check tool availability
- Confirm permissions
- Validate input parameters
```

### 5. Testing Checklist
Before deployment:
- [ ] Test subagent in isolation
- [ ] Verify tool permissions
- [ ] Check MCP server connections
- [ ] Validate file paths
- [ ] Test error scenarios
- [ ] Verify exit conditions
- [ ] Review logs for issues
- [ ] Test with real data

## Getting Help

If you're still stuck:

1. **Check Official Documentation**
   - https://docs.claude.com/en/docs/agent-sdk
   - https://docs.claude.com/en/docs/claude-code/sub-agents

2. **Review Example Agents**
   - Look at working examples in references/subagent-examples.md
   - Study patterns in public skills

3. **Simplify and Test**
   - Remove complexity
   - Test one component at a time
   - Add complexity back gradually

4. **Ask Specific Questions**
   - Include error messages
   - Share relevant configuration
   - Describe expected vs actual behavior
