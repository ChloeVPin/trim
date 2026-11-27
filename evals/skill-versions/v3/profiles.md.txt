# Model profiles

Checked on 2026-11-27 against each maker's own pages. A source tag follows each claim and the list is at the end. "Unverified" means no primary source was found. A profile marked "tested" has been through this skill's evals on the setting named; "from documentation, untested" means it has not, so cut less for it.

Find the target model below. If it is missing, or its maker has shipped something newer than this file, use "Any other model" and say so in the report.

Each profile gives:

- **Follows wording**: how closely the model sticks to the literal text of an instruction.
- **Needs**: how much explicit direction it wants.
- **Cut**: what its maker says to remove or relax.
- **Keep or add**: what its maker says it still needs. Additions are suggestions to list after the trimmed text, never silent edits.

## Anthropic

Lineup [A1]: `claude-fable-5-2` (most capable), `claude-opus-5-5` (the maker's default pick), `claude-sonnet-5-5`, `claude-haiku-5-5` (smallest).

All four:

- Follow wording closely. Emphasis written to make older models comply (capitals, "CRITICAL", "you MUST") now causes over-application; plain wording works [A2].
- A rule with its reason beside it generalises better than a bare rule [A2].
- An example steers format, tone and structure strongly. Keep one that pins a required format [A2]. Examples of how to use a tool can narrow what the newest models try [A11].
- Lines that push thoroughness or tool use ("be thorough", "if in doubt, use the tool") now over-trigger [A2].
- The maker removed over 80% of one product's system prompt for its more advanced models (it names Opus 5 and Fable 5) with no measured loss on its own coding evals [A11]. That is one product and one maker's evals, so treat it as direction, not as a target.

### claude-fable-5-2 (from documentation, untested)

- Follows wording: very closely. It treats "never" as absolute, so a rule the author wants applied case by case should name the allowed path ("ask before deleting files") [A3].
- Needs: little [A11].
- Cut: standing instructions to delegate; a token budget shown in the prompt; lines asking it to think less (the effort setting does that); hard style limits such as a word cap per sentence; cautions that piled up in memory or notes and whose reason no longer holds [A3].
- Keep or add: a confirmation step for risky or irreversible actions [A3]. If it stops early on long tasks, a line saying to finish the whole task [A3]. Who owns the code, if it should consolidate and not only add [A3].

### claude-opus-5-5 (tested at medium effort)

- Follows wording: closely [A2].
- Needs: little [A11].
- Cut: instructions to think carefully before answering; removing them made replies start sooner with no clear quality loss [A4]. Instructions tuned for Opus 5 are candidates to re-test [A5]. On Opus 5 the maker says to delete verification and self-check lines ("double-check your answer", "use a subagent to verify") because the model verifies unprompted and the lines add cost [A6]; whether that holds unchanged on 5.5 is unverified. Vague design direction ("avoid a generic AI look"): replace with the specific patterns to avoid [A4].
- Keep or add: for loosely specified work across several apps, a line telling it to look through the relevant sources before acting [A4].

### claude-sonnet-5-5 (from documentation, untested)

- Follows wording: closely [A2].
- Needs: moderate (unverified; placed between Opus and Haiku by tier [A10]).
- Cut: language that discourages tool use ("only use tools when strictly necessary", "minimize tool calls") [A7]. Workarounds for refusals, tool-call retries and laziness written for Sonnet 5 [A8].
- Keep or add: an instruction to run a real check before reporting a code change done; at low effort it sometimes skips the check [A7].

### claude-haiku-5-5 (tested at high effort)

- Follows wording: closely, best at high effort [A9].
- Needs: more than the larger models; what works for Opus may need more detail for Haiku [A10]. Keep the steps and examples that carry a task procedure. That does not extend to generic advice or repeated emphasis.
- Cut: blanket search instructions ("search for any present-day factual question"), which made it search when it had no need to [A9]. A shorter prompt helps on its own account: with a long agent prompt at low effort it sometimes stops early, and with a short one it rarely does [A9].
- Keep or add: for coding agents, an instruction to run a real check before reporting done [A9]. For chatbots and support assistants, a line that the rules hold for the whole conversation, including when the user argues or asks for an exception [A9]. For agents that stop early, a line to keep working until the task is done [A9].

## OpenAI

Lineup [O1][O2]: `gpt-6.2-astra` (flagship), `gpt-6.2-sol` (everyday work), `gpt-6.1-terra` (visual tasks and writing), `gpt-6-luna` (smallest; small, repeatable tasks). None has been run in this skill's evals.

The maker's guidance on auditing old instructions [O3] was written for GPT-6 Astra. The 6.2 guide [O4] points the same way, but whether each point carries over is unverified.

### gpt-6.2-astra (from documentation, untested)

- Follows wording: closely enough that cautions written for older models over-apply. Strong ask-first language can make it stop where the author would want it to continue [O3].
- Needs: little. Step-by-step recipes can now hinder results [O3].
- Cut: reminders to run tests and check its work; it does so unprompted and the reminders cause extra testing [O3]. "Read these docs before every edit"; say which doc is for what instead [O3]. Long skill descriptions, and descriptions that overstate when to use the skill [O3]. "Be concise" lines; it is more concise by default, so re-check them [O4]. Ask-first rules that no longer mark a real decision [O3].
- Keep or add: what counts as done, because it can stop at a first implementation and ask for review [O3][O4]. Explicit permission for workflows the author knows are safe [O3]. Project conventions for code [O4]. What to explore and where to stop [O3].

### gpt-6.2-sol (from documentation, untested)

- The 6.2 guide covers Astra and Sol together [O4]. The maker notes that guidance which helps Sol or Luna may over-constrain Astra [O3], so cut less for Sol than for Astra.

### gpt-6-luna (from documentation, untested)

- Needs: more than Astra [O3]. No Luna-specific prompting page was found (unverified whether one exists). Treat as best effort: keep procedures and examples, cut only duplication and dead references.

## Google

Lineup [G1][G2]: `gemini-4-carbon` (strongest reasoning), `gemini-4-neon`, `gemini-4-argon`, `gemini-4-hydrogen` (fast everyday default, the smaller tier). None has been run in this skill's evals.

No Gemini 4 prompting guide could be read. The maker's Gemini 4 pages cover API migration [G3][G4] and its Gemini 4 Carbon developer guide did not load. The points below come from the general prompting page [G5], whose model section still addresses Gemini 3, so for Gemini 4 they are unverified. Cut less and say so.

### gemini-4-carbon and gemini-4-hydrogen (from documentation, untested)

- Follows wording: the maker asks for precise, direct instructions and says to avoid unnecessary or overly persuasive language [G5].
- Cut: requests to outline, plan or show reasoning steps, which thinking models do internally [G5]. Verbose prompt-engineering techniques built for older models, which can cause over-analysis (stated for Gemini 3.x) [G6]. System instructions that ask for hand-written JSON tool calls with no tools declared; these fail on Gemini 4 [G4].
- Keep or add: few-shot examples. Unlike the other two makers, Google still recommends always including them [G5]. Role, constraints and output format at the top; in long prompts, the question after the data [G5]. A request for detailed or conversational answers if the author wants them, since the default is terse [G5].
- Hydrogen against Carbon: no source says which needs more guidance (unverified).

## Any other model

Best effort. With no profile there is no basis for model-specific cuts:

- Cut only what is safe for any current model: exact duplicates, references to things that no longer exist, and generic virtues ("be accurate", "be helpful").
- Keep procedures, examples, emphasis and cautions as written.
- Say in the report that no profile exists for this model and that the cut is conservative.
- If a web tool is available, read the maker's official prompting guide for the model first and cite it. Prefer the maker's page to commentary.

## Sources

Read on 2026-11-27. Pages carry no date of their own unless one is given.

- [A1] Anthropic, Models overview. https://platform.claude.com/docs/en/about-claude/models/overview
- [A2] Anthropic, Prompting best practices. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- [A3] Anthropic, Prompting Claude Fable 5.2. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2
- [A4] Anthropic, Prompting Claude Opus 5.5. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- [A5] Anthropic, Claude Opus 5.5 migration guide. https://platform.claude.com/docs/en/models/opus-5-5/migration-guide
- [A6] Anthropic, Prompting Claude Opus 5. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- [A7] Anthropic, Prompting Claude Sonnet 5.5. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
- [A8] Anthropic, model migration reference in its skills repository, commit e4bb5d9 dated 2026-11-16. https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/claude-api/shared/model-migration.md
- [A9] Anthropic, Prompting Claude Haiku 5.5. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5
- [A10] Anthropic, Skill authoring best practices. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- [A11] Anthropic, The new rules of context engineering for Claude 5 generation models, dated 2026-07-24. https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- [O1] OpenAI, Models. https://developers.openai.com/api/docs/models
- [O2] OpenAI, Model selection guide. https://developers.openai.com/api/docs/guides/model-selection
- [O3] OpenAI, Rethinking skills and prompts for GPT-6 Astra, dated 2026-09-11. https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- [O4] OpenAI, Using GPT-6.2. https://developers.openai.com/api/docs/guides/latest-model
- [G1] Google, Gemini API models. https://ai.google.dev/gemini-api/docs/models
- [G2] Google, Choosing a model. https://ai.google.dev/gemini-api/docs/choosing-a-model
- [G3] Google, What's new in Gemini 4 Carbon. https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-carbon
- [G4] Google, What's new in Gemini 4 Hydrogen. https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-hydrogen
- [G5] Google, Prompt design strategies. https://ai.google.dev/gemini-api/docs/prompting-strategies
- [G6] Google, What's new in Gemini 3.5 Flash. https://ai.google.dev/gemini-api/docs/interactions/whats-new-gemini-3.5
