
Usage
=====

.. code-block::

   usage: mapargs [-h] infile

   positional arguments:
     infile

   optional arguments:
     -h, --help  show this help message and exit

Examples
--------

Read input from command line:

.. code-block::

   mapargs -
   field1: str
   b: int
   c: float

   <Ctrl-D>

Output:

.. code-block::

   field1=source.field1,
   b=source.b,
   c=source.c,
