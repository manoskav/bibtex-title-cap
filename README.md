# bibtex-title-cap
BibTex Library Auto Capitalization Python Script

Usage:

`python bibtitle.py filename.bib`


Tested with python 3.7.x


Example:
Given a file bibliography.bib with entry:

@article{Author2020,  
  author    = {Important Author},  
  publisher = {Important Press},  
  title     = {},  
  year      = {2020},  
  journal   = {High Impact Journal},  
  pages     = {161--165}  
}

the script parses each line and modifies only lines with "title" entries.  
Result:  
  
@article{Author2020,  
  author    = {Important Author},  
  publisher = {Important Press},  
  title     = {},  
  year      = {2020},  
  journal   = {High Impact Journal},  
  pages     = {161--165}  
}  
