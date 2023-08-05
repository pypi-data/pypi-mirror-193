## ReplBuilder

`pip install replbuilder`

Quickly build a repl cli prompt in python.

argparse is used for quick and easy parsing interface, some options are overriden for using within a repl prompt.

REPL is a helpful way to interact with a program as it is running, without needing IPC calls.

## Example

see [example calculator repl](example_calculator_repl.py) for example implementation. As easy as:

```
runner = ReplRunner("calculator")
runner.add_commands([add_cmd, sub_cmd, mult_cmd, div_cmd, pow_cmd, cow_cmd])
runner.run()
```

run it `python example_calculator_repl.py`

part of the repl is colorized for better visibility.

![example repl run](demo.jpg)
