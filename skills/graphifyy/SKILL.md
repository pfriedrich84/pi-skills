---
name: graphifyy
description: Build, update, inspect, and query Graphify knowledge graphs for codebases, docs, papers, images, and mixed project folders. Use when the user asks to graph a repository, understand architecture or file relationships, create/query a knowledge graph, inspect blast radius, or use graphify/graphifyy.
license: MIT
compatibility: Requires Node.js and the graphifyy npm package. This pi-skills package declares graphifyy as an npm dependency; a globally installed `graphify` binary also works.
---

# Graphifyy

Use Graphifyy to turn a project or content folder into a persistent knowledge graph under `.graphify/`, then query it for architecture, relationships, impact analysis, or review context.

## Command resolution

Prefer the first available command:

```bash
command -v graphify >/dev/null 2>&1 && GRAPHIFY=graphify \
  || [ -x ../../node_modules/.bin/graphify ] && GRAPHIFY=../../node_modules/.bin/graphify \
  || GRAPHIFY="npx graphifyy"
```

When running from another directory, resolve the package-local binary relative to this skill directory if needed:

```bash
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
GRAPHIFY="$SKILL_DIR/../../node_modules/.bin/graphify"
```

If neither `graphify` nor the package-local binary exists, install or repair the package before continuing:

```bash
npm install
# or, for an operator-local fallback:
npm install -g graphifyy
```

## Default workflow

When the user does not specify a path, use the current directory (`.`). Do not ask for a path unless the detected corpus is unexpectedly huge or empty.

1. Inspect scope before expensive graphing:

   ```bash
   graphify scope inspect . --scope auto
   ```

2. Build or update the graph:

   ```bash
   graphify . --scope auto
   # incremental update after prior graph exists:
   graphify . --scope auto --update
   ```

3. Summarize outputs without dumping raw JSON:

   ```bash
   graphify summary --graph .graphify/graph.json
   ```

4. Query for the user's concrete question:

   ```bash
   graphify query "<question>" --graph .graphify/graph.json --budget 2000
   ```

## Common commands

```bash
# Safe default for Git repositories: committed files plus graphify memory
graphify <path> --scope auto

# Include newly staged files too
graphify <path> --scope tracked

# Full recursive crawl for knowledge-base folders, notes, papers, media
graphify <path> --all

# Incrementally update existing graph
graphify <path> --scope auto --update

# Build agent-crawlable wiki
graphify <path> --scope auto --wiki

# Skip visualization when only JSON/report are needed
graphify <path> --scope auto --no-viz

# Review impact/blast radius for changed files
graphify review-analysis --files src/file.ts --graph .graphify/graph.json

# Advisory commit grouping
graphify recommend-commits --files src/a.ts,src/b.ts --graph .graphify/graph.json

# Shortest path between two concepts
graphify path "ConceptA" "ConceptB" --graph .graphify/graph.json
```

## Scope policy

- Use `--scope auto` by default for code repositories.
- Use `--scope tracked` when staged-but-uncommitted files should be included.
- Use `--all` only for explicit knowledge-base/document-corpus requests.
- If the repo is dirty or the scope is unclear, run `graphify scope inspect` first and summarize what will be included/excluded.
- Do not include secrets, dependency folders, build outputs, caches, virtualenvs, or private runtime data intentionally.

## Safety and repository hygiene

- Treat `.graphify/` as runtime analysis state. Do not commit it unless the user explicitly asks to version graph artifacts.
- Do not print raw `.graphify/*.json` files in chat; summarize counts, communities, paths, and findings.
- Mention sensitive skipped-file counts only at a high level; do not reveal secret filenames or contents.
- For large corpora, warn before running long/expensive graph builds and suggest narrowing to a subfolder.
- Graphify output is analysis aid, not source of truth. Confirm important architectural conclusions against source files before editing.

## When to use

Use this skill for:

- onboarding to an unfamiliar repository;
- architecture and dependency relationship questions;
- blast-radius analysis before a change;
- review context for a set of files;
- creating or updating a queryable knowledge graph/wiki;
- exploring docs, papers, notes, screenshots, transcripts, or mixed corpora.
