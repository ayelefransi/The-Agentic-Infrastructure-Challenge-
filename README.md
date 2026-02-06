# Project Chimera: Autonomous Influencer Network

> **Transitioning from Automated Scripts to Autonomous Agency.**

![System Design](Project%20Chimera%20System%20Design.png)

## Overview
Project Chimera is a submission for the Agentic Infrastructure Challenge (2026). It implements a **Fractal Orchestration** system that allows a single human operator to manage a scalable fleet of autonomous AI influencers ("Chimeras").

Unlike traditional chatbots, Chimera agents possess:
1.  **Identity**: A persistent "Soul" defined by vector embeddings.
2.  **Connectivity**: Universal interaction via the **Model Context Protocol (MCP)**.
3.  **Economy**: Financial sovereignty via **Coinbase AgentKit** and non-custodial wallets.

## System Architecture: The "FastRender" Swarm
We utilize a hierarchical swarm pattern to manage high-concurrency workloads.

- **Planner (The Brain)**: Decomposes high-level goals (e.g., "Promote Summer Sale") into atomic tasks. Uses high-reasoning models (Gemini 1.5 Pro).
- **Worker (The Hands)**: Stateless, ephemeral agents that execute tasks in parallel. Uses high-speed models (Gemini Flash).
- **Judge (The Conscience)**: A governance layer that enforces **Optimistic Concurrency Control**. It reviews every worker output for safety, brand consistency, and budget compliance before committing it.

## Key Features
- **MCP-First Design**: All external tools (Twitter, News, Crypto) are decoupled from the agent core.
- **Agentic Commerce**: Built-in "CFO" governance allows agents to autonomously pay for compute and transact on Base (L2).
- **Polyglot Persistence**: Hybrid architecture using Weaviate (Semantic Memory), PostgreSQL (Transactional Ledger), and Redis (Swarm State).

## Getting Started

### Prerequisites
- Python 3.11+
- Docker
- `uv` (for fast package management)

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/project-chimera.git
    cd project-chimera
    ```

2.  **Set up the environment**:
    ```bash
    make setup
    ```

3.  **Run Tests (TDD Verification)**:
    ```bash
    make test
    ```
    *Note: Tests are expected to verify the "Failing First" TDD requirement.*

## Documentation
- **Technical Report**: [REPORT.md](REPORT.md) - Deep dive into architecture and research.
- **Architecture Strategy**: [research/architecture_strategy.md](research/architecture_strategy.md)
- **OpenClaw Integration**: [specs/openclaw_integration.md](specs/openclaw_integration.md)

## Telemetry
This project is instrumented with **Tenx MCP Sense** to visualize the agent's reasoning process. Ensure the Sense desktop app is running during execution.
