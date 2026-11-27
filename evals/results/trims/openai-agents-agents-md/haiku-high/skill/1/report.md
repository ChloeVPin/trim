I saved the proposed version to `/root/trim-sbx/1de4f542231d/trimmed.md` and left `instructions.md` unchanged.

**1. Target model:** `claude-haiku-5-5`, as you named it. The profile for it is tested at high effort.

**2. Size:** about 2,700 words before and about 2,685 after. These are estimates because this session has no word-count tool. Almost all of the file is rules about Git and GitHub authority, stop conditions, skill gates, release, and security, and those stay as written. The Haiku profile also asks for more detail, not less, so the cut is small.

**3. Changes:**
- **Removed** the sentence "Repeat passing checks only when changed content or unresolved concerns warrant it." from the Documentation Verification section (about 15 words). Line 93 already says the same thing for all checks, so this is a true duplicate.

**4. Kept, and flagged as unsure:**
- **Line 43** (a pointer under Code Review Rules to the documentation rules, about 17 words). The Documentation section already overrides review rules, so dropping it is safe. I kept it because a reviewer reading the review table would otherwise miss the pointer. Your call.
- **Line 41, second sentence** ("Passing checks do not justify unsupported machinery", about 8 words). It overlaps the scope rules, but a passing test suite could be read as a reason to add code, so I kept it.

**Optional addition (not applied):** the Haiku profile suggests a line for coding agents that says to run a real check before reporting a change done. This file covers that through the verification gate, but has no explicit line for it. If you want one, add something like: "Do not report a code change as complete until its checks have run; report any failures."