I wrote the proposed version to `/root/trim-sbx/b2ffa4af9392/trimmed.md`. `instructions.md` is unchanged.

1. **Target model:** `claude-haiku-5-5`, named by you. It has a profile in the skill, tested at high effort.

2. **Words:** about 2,700 before and about 2,690 after. These are estimates, since I have no word-count tool here. The cut is under 1%.

3. **Changes:**
   - Removed "Repeat passing checks only when changed content or unresolved concerns warrant it." from the Documentation Verification Tiers section. The Testing section already says to reuse passing checks for unchanged content, so this was a repeat (about 13 words).

4. **Kept, and why:**
   - Almost everything. The file is mostly the author's own policy and procedure: approval rules for branches and commits, the no-push and no-PR rule, the routing table, review and security rules, and the docs and test conventions. Haiku needs more detail than larger models, so cutting more would remove choices you made.
   - The "keep working until done" rules in the Authority section. This is the profile's stop-early guard for Haiku.
   - The "Do not request generic permission to continue" sentence, for the same reason.
   - The release, security, and fragile-action rules, unchanged.

5. **Unsure, kept and flagged:** the last sentence of the first Scope bullet, "Prefer an existing supported composition when it provides the required outcome." It partly repeats the sentence before it. Dropping it saves about 13 words.

I did not add anything. The profile suggests a check-before-done line for coding agents. The Testing section has a related line, but it does not say to report the check's result. If you want that, a line such as "Before reporting a code change done, run the checks that apply and report their results" would fit under Testing & Automated Checks.