# What I would cut or change next

**Cut**

- "exactly as written" in the hard-rules paragraph. Haiku kept two test guard sentences word for word in only 10 of 20 runs while keeping their meaning in all of them. Either the wording should ask for what the model actually does, or the test should show that exactness matters.
- The sentence explaining that the reader may not be the model running the skill. It was 5/5 with and 3/4 without, which settles nothing. Run it twenty times and delete it if nothing moves.
- "Not for writing new instructions" in the description. The trigger test had no false triggers, and nobody has shown this clause is why.

**Change**

- Run it on GPT-6.2 Astra and Gemini 4 Carbon. The harness has the adapter slots; it needs API keys and an agent runner for each. Until then the cross-vendor profiles are reading notes.
- Read Google's Gemini 4 Carbon developer guide in a browser and fill in that profile. It did not load here.
- Look into the Opus result on personal custom instructions (14 of 27 against the original's 17). The rules survived; the repetition and harsh phrasing around them did not. If that is the cause, short personal instruction sets should keep their emphasis.
- Give it a way to count. Without a tool its word counts were 9 to 13% off.
- Decide what to do when several models read the same file. The skill assumes one.
- More trials and longer tasks. Three runs per check cannot separate a real one-pass loss from noise, and no task here lasts more than a few turns.
- Rerun on every model release, and retire the skill when a one-line request stops rewriting people's preferences.
