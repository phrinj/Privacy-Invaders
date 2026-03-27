# Privacy Invaders

A space shooter that deletes Claude Code's unencrypted plaintext logs from your machine.

## Run

```
python "C:\Users\phrinj\Desktop\Privacy-Invaders\privacy_invaders.py"
```

Run from each directory that has a `.claude/` folder. The game scans for Claude data, shows what it found, and deletes it when you press a key.

**Preserves:** `.claude/.credentials.json` (OAuth) and `.claude/settings.json` (preferences).

**Deletes:** conversation transcripts, prompt history, debug logs, file snapshots, shell snapshots, telemetry, memory files, cached data.

Run only when Claude Code is idle. Don't run it during an active session.

Requires Python 3.6+.

## What Claude Code stores

Claude Code writes everything to `~/.claude/` and `~/.claude.json` in unencrypted plaintext with no automatic cleanup:

- Full conversation transcripts (every message sent and received)
- Every prompt you've typed, including typos and deleted text
- Your email, project paths, GitHub repo mappings
- File edit snapshots, shell state captures
- Memory files that can contain IP addresses, SSH configs, network topology
- Telemetry and debug logs

A few hours of use generates ~10MB across 335 files. Months of regular use: 1.4GB+.

Reported as [GitHub issue #2713](https://github.com/anthropics/claude-code/issues/2713) in June 2025. Closed as NOT_PLANNED.

## Opt-out environment variables

These reduce what gets sent to Anthropic's servers but do NOT stop local logging:

| Variable | What It Disables |
|----------|-----------------|
| `DISABLE_TELEMETRY=1` | Statsig metrics |
| `DISABLE_ERROR_REPORTING=1` | Sentry error logging |
| `DISABLE_BUG_COMMAND=1` | `/bug` command |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` | All of the above |

## Similar tools

- [CC-Cleaner](https://github.com/tk-425/CC-Cleaner) — Web GUI for browsing and cleaning Claude data
- [Claude Config Editor](https://github.com/gagarinyury/claude-config-editor) — Python web tool for bulk history deletion
- [ClawCare](https://github.com/natechensan/ClawCare) — Security scanner for AI agent plugins

## License

MIT
