# Graphy
A simple program that will generate a graph using LaTex and display as a pdf.

#### Requirements:
* LaTex
* Pgfplots (Package for LaTex)
* Python 3.x
    
##### Setting up Graphy:

    1. Place the graphing.tex and the graph.py in the same directory.
    2. Download LaTex and the pgfplots package for LaTex.
    3. Python should be on your computer if not download it.
    
##### Using Graphy:
    $ python graphy.py [equation]
    
    Note: If using zsh shell do the following instead to disable globbing ...
    $ noglob python graphy.py [equation]
    
    Example of usage: $ python graphy.py 2*x^2
    Note: You do have to use the * for cofficients infront of the x or else the pdf won't compile.
    
##### Process of Graphy:
    What graphy.py does is the following ...
    
    1. Takes the input from the user as the equation.
    2. Changes the graphing.tex file with the equation.
    3. Runs pdflatex on the graphing.tex.
    4. Then displays the graphing.pdf that is generated.

    

