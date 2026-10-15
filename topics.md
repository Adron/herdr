# Herding Agents: Topics

A walk through the topics in the *Herding Agents* deck (`presentation/herding-agents.key` / `.pptx`), in slide order, with the links, commands, screenshots, and other things each one points to. The full narrative is in each slide's speaker notes and in the two articles:

- [`articles/01-herding-agents-with-herdr.md`](articles/01-herding-agents-with-herdr.md): what Herdr is and how I lay it out
- [`articles/02-why-i-break-it-out-this-way.md`](articles/02-why-i-break-it-out-this-way.md): why I lay it out that way, and how I prompt

> **Source of truth:** every slide's text, image, and speaker notes live in [`presentation/build/slides.json`](presentation/build/slides.json). Edit that, then rebuild both decks (see the [README](README.md#presentation)).

---

## Part 1: The problem

### 1. Herding Agents: *Herdr, an ultrawide, and precise words*
The setup for the talk: several AI coding agents at once (Claude Code, Codex, Cursor), kept on track by three things: Herdr, a 5120×1440 monitor, and precise prompts.

- 🔗 [herdr.dev](https://herdr.dev) · [compositecode.blog](https://compositecode.blog/)

### 2. "One agent is a tool. Six is a zoo."
The opening tension. The expensive failure isn't an agent doing the wrong thing. It's an agent doing **nothing**, sitting on a yes/no question for twenty minutes. Wall-clock time is the scarce resource.

> 💡 Speaker cue: pause here and let it land.

### 3. A normal Tuesday
The full ultrawide: one Herdr window, the `ledger-service` space, the implementation tab. The middle agent is **blocked** on a scoping question, which the second half of the talk pays off.

- 🖼️ [`images/03-ultrawide-agent-blocked-on-scope.png`](images/03-ultrawide-agent-blocked-on-scope.png)
- ℹ️ Every screenshot was taken on Herdr 0.8.0, in an isolated named session, against throwaway repos, with Claude Code in plan mode. See [`images/README.md`](images/README.md).

---

## Part 2: Herdr

### 4. Herdr
What it is, in four lines:
- A terminal workspace manager built for coding agents (Claude Code, Codex, Cursor, Copilot CLI, OpenCode, Devin, and others)
- A single Rust binary that runs **inside** your existing terminal (iTerm, Ghostty, WezTerm, kitty, Alacritty, tmux)
- Client/server: detach or drop SSH and the agents keep working
- Agent-state detection: it knows when an agent needs you

- 🔗 [herdr.dev](https://herdr.dev) · [GitHub: herdrdev/herdr](https://github.com/herdrdev/herdr)

### 5. Installs in one line
How little setup it takes: install, run, and (optionally) wire up the agent hooks.

```bash
brew install herdr                              # macOS
curl -fsSL https://herdr.dev/install.sh | sh    # Linux
herdr                                           # starts the server, attaches to the default session
herdr integration install claude                # optional: agent reports its own state (also codex, copilot, opencode…)
```

- ✅ No runtime, no Electron, no config file needed to start.

> 🪟 **Windows note:** Herdr runs natively on Windows (x86_64; ARM64 runs the x86_64 build under emulation). Install from PowerShell:
>
> ```powershell
> powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
> ```
>
> If endpoint security blocks that, use Command Prompt instead:
>
> ```cmd
> curl.exe -fsSLo install.cmd https://herdr.dev/install.cmd && install.cmd && del install.cmd
> ```
>
> The installer puts `herdr` on your PATH. Windows is generally available but has documented limitations, so read [Windows support](https://herdr.dev/docs/windows-beta/) first. Older Windows *preview* installs stay on the preview channel until you run `herdr channel set stable`.

- 🔗 [Install](https://herdr.dev/docs/install/) · [Windows support](https://herdr.dev/docs/windows-beta/) · [Quick start](https://herdr.dev/docs/quick-start/) · [Supported agents](https://herdr.dev/docs/agents/)

### 6. Session › Space › Tab › Pane
Herdr's four nouns:

| Noun | Herdr's definition |
|---|---|
| Session | A persistent server namespace (`herdr --session <name>` for an isolated one) |
| Workspace / space | "The top-level project container. Use one workspace per repo, task, or investigation." |
| Tab | "A layout inside a workspace." |
| Pane | "A real terminal." |

- 💡 If you know tmux, you already have most of this model.
- 🔗 [Concepts](https://herdr.dev/docs/concepts/)

### 7. Blocked. Working. Done. Idle.
The sidebar: spaces at the top, every agent below with a state dot. **Blocked** is the one that matters. This is the "tap on the shoulder" agents never give you on their own.

- 🖼️ [`images/08-crop-sidebar-spaces-and-agents.png`](images/08-crop-sidebar-spaces-and-agents.png)
- ⌨️ `herdr integration install claude` · `herdr integration status`
- 🔗 [Concepts](https://herdr.dev/docs/concepts/) · [Agents](https://herdr.dev/docs/agents/)

---

## Part 3: The layout rules

### 8. Rule one: One space per folder
An agent's working directory is the edge of its world, so each space draws that same boundary on screen. There is no "misc" space, because misc is where context goes to die.

- ⚙️ Config: `agent_panel_sort = "spaces"`

### 9. Spaces mirror my head
A second space (`transit-tracker`). The sidebar becomes a readout of my working memory.

- 🖼️ [`images/05-ultrawide-second-space-implementation.png`](images/05-ultrawide-second-space-implementation.png)
- ⌨️ `herdr worktree create`: two agents on one repo each get their own worktree, which means a new folder and so a new space.
- 🔗 [Giving Every Agent Its Own Branch: Git Worktrees for Parallel AI Work](https://compositecode.blog/2026/08/19/worktrees/)

### 10. Rule two: One tab per kind of work
Tabs are modes, and each mode is a verb:
- `domain-modeling`: **think** (plan mode, no typing)
- `implementation`: **change** (inside an explicit scope, after an approved plan)
- `pr-reviews`: **judge** (read and report, no fixing)

- ⚠️ The thing this guards against is **verb drift**, like a reviewer that slides into rewriting the module.
- 🔗 [Ask, Plan, Confirm](https://compositecode.blog/2026/08/20/plan-then-build/)

### 11. domain-modeling
An agent column on the left, with domain notes, entity code, and git history on the right so I can check its vocabulary against the agreed vocabulary.

- 🖼️ [`images/01-ultrawide-domain-modeling-tab.png`](images/01-ultrawide-domain-modeling-tab.png)

### 12. implementation
Two agents, each fenced to its own slice of the code, with a diffstat over a shell so I can see what actually changed.

- 🖼️ [`images/02-ultrawide-implementation-tab.png`](images/02-ultrawide-implementation-tab.png)
- 🔗 [Git worktrees for parallel AI work](https://compositecode.blog/2026/08/19/worktrees/)

### 13. pr-reviews
The reviewer on the left and the raw diff on the right. Every `file:line` it cites can be checked just by looking across. The reviewer is read-only, and a fix becomes a new, scoped task.

- 🖼️ [`images/04-ultrawide-pr-reviews-tab.png`](images/04-ultrawide-pr-reviews-tab.png)

### 14. Rule three: Tall for agents. Short for shells.
Agents produce long, structured output, so they get full-height vertical splits. Shells, test runners, and `git log` are things you glance at, so they get short horizontal splits. One pane holds one agent with one context window doing one job.

- ⌨️ Keys (prefix `ctrl+b`): `v` split vertical · `-` split horizontal · `h/j/k/l` move · `z` zoom · `r` resize · `c` new tab · `shift+n` new space · `w` space picker · `b` sidebar · `q` detach · `?` help
- 🔗 [Configuration](https://herdr.dev/docs/configuration/)

---

## Part 4: The ultrawide

### 15. 32:9 (5120 × 1440)
The cheat code: two 2560×1440 screens fused together with no bezel. That fits three or four full-height agent columns, a utility column, and the sidebar, all visible at once.

### 16. Half the screen
The same tab at 16:9. It works, but it's tight, and a third agent means zooming panes in and out all day.

- 🖼️ [`images/07-half-ultrawide-implementation-16x9.png`](images/07-half-ultrawide-implementation-16x9.png)

### 17. The whole screen
Nothing is hidden. The sidebar tells you *that* an agent is blocked, and having it on screen tells you *why*, in your peripheral vision.

- 🖼️ [`images/02-ultrawide-implementation-tab.png`](images/02-ultrawide-implementation-tab.png)

---

## Part 5: Precise words

### 18. Words are the interface
The turn in the talk: everything so far is plumbing, and the water is language. A vague word in an agent prompt gets you a nine-file diff.

- 🔗 [Precision in Words, Precision in Code](https://compositecode.blog/2024/12/09/precision-in-words-precision-in-code-the-power-of-writing-in-modern-development/)
- 🔗 [AI Prompt Engineering: Mastering Language Constructs](https://compositecode.blog/2025/02/25/ai-prompt-engineering-mastering-language-constructs/)

### 19. Use the glossary. Ban the rest.
Ubiquitous language from DDD. The prompt allows only *Account, Entry, Journal, Posting* and bans "transaction", which is overloaded in a ledger. The model stays inside that vocabulary and marks which rules it inferred.

- 🖼️ [`images/11-crop-domain-model-output.png`](images/11-crop-domain-model-output.png)
- 💬 Prompt: *"Using only the domain terms Account, Entry, Journal, and Posting (never 'transaction'), describe a Posting aggregate… Do not write code."*
- 🔗 [Notes repos as shared project context](https://compositecode.blog/2026/09/25/notes-repos-as-shared-project-context/) · [Fowler: Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html)

### 20. Scope first
Put the scope first: a positive fence, a negative fence, and a size limit as a number. The agent hit a decision that would have taken it out of scope, so it stopped, went **blocked**, and asked. Herdr flagged it, and answering took one keystroke.

- 🖼️ [`images/09-crop-agent-asks-about-scope.png`](images/09-crop-agent-asks-about-scope.png)
- 💬 Prompt: *"Scope: cmd/main.go only… Do not touch internal/ledger. Keep the planned diff under 50 lines."*
- 🔗 [Hurting or Helping Devs?](https://compositecode.blog/2026/04/15/hurting-or-helping-devs/)

### 21. Review means review
Use precise verbs, because review isn't fix. The prompt sets the output shape (a numbered list with `file:line`) so each finding can be checked against the diff. The reviewer also caught behavioral drift nobody asked about.

- 🖼️ [`images/10-crop-pr-review-findings.png`](images/10-crop-pr-review-findings.png)
- 💬 Prompt: *"Classify every change as additive, mutative, or destructive… numbered list with file:line. Do not propose rewrites outside the diff."*
- 🔗 [Additive vs. Mutative vs. Destructive Code Changes](https://compositecode.blog/2026/02/12/additive-vs-mutative-vs-destructive-code-changes-and-why-ai-agents-love-the-wrong-one-at-213am/)

### 22. The prompt shape
The template, which works the same in Claude Code, Codex, and Cursor:

```text
Scope: <paths> only. Do not touch: <paths>.
Context: Read <files / glossary / plan>. Use the terms <A, B, C>; never <overloaded term>.
Task (plan | implement | review): <one sentence, one job>.
Constraints: additive only | under N lines | no new dependencies | tests first.
Output: numbered list | file:line | severity first | test names first.
If anything above is ambiguous or blocks you, stop and ask.
```

- ⭐ The last line matters most, because it turns a silent stall into a visible **blocked** dot.
- 🔗 [Loop Engineering Is Mostly Just Broken SDLC Wearing a Costume](https://compositecode.blog/2026/07/15/loop-engineering-is-mostly-just-broken-sdlc-wearing-a-costume/) · [Agent-ready local environments and MCP](https://compositecode.blog/2026/09/24/agent-ready-local-environments-and-mcp/)

### 23. Ask. Plan. Confirm.
The gate: no edits until the agent has asked its questions, shown a plan, and gotten a yes. Approval covers only that plan, and if the work grows past it, the agent re-plans.

- ⌨️ `claude --permission-mode plan` (Codex and Cursor have their own read-only and ask-first modes)
- 🔁 My side of the loop: **Blocked** means answer in place, and log the decision in the notes repo. **Done** means check against the evidence pane. **Finished** means end the conversation.
- 🔗 [Ask, Plan, Confirm](https://compositecode.blog/2026/08/20/plan-then-build/)

---

## Part 6: Wrap-up

### 24. Try it
`brew install herdr` → `herdr` → `ctrl+b ?`. Then make a space per folder, name your tabs for the kind of work, put agents tall and shells short, and install the integrations.

- ⌨️ `herdr workspace create --cwd <dir> --label <name>` · prefix `shift+n` (new space) · prefix `shift+t` (name tab)
- 🔗 [Quick start](https://herdr.dev/docs/quick-start/) · [Configuration](https://herdr.dev/docs/configuration/)

### 25. Thanks
"Draw the boundaries on screen. Draw them again in words. Then let the agents work."

- 📄 [Article 01](articles/01-herding-agents-with-herdr.md) · [Article 02](articles/02-why-i-break-it-out-this-way.md) · [Screenshots](images/)
- 🔗 [herdr.dev](https://herdr.dev) · [GitHub](https://github.com/herdrdev/herdr) · [compositecode.blog](https://compositecode.blog/) · [Garr Reynolds, Presentation Zen](https://garrreynolds.com/)
