# Technical Specification

## Data Schemas

### 1. The Agent Task (JSON)
Payload between Planner -> Worker -> Judge.

```json
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "Promote summer line",
    "persona_constraints": ["Use Gen-Z slang", "No emojis"],
    "required_resources": ["mcp://twitter/mentions/123"]
  },
  "assigned_worker_id": "string",
  "status": "pending | in_progress | review | complete",
  "created_at": "timestamp",
  "result_artifact": {
    "content": "string",
    "media_url": "string",
    "confidence_score": 0.95
  }
}
```

### 2. MCP Tool Definition
Example: `post_content`

```json
{
  "name": "post_content",
  "description": "Publishes text and media to a connected social platform.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "platform": { "type": "string", "enum": ["twitter", "instagram"] },
      "text_content": { "type": "string" },
      "media_urls": { "type": "array", "items": { "type": "string" } },
      "disclosure_level": { "type": "string", "enum": ["automated", "assisted"] }
    },
    "required": ["platform", "text_content"]
  }
}
```

## API Contracts (Service-to-Service)
- **POST /planner/goal**: Accepts natural language goal, returns `plan_id`.
- **POST /judge/review**: Accepts `task_result`, returns `verdict` (approve/reject/escalate).

## Infrastructure Maps
- **Service Discovery**: K8s Services (planner-svc, worker-svc).
- **Queues**: Redis Lists (`queue:tasks`, `queue:review`).
- **Secrets**: AWS Secrets Manager / K8s Secrets (for Coinbase Keys).
