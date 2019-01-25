.PHONY: MyDoc.pdf all clean

all: MyDoc.pdf

%.tex: %.raw
	./raw2tex $< > $@

%.tex: %.dat
	./dat2tex $< > $@

MyDoc.pdf: TestPlan.tex
	latexmk -pdf -latex="pdflatex -interaction=nonstopmode" -use-make TestPlan.tex

clean:
	latexmk -CA
