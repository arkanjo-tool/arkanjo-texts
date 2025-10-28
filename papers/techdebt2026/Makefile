# Makefile para compilar artigo em LaTeX com BibTeX

MAIN = techdebt
BIB  = references.bib

all: pdf

pdf: $(MAIN).tex $(BIB)
	pdflatex $(MAIN).tex
	bibtex $(MAIN)
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk

distclean: clean
	rm -f $(MAIN).pdf

