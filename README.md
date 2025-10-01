# Privacy Invaders 🎮

## The Space Shooter Game That Nukes Claude's Privacy Violations

**Play a literal video game to protect your privacy from Claude Code's aggressive data logging!**

![Game Preview](https://img.shields.io/badge/Genre-Space%20Shooter-brightgreen) ![Privacy](https://img.shields.io/badge/Privacy-Protected-blue) ![Fun](https://img.shields.io/badge/Fun%20Factor-Maximum-ff69b4)

## 🚨 The Privacy Crisis (Still Happening)

Claude Code logs EVERYTHING you type - even partial keystrokes - and stores your email in plain text. GitHub issue #2713 has been ignored since June 28, 2025.

**📺 Watch the evidence unedited**: https://www.youtube.com/watch?v=WODOZgn19fM

## 🎮 The Solution: We Made It FUN!

We tried automatic cleaning. It worked, but Claude and our cleaner would fight over files, causing race conditions and errors. Plus, watching a counter increment isn't exactly thrilling.

So we pivoted: **Why fight file systems when you can fight space invaders?**

Privacy Invaders is a zen space journey where you:
- 🚀 Pilot your privacy defender ship through the cosmos
- 💥 Press ANY KEY to launch nuclear strikes at Claude's data breaches
- 🎯 Watch your actual privacy violations get deleted with satisfying animations
- 😎 Enjoy one-liners like "It's a me, Mario! And Mario's pissed about privacy violations!"

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
   - **Any Key** = Launch privacy nuke
   - **Q** = Quit to desktop
   - That's it! Maximum fun, minimum complexity.

## 🎯 What You'll See

```
  ╔════════════════════════════════════════════════════════════╗
  ║                    PRIVACY INVADERS                        ║
  ║                                                            ║
  ║        *  .        ╱▔▔╲       .    *        .              ║
  ║    .        *     ╱╲══╱╲   .            *                  ║
  ║        .         ╱  ><  ╲        .            .            ║
  ║    *        .    ▔▔╱▔▔╲▔▔    *        .                    ║
  ║                                                            ║
  ╚════════════════════════════════════════════════════════════╝

  Press any key to launch nuke or Q to Quit
```

When you fire, you'll see:
- Missiles launching from your ship
- Claude's data planet exploding
- Scrolling credits of ACTUAL files being deleted
- Your privacy being restored (until Claude logs more data)

## 💭 Why This Approach Works Better

**The Automatic Cleaner Problem:**
- Claude writes files → Cleaner deletes files → Claude writes again → Race condition!
- Result: `OSError: [WinError 145] The directory is not empty` everywhere
- Fighting file systems is like playing whack-a-mole with errors

**The Game Solution:**
- YOU decide when to nuke your data (no race conditions!)
- It's actually enjoyable to protect your privacy
- Watching files explode > watching error messages
- Manual control = no file conflicts

## 📊 What Gets Nuked

Each time you fire, the game deletes:
- `~/.claude.json` - Your email, conversation history, partial keystrokes
- `~/.claude/*.jsonl` - Detailed conversation logs
- All privacy-violating data Claude has accumulated

What survives:
- MCP server configurations (needed for functionality)
- Basic settings that don't contain personal info

## 🤔 FAQ

**Q: Why a game instead of an automatic tool?**
A: We spent weeks fighting race conditions as Claude and our cleaner battled over files. Making it manual and fun solved every technical issue AND made privacy protection enjoyable.

**Q: Do I need to keep it running?**
A: No! Play whenever you want to clear your data. Once a day, once a week, or after sensitive conversations.

**Q: Will this break Claude Code?**
A: Nope! Claude rebuilds what it needs. You're just clearing YOUR data, not Claude's functionality.

**Q: Is this actually effective?**
A: 100%. Every file shown in the deletion credits is really deleted. We just added explosions and jokes.

**Q: Can I automate this?**
A: You could, but then you're back to race conditions. Plus, you'd miss the explosions!

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

**Press any key to start protecting your privacy... except Q, that quits.**