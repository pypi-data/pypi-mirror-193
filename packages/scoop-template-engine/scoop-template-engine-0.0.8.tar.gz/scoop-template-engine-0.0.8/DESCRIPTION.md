The purpose of the scoop template engine (`ste`) is to facilitate the preparation of manuscripts in [LaTeX](https://www.latex-project.org/) for publication in scientific journals.
It allows the separation of layout from content.
The layout, which depends on the journal, will be automatically generated.
An effort is made to achieve compatibility of a range of standard LaTeX packages with each supported journal.
In addition, a consistent set of theorem-like environments is provided across journals. 


## Installation
```python
pip3 install scoop-template-engine
ste --init
```

## Quick Start
Describe the meta data of your manuscript in a `.yaml` file, such as
```yaml
# LaTeX related settings
latex:
  bibfiles: my.bib
  abstract: abstract.tex
  body: content.tex
  preamble: |-
    \usepackage{amsmath}
    \usepackage{cleveref}

# Information on your manuscript
manuscript:
  authors:
    - LMS
    - JIF
  title: Carrying the One Effectively

# Author data
authors:
  - 
    familyname: Simpson
    givenname: Lisa M.
    institutions: Harvard College
    tag: LMS

  - 
    familyname: Frink
    givenname: Jonathan I. Q.
    institutions: Springfield Heights
    tag: JIF

# Institution data
institutions:
  Harvard College: >-
    Harvard College, Cambridge, MA 02138, USA

  Springfield Heights: >-
    Springfield Heights Institute of Technology, Springfield, OR 97475, USA
```
