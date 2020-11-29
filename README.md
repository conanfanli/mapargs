
# Usage

[//]: # (start:shell`python -m mapargs.command_line --help`)
```
usage: mapargs [-h] infile

positional arguments:
  infile

optional arguments:
  -h, --help  show this help message and exit

```
[//]: # (end)

## Examples

Read input from command line:
```
mapargs -
field1: str
b: int
c: float

Ctrl-D
```

[//]: # (start:shell`python -m mapargs.command_line docs/example_infile.txt`)
[//]: # (end)
