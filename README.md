# mypy plugin test

Just some code to undestand how to write [mypy](https://mypy.readthedocs.io/en/stable/index.html) plugins.

## How it works
The plugin checks two things:
- `pow` operations between integers
- string concat with the `+`

`mypy .` to run the checks and you should see something like this:
```
main.py:5: error: No power between ints in my code!  [misc]
main.py:11: error: Use another method for concatenate strings  [misc]
Found 2 errors in 1 file (checked 4 source files)
```
