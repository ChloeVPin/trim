# Running agents

Use `Runner.run()` to run an agent until it produces a final output.

## The agent loop

The runner calls the model, executes any tool calls the model asks for, and repeats.
The loop stops when the model returns a final output or when `max_turns` is reached.
By default `max_turns` is 10; pass a `RunConfig` to change it.

## Tool outputs

Tool return values are converted to strings and sent back to the model on the next turn.
Make sure your tools recieve only the arguments they declare; extra arguments are an error.
Large tool outputs are sent to the model in full, wich can be slow and expensive.
