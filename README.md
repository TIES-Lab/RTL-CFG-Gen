# Repository Details
This Repo contains codes for path-specification. It has four main code files *i.e.*, RTL_File_Collection, Preprocessing, CFG-gen, Branch_extraction.

| Code File Name | What it Does |
| --- | --- |
| RTL_File_Collection.py | Collects all the ".v" and ".sv" files from the root directory|
| Preprocessing | Removes all comments and makes multiline statements into single line statements |
| CFG-gen | Generates control flow graph of all the collected files |
| Branch_extraction | For a given node it extracts all the preceeding conditions |

## Known issues
CFG-gen.py skips assignments if there is no begin/end blocks in if/else or case statement blocks.


