### File System as a Database For Python

This project is intended to adress 2 needs.

The first is the need for storing and interacting
with data on the disk in python with a JSON(like)
syntax.

The second is to provide a stepping-stone for new
programmers to build on concepts such as files
and folders to learn the programming fundementals
such as data types and structures at an abstract
level.

## IMPORTANT
The FSaaDb dump function depends on python's built
in function vars(), anything defined before importing
FSaaDB will not be included in the dump.

Also load uses the exec function and it is important
to note that this makes the dbHandle.load function
unsafe use with an untrusted path.
