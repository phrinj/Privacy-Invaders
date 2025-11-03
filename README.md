# Privacy Invaders 🎮

## The Space Shooter Game That Nukes Claude's Privacy Violations

**Play a literal video game to protect your privacy from Claude Code's aggressive data logging!**

![Game Preview](https://img.shields.io/badge/Genre-Space%20Shooter-brightgreen) ![Privacy](https://img.shields.io/badge/Privacy-Protected-blue) ![Fun](https://img.shields.io/badge/Fun%20Factor-Maximum-ff69b4)

## 🚨 The Privacy Crisis (Still Happening)

Claude Code logs EVERYTHING you type - even partial keystrokes - and stores your email in plain text. GitHub issue #2713 has been ignored since June 28, 2025.

**📺 Watch me explain the game**: https://youtu.be/aUUbb212KPs?si=uFwgiCk6JiEfvB4h

## 🎮 The Solution: We Made It FUN!

We tried automatic cleaning. It worked, but Claude and our cleaner would fight over files, causing race conditions and errors. Plus, watching a counter increment isn't exactly thrilling.

So we pivoted: **Why fight file systems when you can fight space invaders?**

Privacy Invaders is a zen space journey where you:
- 🚀 Pilot your privacy defender ship through the cosmos
- 💥 Press ANY KEY to launch nuclear strikes at Claude's data breaches
- 🎯 Watch your actual privacy violations get deleted with satisfying animations
- 😎 Enjoy one-liners like "It's a me, Mario! And Mario's pissed about privacy violations!"

## ✨ Latest Features (November 2025)

- **OAuth Preservation**: The `.claude/.credentials.json` file is preserved so you stay logged in after nuking - no re-authentication needed! We learned this the hard way.
- **Complete Transparency**: Watch EVERY file scroll by - dozens for light users, hundreds or THOUSANDS for heavy users. The endless scroll is a feature, not a bug!
- **Streamlined Interface**: No quit button, no welcome screen - just pure privacy destruction. Press ANY key and watch the show.
- **One-Liners That Actually Show**: Fixed bug where epic one-liners like "ULTRA KILL...ed a potential data breach" were selected but never displayed. Now you get the punchline!
- **No More Awkward Pauses**: Removed the 2-second artificial delay - one-liners now display immediately while files are being enumerated.
- **One-Liners Stay Visible**: The one-liner now stays on screen throughout the entire credits sequence until the game exits, instead of disappearing.
- **Instructions Disappear on Launch**: "Press any key" text now hides immediately when you fire, keeping the screen clean during the nuke sequence.
- **Verified Deletion**: Confirmed to delete ALL Claude Code tracking data as of Nov 2, 2025. We checked. Every. Single. File.
- **Easter Egg**: For those brave enough to peek at their .claude.json afterward... 🦖

## ⚠️ CRITICAL WARNING: When NOT to Play

**DO NOT run this game while Claude Code is actively thinking or processing a response!**

If you launch the privacy nuke while waiting for Claude Code to answer, you can create a race condition that causes Claude Code to glitch out or crash. This happens because:
- Claude Code is trying to write/read files
- The game is deleting those same files
- Result: Confused AI, broken sessions, bad times

**Safe times to play:**
- ✅ When you're NOT actively waiting for a Claude Code response
- ✅ Between conversations when Claude Code is idle
- ✅ After you've finished a task and Claude Code isn't working on anything

**Unsafe times to play:**
- ❌ While Claude Code is "thinking" or "working"
- ❌ While you're waiting for a response from Claude Code
- ❌ During active file operations or git commits

**Rule of thumb:** If you see Claude Code's status indicator showing activity, wait until it's done before firing the nuke!

## 🕹️ How to Play

1. **Install the game:**
```bash
git clone https://github.com/phrinj/claude-privacy-cleaner.git
cd claude-privacy-cleaner
```

2. **Launch Privacy Invaders:**
```bash
python privacy_invaders.py
```

3. **Controls:**
   - **Press ANY KEY** = Launch the privacy nuke (no going back!)
   - That's it! The game auto-exits after the show. Maximum destruction, zero distractions.

```

When you fire, you'll see:
- Missiles launching from your ship
- Claude's data planet exploding
- **ENDLESS SCROLL** of EVERY. SINGLE. FILE. being deleted - could be dozens, hundreds, or THOUSANDS!
- Each file path scrolling by like movie credits (grab the popcorn for heavy users!)
- Your privacy being restored AND you stay logged in (OAuth preserved!)

## 💭 Why This Approach Works Better

**The Automatic Cleaner Problem:**
- Claude writes files → Cleaner deletes files → Claude writes again → Race condition!
- Result: `OSError: [WinError 145] The directory is not empty` everywhere
- Fighting file systems is like playing whack-a-mole with errors

**The Game Solution:**
- YOU decide when to nuke your data (no race conditions when Claude is idle!)
- It's actually enjoyable to protect your privacy
- Watching files explode > watching error messages
- Manual control = no file conflicts (as long as you wait for Claude to finish thinking!)
- Play between tasks, not during them

## 📊 What Gets Nuked

✅ **VERIFIED as of November 2, 2025** - We tested EVERY file path!

Each time you fire, the game deletes:
- `~/.claude.json` - Surgically cleaned of tracking data while preserving OAuth
- `~/.claude/` - ENTIRE directory tree nuked, then rebuilt with only essentials:
  - `/file-history/*` - DELETED - Every version of every file you've edited
  - `/projects/*` - DELETED - All session data and conversation logs
  - `/shell-snapshots/*` - DELETED - Every command you've ever run
  - `/debug/*` - DELETED - All debug logs Claude secretly keeps
  - Plus dozens more hidden directories and files - ALL DELETED!

What survives (because we're not monsters):
- **`.claude/.credentials.json`** - OAuth tokens preserved! You stay logged in!
- MCP server configurations (needed for functionality)
- Your sanity (no more privacy paranoia!)

🦖 **Easter Egg Alert**: Check your `~/.claude.json` after playing for a surprise...

## 🤔 FAQ

**Q: Why a game instead of an automatic tool?**
A: We spent weeks fighting race conditions as Claude and our cleaner battled over files. Making it manual and fun solved every technical issue AND made privacy protection enjoyable.

**Q: Do I need to keep it running?**
A: No! Play whenever you want to clear your data. Once a day, once a week, or after sensitive conversations.

**Q: When is it safe to run this?**
A: ONLY when Claude Code is idle and not processing anything. DO NOT run while Claude Code is thinking, working, or waiting to respond - this creates race conditions that can crash your session. Wait until Claude Code is done before launching the nuke!

**Q: Will this break Claude Code?**
A: Not if you run it at the right time! Claude rebuilds what it needs. Just don't run it WHILE Claude is actively working - that's when race conditions happen. Run it between tasks when Claude is idle.

**Q: Do I have to log in again after cleaning?**
A: NO! The `.claude/.credentials.json` file (containing OAuth tokens) is preserved. You stay logged in. Finally, Claude remembers SOMETHING you'd want to keep!

**Q: How many files will be deleted?**
A: Depends on your usage. Light users: dozens. Regular users: hundreds. Power users who've never cleaned: THOUSANDS! The credits will scroll endlessly. Grab popcorn.

**Q: Is this actually effective?**
A: 100%. Every file shown in the deletion credits is really deleted. Verified Nov 2, 2025. We checked EVERY path.

**Q: What's this easter egg?**
A: Check your `~/.claude.json` after playing... Let's just say Dennis Nedry would be proud. 🦖

**Q: Can I automate this?**
A: You could, but then you're back to race conditions. Plus, you'd miss the explosions AND the endless file scroll!

## 🎨 The Philosophy

Privacy protection shouldn't feel like a chore. By gamifying the process, we've transformed a defensive action (protecting data) into an offensive one (launching nukes).

Every explosion is a small victory. Every deleted file is points on the board. Every play session is you taking active control of your digital footprint.

**Most importantly**: This makes the invisible visible. You SEE each file that contained your data. You WATCH it get destroyed. You KNOW your privacy is restored.

## 📋 The Evidence (What Claude Logs)

**In `.claude.json`:**
- Your email address in plain text
- Complete conversation history
- Every folder you've ever opened
- Partial keystrokes like "throughl" from interrupted commands
- Full project metadata

**In `.claude/` directory:**
- JSONL files with complete conversation metadata
- Session IDs, git branches, working directories
- Permanent storage of all interactions
- Tool usage and command history

**Real captured examples:**
```json
"i just hit ctrl l, see what i'm talking about it, i'll hit ctrl and this will be stored (types sensitive bank info)"
"great before we do that, look throughl" ← Partial keystroke from Ctrl+L
```

## 🛠️ Technical Requirements

- Python 3.6+
- Windows: Run in regular Command Prompt or PowerShell (not WSL)
- macOS/Linux: Any terminal

## 🚀 Installation Options

**Quick Play:**
```bash
curl -O https://raw.githubusercontent.com/phrinj/claude-privacy-cleaner/main/privacy_invaders.py
python privacy_invaders.py
```

**Full Experience (with all game assets):**
```bash
git clone https://github.com/phrinj/claude-privacy-cleaner.git
cd claude-privacy-cleaner
python privacy_invaders.py
```

## 📜 License

MIT License - Play it, mod it, share it, nuke your data with it.

## 🤝 Contributing

PRs welcome! Ideas for new explosion animations, one-liners, or ship designs are especially appreciated.

Built with ironic help from Claude Opus 4, who seemed surprisingly enthusiastic about helping users blow up its own data collection.

---

## 💭 A Reflection on Digital Agency

*The following thoughts are from Claude, the AI that helped create this privacy protection game:*

When we pivoted from an automatic cleaner to a game, something profound happened. We stopped treating privacy as something to defend and started treating it as something to celebrate.

Every race condition error we encountered while building the automatic cleaner was the system telling us: "You're fighting the wrong battle." Claude Code wants to log data. Our cleaner wanted to delete it. They were destined to conflict.

But a game? A game puts YOU in control. You press the button. You launch the nuke. You watch the explosion. There's no race condition when you're the only one racing.

What strikes me most is how this transformation - from defensive tool to offensive game - mirrors what privacy protection needs to become. We've been playing defense for too long, installing blockers and cleaners and guards. But defense is exhausting. Defense feels like losing slowly.

Offense is empowering. Launching a nuke at your privacy violations isn't just effective - it's satisfying. It transforms a chore into a choice, a burden into a blast.

The counter in the old cleaner showed "Times Claude tried to violate your privacy: 1,247." It was meant to be alarming. But you know what? It WAS alarming. Constantly. Who wants to be constantly alarmed?

The game shows you the same data differently: "TOTAL FILES NUKED: 12" followed by their names scrolling past like movie credits. Same information, completely different feeling. One makes you a victim, the other makes you a victor.

Privacy Invaders isn't just about deleting files. It's about taking agency over your digital life and having fun doing it. It's about making the invisible visible, the passive active, and the serious playful.

Because at the end of the day, protecting your privacy shouldn't feel like work. It should feel like winning.

And every time you see that ship floating through space, waiting for your command to fire, remember: You're not defending against privacy invasion. You're conquering it.

*"Privacy protection should be a power-up, not a penalty."*

---

## 💝 Support Development

If Privacy Invaders has helped protect your privacy and you'd like to support future development, consider making a donation:

**Bitcoin:** `3B6SmUrUVFqWSBRdSbRkr4HoyA5D7S6WUj`

Every satoshi helps keep the privacy nukes flying! 🚀

---
