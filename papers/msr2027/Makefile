# Makefile para compilar artigo em LaTeX com BibTeX

MAIN = msr
BIB  = references.bib

FIGURES_DIR = figures

FIGURES = $(FIGURES_DIR)/pipeline.pdf

all: pdf

figures: $(FIGURES)

$(FIGURES_DIR)/%.pdf: $(FIGURES_DIR)/%.tex
	pdflatex -interaction=nonstopmode -halt-on-error \
		-output-directory=$(FIGURES_DIR)/ \
		-jobname=$* \
		$<

pdf: $(MAIN).tex $(BIB)
	pdflatex $(MAIN).tex
	bibtex $(MAIN)
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk

distclean: clean
	rm -f $(MAIN).pdf

