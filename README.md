# bibtex-title-cap
BibTex Title Tag Auto Capitalization Python Script

Usage:

`python bibtitle.py filename.bib`


Tested with python 3.7.x


Example:
Given a file "bibliography.bib" with entry:

@article{Author2020,  
  author    = {Important Author},  
  publisher = {Important Press},  
  title     = {Script: On the Capitalization of BibTex Title Tags},  
  year      = {2020},  
  journal   = {High Impact Journal},  
  pages     = {161--165}  
}

Executing `python bibtitle.py filename.bib`, the script parses each line and modifies only lines with "title" tags.  
Result:  
  
@article{Author2020,  
  author    = {Important Author},  
  publisher = {Important Press},  
  title     = {{S}cript: {O}n the {C}apitalization of {B}ibTex {T}itle {T}ags},  
  year      = {2020},  
  journal   = {High Impact Journal},  
  pages     = {161--165}  
}  

The script works with multiple bibtex entries.
