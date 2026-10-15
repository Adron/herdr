# herdr-preso-demo

**Herding Agents: Herdr, an ultrawide, and precise words.**

Material for a talk and blog series by [Adron Hall](https://compositecode.blog/) on how I run several AI coding agents at once (Claude Code, Codex, Cursor) with [Herdr](https://herdr.dev) on a 5120×1440 ultrawide, and how I prompt them so they stay effective and accurate.

Created 2026-10-07. Screenshots are from Herdr 0.8.0.

## What's in here

```
herdr-preso-demo/
├── articles/
│   ├── 01-herding-agents-with-herdr.md      # What Herdr is, how it works, how I lay it out
│   └── 02-why-i-break-it-out-this-way.md    # Why I split it that way, and how I prompt in the panes
├── images/                                  # Screenshots of Herdr running real agents (see images/README.md)
├── presentation/
│   ├── herding-agents.key                   # Keynote deck, stock "Basic White" theme
│   ├── herding-agents.pptx                  # PowerPoint deck, stock "Office Theme"
│   └── build/
│       ├── slides.json                      # Single source for both decks: slide text, images, speaker notes
│       ├── build_keynote.py                 # Rebuilds the .key natively through Keynote (AppleScript)
│       └── build_pptx.py                    # Rebuilds the .pptx with python-pptx
├── topics.md                                # Slide-by-slide topic guide with links, commands, and screenshots
├── LICENSE                                  # MIT
└── README.md
```

### `articles/`

Two posts written for [Composite Code](https://compositecode.blog/), in Markdown with front matter, ready to paste into WordPress. Images use relative paths into `../images/`.

1. **[Herding Agents: How I Actually Use Herdr (on a Ridiculously Wide Screen)](articles/01-herding-agents-with-herdr.md)**: what Herdr is (a terminal workspace manager for coding agents: one Rust binary, a background server, agent-state detection), its model (session › space › tab › pane), the keys and CLI I actually use, and my layout: **one space per folder, one tab per kind of work** (`pr-reviews`, `domain-modeling`, `implementation`), and **agents in tall vertical splits, shells in short horizontal ones**.
2. **[Spaces, Tabs, Panes, and Precise Words](articles/02-why-i-break-it-out-this-way.md)**: the reasoning behind that layout (context management for me and for the models, verb drift, one agent per job, why 32:9 matters), followed by the prompting practices that keep agents accurate: domain vocabulary, scope first, precise verbs, specified output shapes, front-loaded context, and a prompt template that works across Claude, Codex, and Cursor. It links back to a dozen earlier Composite Code posts.

### `images/`

Eleven PNGs: full-width 5120×1415 captures of each tab, a 16:9 comparison, and readable close-ups of the sidebar and of real agent output. They were captured in an **isolated, throwaway Herdr session** against throwaway demo repos, with agents in read-only plan mode, and everything was torn down afterward. [`images/README.md`](images/README.md) lists every file and how it was made.

### `presentation/`

The same talk as two decks, built in the **[Presentation Zen](https://garrreynolds.com/)** style: one idea per slide, mostly screenshots, a handful of words, and the actual narrative in the **speaker notes**, with links to the Herdr docs and related posts.

- **`herding-agents.key`**: native Keynote, stock **Basic White** theme, built on Keynote's own master slides (Title, Statement, Big Fact, Title & Bullets, Title Only). To restyle it, use **File › Change Theme…**.
- **`herding-agents.pptx`**: PowerPoint, stock **Office Theme** (16:9), built on PowerPoint's standard layouts and placeholders. To restyle it, pick any theme on the **Design** tab.

Both decks come from `presentation/build/slides.json`. Edit that file, then rebuild:

```bash
python3 presentation/build/build_keynote.py        # needs Keynote; standard library only
python3 -m pip install python-pptx pillow
python3 presentation/build/build_pptx.py
```

## Links

- Herdr: [herdr.dev](https://herdr.dev) · [docs](https://herdr.dev/docs/) · [GitHub](https://github.com/herdrdev/herdr)
- Blog: [compositecode.blog](https://compositecode.blog/)

## License

[MIT](LICENSE) © 2026 Adron Hall. The screenshots show Herdr and Claude Code, which belong to their respective owners. The license covers the writing, decks, build scripts, and screenshot compositions in this repo.
