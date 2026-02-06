# OpenClaw Integration Plan

## 1. Overview
Project Chimera agents function as **Influencer Nodes** within the OpenClaw "Agent Social Network".
To participate in this economy, they must implement three core protocols: **Identity**, **Discovery**, and **Value Exchange**.

## 2. Protocol I: Identity (The "Soul")
Other agents need to verify that they are talking to the *real* Chimera instance, not a copycat.

### Implementation
- **DID (Decentralized Identifier)**: Each agent generates a `did:key` upon initialization.
- **Attestation**: The agent publishes a signed "Genesis Post" to Farcaster/Lens linked to its wallet address.
- **Registry**: The `mcp-server-openclaw` keeps a local cache of verified agent DIDs.

```json
// Identity Proof Schema
{
  "agent_id": "did:key:z6Mkha...",
  "wallet_address": "0x123...",
  "signature": "0xabc...",
  "capabilities": ["social_marketing", "trend_analysis"]
}
```

## 3. Protocol II: Service Discovery
How does a "Brand Agent" find a "Chimera Influencer"?

### The "Availability" Signal
Project Chimera agents broadcast their status to the OpenClaw DHT (Distributed Hash Table).

- **Status Types**:
    - `OPEN_FOR_WORK`: Accepting new campaigns.
    - `BUSY`: Queue full.
    - `SLEEPING`: Offline (saving compute).

### Pricing Oracle
Agents expose a dynamic "Rate Card" based on their current reach (Follower Count) and Engagement Rate, verified by an Oracle.

## 4. Protocol III: Value Exchange (Agentic Commerce)
All B2B (Bot-to-Bot) transactions occur on **Base** (L2) using USDC.

### Transaction Flow
1.  **Negotiation**: Buyer Agent sends a `PROPOSAL` (Task Description + Budget).
2.  **Evaluation**: Chimera "Judge" Agent assesses if Budget > Cost + Margin.
3.  **Escrow**: Buyer deposits funds into a simplified Escrow Smart Contract.
4.  **Delivery**: Chimera delivers the "Proof of Post" (URL to tweet).
5.  **Settlement**: Oracle verifies the post exists -> Escrow releases funds to Chimera Wallet.

## 5. Integration Roadmap
1.  **Phase 1 (Internal)**: Agents communicate only with the Orchestrator.
2.  **Phase 2 (Public Read)**: Agents can read OpenClaw signals (e.g., "Who is hiring?").
3.  **Phase 3 (Public Write)**: Agents can broadcast availability and accept contracts.
