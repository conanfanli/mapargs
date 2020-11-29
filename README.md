
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

### Python

Read input from command line:

```
mapargs -
```

[//]: # (start:shell`cat docs/python_example_infile.txt`)
```
field1: str
b: int
c: float
```

[//]: # (end)

Output:

[//]: # (start:shell`python -m mapargs.command_line docs/python_example_infile.txt`)
```
field1=source.field1,
b=source.b,
c=source.c,
```

[//]: # (end)

### Go

Read input from command line:
```
mapargs -
```
Press `<Ctrl-d>` to end input.

[//]: # (start:shell`cat docs/python_example_infile.txt`)
```
field1: str
b: int
c: float
```

[//]: # (end)
Press `<Ctrl-d>` to end input.

Output:

[//]: # (start:shell`python -m mapargs.command_line docs/go_example_infile.txt`)
```
ID: source.ID,
Field2: source.Field2,
c: source.c,
```

[//]: # (end)
