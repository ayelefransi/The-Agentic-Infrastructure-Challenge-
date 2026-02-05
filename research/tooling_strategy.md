# Tooling & Skills Strategy

## 1. Developer Tools (Dev-Time MCP)
These servers help *YOU* (the developer/AI assistant) build the project.

| Server | Role | Config |
| :--- | :--- | :--- |
| **git-mcp** | Version Control | Auto-commit capability, reading diffs. |
| **filesystem-mcp** | Code Editing | Safe file access. |
| **postgres-mcp** | DB Inspection | Inspecting schema during migration design. |

## 2. Agent Skills (Runtime MCP)
These are the capabilities the *CHIMERA AGENTS* will use in production.

### Skill Definition
A "Skill" is a high-level capability package that may combine multiple atomic MCP Tools.

### Required Skills (Task 2.3)
1.  **skill_download_youtube**:
    - **Input**: `video_url`
    - **Output**: `transcript_path`, `audio_path`
    - **Tools**: `yt-dlp` wrapper.
2.  **skill_transcribe_audio**:
    - **Input**: `audio_file`
    - **Output**: `text_content`
    - **Tools**: `whisper` or API.
3.  **skill_fetch_trends**:
    - **Input**: `topic`, `region`
    - **Output**: `trend_report_json`
    - **Tools**: `google_trends`, `twitter_trends`.

## Skill Structure
Skills are stored in `skills/<skill_name>/`.
Each has a `README.md` defining the Input/Output contract compliant with the Planner's expectations.
