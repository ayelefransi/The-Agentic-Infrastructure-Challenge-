# Project Chimera Submission Report

## 1. Research Summary

### Key Insights
1.  **The Shift to Agency**: We are moving from "Chatbots" (reactive) to "Agents" (proactive, goal-directed). The a16z and OpenClaw materials highlight that agents need their own social network to transact and discover services, rather than just existing in silos.
2.  **Fractal Orchestration**: The "Solopreneur" model described in the SRS is only possible if we abstract complexity. A single human cannot manage 1,000 agents unless they are self-healing and organized hierarchically (Manager -> Worker Swarm).
3.  **Economic Independence**: Integrating **Coinbase AgentKit** is the critical unlocks. Agents without wallets are just toys; agents with wallets are businesses. They can pay for their own compute and negotiate with other agents.
4.  **Protocol over Platform**: By using **MCP (Model Context Protocol)**, we decouple the agent's "Brain" from the specific API implementation (Twitter vs Threads). This ensures longevity and resilience against platform volatility.

## 2. Architectural Approach

### Pattern: Hierarchical Swarm ("FastRender")
We chose the **FastRender Swarm** pattern over a monolithic agent or a sequential chain.
- **Why?**: Social media management is high-throughput. A serialized chain is too slow to reply to 50 comments. A Swarm allows us to spin up 50 "Worker" agents in parallel, managed by a persistient "Planner".
- **Safety**: The "Judge" role implements the necessary friction (Optimistic Concurrency Control) to ensure brand safety before any external action is taken.

### Infrastructure Decisions
1.  **Hybrid Database Strategy**:
    - **Weaviate** for the "Soul" (Long-term semantic memory).
    - **PostgreSQL** for the "Business" (Transactional accounts, firm constraints).
    - **Redis** for the "Swarm" (Ephemeral state, queues).
2.  **Governance**:
    - **Confidence-Based HITL**: We don't review everything. We only review low-confidence (< 0.7) or sensitive actions.
    - **Policy-Code Separation**: Rules are defined in `specs/`, enforced by `tests/`, and monitored by the "Judge" agent.

## 3. Tooling Strategy
- **MCP-First**: All external tools (Twitter, News, Crypto) are wrapped as MCP servers.
- **TDD**: We write failing tests (e.g., `test_trend_fetcher.py`) before implementing logic to ensure strict adherence to the spec.
