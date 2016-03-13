# Graphy
A simple program that will generate a graph using LaTex and display as a pdf.

Requirements:

    latex
    pgfplots (Package for LaTex used to generate the graphs)
    python 3.x
    
Setting up Graphy:

    1. Place the graphing.tex and the graph.py in the same directory.
    2. Download LaTex and the pgfplots package for LaTex.
    3. Python should be on your computer if not download it.
    
Using Graphy:

    $ python graph.py [equation]
    
    Note: If using zsh shell do the following instead to disable globbing ...
    $ noglob python graph.py [equation]
    
    Example of usage: $ python graph.py 2*x^2
    Note: You do have to use the * for cofficients infront of the x or else the pdf won't compile.
    

