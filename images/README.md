# images/

Screenshots of [Herdr](https://herdr.dev) 0.8.0 running real Claude Code agents, captured on 2026-10-07 on a 5120×1440 (32:9) ultrawide.

## How they were made

- **Isolated session.** Everything ran in a throwaway named session (`herdr --session presodemo`) in its own iTerm window, so my everyday Herdr session was never touched.
- **Throwaway repos.** Four small demo projects (`transit-tracker`, `ledger-service`, `storefront-web`, `project-notes`), each its own git repo, created in `/tmp` for the occasion.
- **Scripted layout.** Spaces, tabs, splits, and prompts were all driven through the Herdr CLI and socket API (`herdr workspace create`, `herdr tab rename`, `herdr pane split`, `herdr pane run`, `herdr agent prompt`).
- **Read-only agents.** Every agent ran as `claude --permission-mode plan`, so nothing was written to the demo repos. The prompts, and the agents' answers, are real.
- **Cleaned up afterward.** The demo session was stopped and deleted, the window closed, and the demo repos, agent transcripts, and plan files removed.

## The files

| File | Size | What it shows |
|---|---|---|
| `01-ultrawide-domain-modeling-tab.png` | 5120×1415 | `ledger-service` space, **domain-modeling** tab: an agent column on the left; domain notes over git history on the right |
| `02-ultrawide-implementation-tab.png` | 5120×1415 | **implementation** tab: two scoped agents side by side, diffstat stacked over a shell |
| `03-ultrawide-agent-blocked-on-scope.png` | 5120×1415 | The same tab earlier, while the middle agent is **blocked**, asking a scoping question |
| `04-ultrawide-pr-reviews-tab.png` | 5120×1415 | **pr-reviews** tab: reviewer findings on the left, the raw diff on the right |
| `05-ultrawide-second-space-implementation.png` | 5120×1415 | A second space (`transit-tracker`) with its own implementation tab |
| `06-ultrawide-third-space-pr-review.png` | 5120×1415 | A third space (`storefront-web`): a money-handling review next to its diff |
| `07-half-ultrawide-implementation-16x9.png` | 2560×1415 | The implementation tab squeezed into half the width, i.e. a normal 16:9 screen, for comparison |
| `08-crop-sidebar-spaces-and-agents.png` | 190×1415 | Sidebar: spaces up top, every agent with its state dot below |
| `09-crop-agent-asks-about-scope.png` | 1640×540 | Close-up: a `Scope: cmd/main.go only` agent stops and asks instead of wandering out of bounds |
| `10-crop-pr-review-findings.png` | 2460×640 | Close-up: reviewer output, numbered and classified additive / mutative / destructive with `file:line` |
| `11-crop-domain-model-output.png` | 2460×1120 | Close-up: the Posting aggregate model, using only the agreed vocabulary, with inferred rules marked |

The heights are 1415 rather than 1440 because the macOS menu bar is cropped out.
