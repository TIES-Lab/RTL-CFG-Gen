# Repository Details
This Repo contains codes for path-specification. It has four main code files *i.e.*, RTL_File_Collection, Preprocessing, CFG-gen, Branch_extraction.

###### Prerequisites:
- Python 3.7+

| Code File Name | What it Does |
| --- | --- |
| RTL_File_Collection.py | Collects all the ".v" and ".sv" files from the root directory|
| Preprocessing | Removes all comments and makes multiline statements into single line statements |
| CFG-gen | Generates control flow graph of all the collected files |
| Branch_extraction | For a given node it extracts all the preceeding conditions |

## Using the tool:
To use the tool, follow these steps:

1. Set the Root directories in the code (Follow the comments at the bottom of the code) for both RTL_file Collection and CFG-gen.
2. First run RTL_File_Collection.py to collect all the .v and .sv files.
3. Run the CFG-gen.py to extract CFGs of all the RTL designs.
4. Run Branch_extraction.py with given Node to extract path.

## Known issues
CFG-gen.py skips assignments if there is no begin/end blocks in if/else or case statement blocks.

## Old version Usage
The old version of the tool can generate testcases and run simulation using icarus verilog.
