# pi-skills

Personal Pi package containing the skills, extensions, and non-secret configuration I use.

## Contents

- `skills/` — Pi skills discovered by convention.
- `extensions/` — Pi extensions discovered by convention.
- `config/agent-settings.json` — non-secret snapshot of `~/.pi/agent/settings.json`.
- `config/pi-config.json` — non-secret snapshot of `~/.pi/config.json`.

## Install as a Pi package

```bash
pi install https://github.com/pfriedrich84/pi-skills.git
```

The package manifest exposes `skills/` and `extensions/` to Pi.

## Restore config manually

Review before copying. These files intentionally exclude secrets.

```bash
mkdir -p ~/.pi/agent
cp config/agent-settings.json ~/.pi/agent/settings.json
cp config/pi-config.json ~/.pi/config.json
```

## Excluded intentionally

- `~/.pi/agent/auth.json` and any credentials/tokens.
- Session history, run history, todos, caches, package clones, and project repositories.
- Installed binaries and dependency folders.

## Included skills

- `clawpatch`
- `grill-me`
- `grill-with-docs`
- `improve-codebase-architecture`
- `tune-repo`

## Included extensions

- `answer.ts`
- `review.ts`
- `todos.ts`
