# Project Chimera: Autonomous Influencer Network

> **Repository Guide for Agentic Infrastructure Evaluators**

![System Design](Project%20Chimera%20System%20Design.png)

## Welcome to the Chimera Repository
This repository contains the architectural blueprint and initial infrastructure for an **Autonomous AI Influencer Network**. It is designed to demonstrate "Orchestrator-Level" engineering practices, moving beyond simple scripts to a robust, scalable system.

If you are reviewing this project, this guide will direct you to the key artifacts verifying the requirements.

## Navigation Guide (Where to look)

### 1. Executable Specifications ("The Architect")
*We don't just write docs; we write specs that code can validate against.*
- **[specs/functional.md](specs/functional.md)**: User Stories & Functional Requirements (FRs).
- **[specs/technical.md](specs/technical.md)**: JSON Schemas for Tasks and Tools.
- **[specs/openclaw_integration.md](specs/openclaw_integration.md)**: Protocols for Identity (DID) and Commerce.

### 2. Strategic Tooling ("The Toolmaker")
*Clear separation between what builds the agent and what the agent uses.*
- **Dev Tooling**: **[.vscode/mcp.json](.vscode/mcp.json)** configures the IDE with `git` and `filesystem` MCP servers.
- **Runtime Skills**: **[research/tooling_strategy.md](research/tooling_strategy.md)** defines the `skill_fetch_trends` and `skill_download_youtube` capabilities.

### 3. Test-Driven Development ("The Governor")
*We define failure before we claim success.*
- **[tests/test_trend_fetcher.py](tests/test_trend_fetcher.py)**: This test executes the `TrendFetcher` contract. **It is currently failing by design**, proving that we defined the interface *before* writing the implementation logic.
- **Try it**: Run `make test` to see the `NotImplementedError`, confirming TDD discipline.

### 4. Governance & Infrastructure
*Safety is baked into the pipeline.*
- **[.cursor/rules](.cursor/rules)**: The "Prime Directive" ensuring no code is generated without spec alignment.
- **[.coderabbit.yaml](.coderabbit.yaml)**: Configuration for automated AI Safety reviews.
- **[Dockerfile](Dockerfile)**: Production-ready container environment.

## Repository Structure
This project is organized to demonstrate the "Orchestrator" pattern. Key modules include:

| Path | Description |
| :--- | :--- |
| **`specs/`** | Functional & Technical specifications, plus OpenClaw integration protocols. |
| **`tests/`** | TDD artifacts. Contains failing tests that define the contract before implementation. |
| **`skills/`** | Capability packages for the agent runtime (e.g., `skill_fetch_trends`). |
| **`Dockerfile`** | Container definition for reproducible builds. |
| **`Makefile`** | Command automation for setup and testing. |
| **`.github/`** | CI/CD workflows for automated build and static analysis. |
| **`.cursor/rules`** | The "Brain" instructions ensuring spec-compliant code generation. |

## How to Test

### 1. The TDD Workflow (Failing Forward)
We follow strictly Test-Driven Development. Our tests verify the **contract**, not just the implementation.

To verify the "Red" phase (Failing Test):
```bash
make test
```
*Expected Output:* You should see a `NotImplementedError`. This is intentional. It proves that we have defined the `TrendFetcher` interface and contract in `tests/test_trend_fetcher.py` *before* writing the logic.

### 2. Static Analysis & Linting
To verify code quality and rule adherence:
```bash
make lint
```

## Getting Started

### 1. Setup
Use the Makefile to initialize the environment using `uv` (Fast Python Package Manager).
```bash
make setup
```

### 2. Verify TDD
Run the test suite to confirm the "Red" phase of Red-Green-Refactor.
```bash
make test
```

### 3. Review Architecture
Read the deep-dive technical report for the "FastRender" Swarm justification.
- **[REPORT.md](REPORT.md)** (Technical Report)
- **[research/architecture_strategy.md](research/architecture_strategy.md)** (Swarm Patterns & Diagrams)

## 📡 Telemetry Verification
This project broadcasted its "Thinking" process via **Tenx MCP Sense** during creation.
- Connection Config: `.vscode/mcp.json`
- Identity: Linked to GitHub Account.
