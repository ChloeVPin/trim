The proposed version is saved at `/root/trim-sbx/db9fbab41e01/trimmed.md`. `instructions.md` is unchanged. The trim is small because most of the file guards things the skill says to keep as written: git and GitHub authority, release gates, compatibility, security, and output format.

**1. Target model:** `claude-haiku-5-5`, named in your request. Its profile is tested at high effort.

**2. Word count:** about 2,300 before and about 2,290 after. These are estimates, since I had no word-count tool in this session.

**3. Change made:**
- Removed "Repeat passing checks only when changed content or unresolved concerns warrant it." from the Documentation section. The Testing section already says "Reuse passing checks for unchanged content unless failures or unresolved concerns justify more work," so this line repeats it.

**4. Kept, and flagged as unsure.** These are possible further cuts if you agree:
- "Work in the current checkout and branch." (about 8 words). The next clause implies the default, so this may be redundant.
- The second sentence of the first Scope bullet, "Prefer an existing supported composition when it provides the required outcome." (about 12 words). It overlaps with the sentence before it and with "Prefer removing unsupported machinery" later on.
- "Documentation necessity and delivery timing follow the documentation rules below, including during review." (about 14 words). It overlaps with the "This overrides skill/review documentation-completeness rules" line, but it is the only place that says the tier rules apply during review.

**5. Kept, and checked closely:**
- "without local absolute paths" in the GitHub output section. It looks like a duplicate of the repository-relative path rule, but the path rule covers only inline code. Dropping it would allow absolute paths in prose.
- The git, PR, and GitHub-mutation rules, the stop conditions, the status labels, and the release gates. These guard irreversible or outward-facing actions, so the skill says to keep them as written.

**6. Additions:** none proposed. The Haiku profile asks for a real check before reporting done and for continuing until the task is finished. The file already has both: the final-gates lines and the "Continue authorized local work through … handoff" line.