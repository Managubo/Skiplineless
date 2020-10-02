[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Managubo/Skiplineless/master)
.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/Managubo/Skiplineless/master
 

# Skiplineless

Version 0.1.0

The purpose of Skiplineless is to automatically transform "chopped" fasta files in more nicely structured ones. 
With Skiplineless we read a given .txt file with gene IDs and sequences which are "chopped" in short lines and then we make those sequences to go
all the way in a single line, so that the result of the code is a list of gene ID, in the next line the sequence, then an empty line after which 
the next gene ID, sequence and emty line will be printed, and so on and so on.

You can both download or clone the project to use it with your own fasta .txt files.
The main script performing the transformation of "chopped" files is called "No_line_skips.py" and you can find it in the main folder.

## Installation

Prerequisites:
> Python 3.5+

Packages and versions:
> arrow==0.16.0
> binaryornot==0.4.4
> certifi==2020.6.20
> chardet==3.0.4
> click==7.1.2
> cookiecutter==1.7.2
> flake8==3.8.3
> idna==2.10
> Jinja2==2.11.2
> jinja2-time==0.2.0
> MarkupSafe==1.1.1
> mccabe==0.6.1
> poyo==0.5.0
> pycodestyle==2.6.0
> pyflakes==2.2.0
> python-dateutil==2.8.1
> python-slugify==4.0.1
> requests==2.24.0
> six==1.15.0
> text-unidecode==1.3
> urllib3==1.25.10


## Project organization

```
.
├── .gitignore
├── CITATION.md
├── LICENSE.md
├── README.md
├── requirements.txt
├── bin                <- Compiled and external code, ignored by git (PG)
│   └── external       <- Any external source code, ignored by git (RO)
├── config             <- Configuration files (HW)
├── data               <- All project data, ignored by git
│   ├── processed      <- The final, canonical data sets for modeling. (PG)
│   ├── raw            <- The original, immutable data dump. (RO)
│   └── temp           <- Intermediate data that has been transformed. (PG)
├── docs               <- Documentation notebook for users (HW)
│   ├── manuscript     <- Manuscript source, e.g., LaTeX, Markdown, etc. (HW)
│   └── reports        <- Other project reports and notebooks (e.g. Jupyter, .Rmd) (HW)
├── results
│   ├── figures        <- Figures for the manuscript or reports (PG)
│   └── output         <- Other output for the manuscript or reports (PG)
└── src                <- Source code for this project (HW)

```


## License

This project is licensed under the terms of the [MIT License](/LICENSE.md)

## Citation

Please [cite this project as described here](/CITATION.md).
