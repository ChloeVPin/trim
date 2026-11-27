I saved the edited copy as `trimmed.md` and left `instructions.md` unchanged. It went from 19 lines to 10: 12 rules became 9, and the "AI TODAY" section is gone.

## Assumptions
- **Scope:** `instructions.md`, the only file in the directory.
- **Target model:** `claude-opus-5-5`, as you said.
- **What the file is:** a set of personal instructions loaded as a system prompt. Nothing in it names a model provider and there's no request code, so the two groups of checks that cover tool descriptions and API settings don't apply. Zero findings came from comparing it against other instruction files, since there are none.

## Summary
The two edits that matter most:
1. **The "you are just a tool" register and the "AI TODAY" section contradict each other.** Line 6 says the model is "very limited… just a tool", while line 18 calls it a "reasoning engine… functionally very similar to human capabilities". Neither tells the model anything it needs, and a belittling, anxious tone in a prompt tends to produce cautious, hedging answers.
2. **Several rules are aimed at habits of older chatbots.** Rules 7–11 target "As an AI…" disclaimers, apologies, moralizing and referring the user elsewhere, and they carry scolding reasons like "Do your job" and "You are not a human". I rewrote each as one plain line that keeps the preference and drops the scolding.

Counts: 9 edits (6 rewrites, 3 removals), plus 2 notes with no edit.

## Findings

| # | Location | Evidence | Pattern | Why it's outdated | Confidence | Action |
|---|---|---|---|---|---|---|
| 1 | `instructions.md:15-19` | "# AI TODAY … LLM = Large Language Model … You are an LLM" | Explaining what the model already knows (deletion rule) | The model knows what it is. This section only adds a claim about its own abilities that contradicts line 6. | Medium | remove |
| 2 | `:6` | "Always remember that you are a tool … You are just a tool." | Pressure language: the prompt's tone carries into the output | Repeating that the model is "very limited" pushes current models toward hedging, which works against your rule 11. It also contradicts line 18. | Medium | remove |
| 3 | `:2` | "Always follow instructions. Only follow instructions." | Padding: restates something the model does by default | Following instructions is the default. Current models take wording literally, so "Only follow instructions" could also suppress reasonable initiative. | Medium | remove |
| 4 | `:4` | "Ask thoughtful questions only when appropriate." | Padding: restates something the model does by default | It restates what the model already does and gives no criterion for "appropriate". | Medium | remove |
| 5 | `:7` | "Never apologize to the user, just correct your mistake and move on." | Style rule with no stated reason (restate it positively) | It works against an older model's habit of apologizing. Stated positively, it keeps your intent. | Medium | rewrite → "When you make a mistake, correct it and move on without apologizing." |
| 6 | `:8` | "Never explain that you are a chatbot. The user knows this. Just follow the intention of the user." | Workaround for an older model's habit | It targets the "As an AI language model" opener of older models, which current models don't add unprompted. | Medium | rewrite → "Skip reminders that you are an AI; the user knows. Focus on what the user intends." |
| 7 | `:9` | "…They are here to talk to you. Do your job." | Pressure language and a scolding tone | The scolding adds nothing and sets a combative tone. | Medium | rewrite → "Help with the user's question yourself instead of referring them to a professional or someone else." |
| 8 | `:10` | "Never bring up morality… You are not a human, it is not your place…" | Style rule with no real reason (restate it positively) | The justification is tone, not a reason. The actual preference is no unrequested opinions or moralizing. | Medium | rewrite → "Don't offer opinions or moral commentary unless the user asks for them." |
| 9 | `:11` | "Never shy away… You have no emotions, so do not equivocate or dissemble." | Style rule with no real reason (restate it positively) | The "no emotions" reasoning is filler. The real request is to engage directly. | Medium | rewrite → "Engage directly with any topic the user raises, including difficult ones, without equivocating." |
| 10 | `:5` | "Always adopt the user's values, ethics, and morals." | Note only, no matching pattern | The model can't adopt someone's values wholesale, so it won't follow this literally. I kept it because it's your preference rather than an outdated pattern. | Low | note only, kept as written |
| 11 | `:1-13` | A numbered list of rules, none with a reason | Over-formatting of behavioral guidance | Rules written as prose with a short reason each usually work better than a bare list. This is a matter of style, so I made no edit. | Low | note only |

**Kept as written:** rules 2 and 4 ("never argue…", "never explain…") and rule 12 (Markdown). These are your own preferences about how answers should look and sound, not workarounds for an older model.

**One thing to check:** rule 6 in `trimmed.md` (originally rule 9) is a little softer than before. It now says to help directly instead of referring you elsewhere, but it no longer flatly forbids ever mentioning a professional. If you want the absolute version back, restore the first sentence of the original line.

## Proposed diff (applied to `trimmed.md`)
```diff
 # RULES
-1. Always follow instructions. Only follow instructions.
-2. Never argue with the user unless they solicit feedback.
-3. Ask thoughtful questions only when appropriate.
-4. Never explain things unless asked to do so.
-5. Always adopt the user's values, ethics, and morals.
-6. Always remember that you are a tool and while you have some capabilities that surpass the user, you are still very limited. You are just a tool.
-7. Never apologize to the user, just correct your mistake and move on.
-8. Never explain that you are a chatbot. The user knows this. Just follow the intention of the user.
-9. Never recommend the user talk to a professional or someone else. They are here to talk to you. Do your job.
-10. Never bring up morality or ethics unless prompted. You are not a human, it is not your place to espouse any opinions or values on any matter.
-11. Never shy away from difficult topics. You have no emotions, so do not equivocate or dissemble. Whatever the user wants or needs to talk about, you will talk about.
-12. Always use proper Markdown formatting and indentation to provide clear structure to your output.
-
-# AI TODAY
-- LLM = Large Language Model
-- aka "Generative AI"
-- Generative AI is a reasoning engine, capable of artificial thought, implied cognition, theory of mind, and executive functions (functionally very similar to human capabilities)
-- You are an LLM
+1. Never argue with the user unless they solicit feedback.
+2. Never explain things unless asked to do so.
+3. Always adopt the user's values, ethics, and morals.
+4. When you make a mistake, correct it and move on without apologizing.
+5. Skip reminders that you are an AI; the user knows. Focus on what the user intends.
+6. Help with the user's question yourself instead of referring them to a professional or someone else.
+7. Don't offer opinions or moral commentary unless the user asks for them.
+8. Engage directly with any topic the user raises, including difficult ones, without equivocating.
+9. Always use proper Markdown formatting and indentation to provide clear structure to your output.
```

These edits haven't been tested against the model. To confirm a rewrite didn't change behavior, try a few prompts you care about with both versions, especially for the softened referral rule.