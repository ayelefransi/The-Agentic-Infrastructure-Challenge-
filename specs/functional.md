# Functional Requirements (SRS Section 4)

## FR 1.0: Cognitive Core & Persona
- **Persona Instantiation**: Defined via `SOUL.md` (Backstory, Voice, Beliefs).
- **Memory**:
    - Short-Term: Redis (last 1 hour).
    - Long-Term: Weaviate (Semantic RAG).
- **Context Construction**: Dynamic injection of SOUL + Memory into System Prompt.

## FR 2.0: Perception System (Data Ingestion)
- **Active Monitoring**: Polling `news://`, `twitter://` MCP Resources.
- **Semantic Filtering**: LLM-based relevance scoring before creating Tasks.
- **Trend Spotter**: Background worker analyzing aggregated data for "Trend Alerts".

## FR 3.0: Creative Engine
- **Multimodal**: Text (LLM), Images (Ideogram/Midjourney), Video (Runway/Luma).
- **Consistency**: Hard enforcement of `character_reference_id` / LoRA for all visual generation.
- **Tiered Video**: "Living Portrait" (Cheap) vs "Text-to-Video" (Expensive) based on budget.

## FR 4.0: Action System
- **Platform Agnostic**: All social actions via MCP Tools (`twitter.post_tweet`).
- **Interaction Loop**: Ingest -> Plan -> Generate -> Act -> Verify.

## FR 5.0: Agentic Commerce
- **Wallet**: Non-custodial wallet via Coinbase AgentKit.
- **Transactions**: `native_transfer`, `deploy_token`, `get_balance`.
- **CFO Governance**: "CFO Judge" enforces daily spend limits (e.g., $50/day).

## FR 6.0: Orchestration & Governance
- **FastRender Pattern**:
    - **Planner**: Decomposes Goals -> Tasks.
    - **Worker**: Executes Tasks (Stateless).
    - **Judge**: Validates Results (Quality + Safety).
- **OCC**: Optimistic Concurrency Control using `state_version` checks.
