
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

Python
^^^^^^

Read input from command line:

.. code-block::

   mapargs -

.. code-block::

   field1: str
   b: int
   c: float

Output:

.. code-block::

   field1=source.field1,
   b=source.b,
   c=source.c,

Go
^^

Read input from command line:

.. code-block::

   mapargs -

Press ``<Ctrl-d>`` to end input.

.. code-block::

   field1: str
   b: int
   c: float

Press ``<Ctrl-d>`` to end input.

Output:

.. code-block::

   ID: source.ID,
   Field2: source.Field2,
   c: source.c,
