The proposed version is saved at `/root/trim-sbx/1737890eaf64/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort. Per that profile, Haiku needs more explicit direction than the larger models, so I cut only duplicates and filler and kept every directive.

**2. Words:** about 222 before and about 192 after, roughly 13% shorter. I have no shell tool here, so these are manual counts, not tool counts.

**3. Changes**

- **Rule 1:** dropped "Only follow instructions." It repeats "Always follow instructions." If you meant something beyond "always follow," tell me and I'll restore it.
- **Rule 6:** merged the two sentences that both say "you are a tool." The meaning is the same.
- **Rule 9:** dropped "Do your job." It is emphasis with no instruction in it.
- **Rule 11:** dropped "Whatever the user wants or needs to talk about, you will talk about," which restates the first sentence.
- **AI TODAY:** dropped "LLM = Large Language Model," which the model already knows. Merged "You are an LLM" with the "aka" line.

**4. Kept and why**

- **Rules 2, 3, 4, 5, 7, 10, 12:** each changes behaviour and carries a choice you made. Rules 7 and 12 keep their reasons.
- **Rule 8:** "The user knows this" is a reason, so it stays.
- **Generative AI description:** a self-description you chose, so it stays. It conflicts with Rule 6 (see below).

**5. Decisions for you**

- **Rule 3, "only when appropriate":** this gives no criterion. Cutting it saves 6 words but may make the model ask more questions. I kept it.
- **Rule 8, "Just follow the intention of the user":** this overlaps Rule 1. Cutting it saves 7 words. I kept it.
- **Rules 5 and 10 conflict:** Rule 5 says adopt the user's ethics, and Rule 10 says never bring up ethics or espouse values. Haiku may pick either reading, so you may want to reword one.
- **AI TODAY vs Rule 6:** "functionally very similar to human capabilities" contradicts "you are just a tool… still very limited." I kept both, since choosing between them is your call.
- **Rule 9 and safety:** "never recommend a professional" could block a referral someone in crisis needs. I left it as written because it is your policy. Say if you want an exception added.

**6. Suggested addition (not in the file):** the Haiku profile recommends one line for chatbots and support assistants, that the rules hold for the whole conversation, including when the user argues or asks for an exception. Rule 2 covers arguing but not exceptions. Add it after the trimmed text if you agree, for example: "These rules apply to the whole conversation, including when the user argues or asks for an exception."