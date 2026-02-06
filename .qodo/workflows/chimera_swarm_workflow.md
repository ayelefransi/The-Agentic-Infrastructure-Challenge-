# Chimera Swarm Workflow

This document outlines the operational workflow of the Project Chimera "FastRender" Swarm.

## The Planner-Worker-Judge Lifecycle

The system operates on an asynchronous "Hub-and-Spoke" model to handle high-concurrency social tasks.

### Diagram
```mermaid
sequenceDiagram
    participant User as Network Operator
    participant Planner as Planner Agent
    participant Queue as Redis TaskQueue
    participant Worker as Worker Agent
    participant Judge as Judge Agent (Safety)
    participant MCP as MCP Tool (Twitter/Wallet)
    participant DB as Global State

    User->>Planner: "Goal: Promote Summer Sale"
    activate Planner
    Planner->>DB: Read Persona & Constraints
    Planner->>Planner: Decompose into 20 Tasks
    Planner->>Queue: Push Tasks
    deactivate Planner

    par Parallel Execution
        Worker->>Queue: Pop Task
        activate Worker
        Worker->>Worker: Execute Logic (Draft/Design)
        Worker->>Judge: Submit Proposal
        deactivate Worker
    
        activate Judge
        Judge->>Judge: Policy Check (Budget/Brand)
        Judge->>Judge: Calc Confidence Score
        
        alt Score > 0.9
            Judge->>MCP: Execute Action (Post/Pay)
            MCP-->>Judge: Success
            Judge->>DB: Update State
        else Score < 0.7
            Judge->>Queue: Reject & Retry
        else Low Confidence
            Judge->>User: Request Approval
        end
        deactivate Judge
    end
```

### Workflow Stages

1.  **Ingestion & Planning**:
    - **Trigger**: New Goal from User or Trend Alert from Perception System.
    - **Action**: Planner decomposes the abstract goal into concrete `Task` objects (e.g., "Draft Tweet", "Generate Image").
    - **Output**: Populates the `task_queue`.

2.  **Execution (Stateless Workers)**:
    - **Trigger**: Task available in `task_queue`.
    - **Action**: Worker claims task, uses Tools (read-only) to gather context, and generates a *result artifact*.
    - **Constraint**: Workers **cannot** perform side-effects (posting/paying). They can only *propose*.

3.  **Governance (The Judge)**:
    - **Trigger**: New Result in `review_queue`.
    - **Action**: Judge evaluates the result against `specs/functional.md` and safety guidelines.
    - **Decision**:
        - **Approve**: Calls the sensitive MCP Tool (write-access).
        - **Reject**: Sends feedback to Planner.
        - **Escalate**: Pauses for Human-in-the-Loop.

4.  **Completion**:
    - Global State is updated.
    - Planner marks the parent Goal as progress incremented.
