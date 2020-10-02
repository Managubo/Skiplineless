[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Managubo/Skiplineless/master)

 

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
