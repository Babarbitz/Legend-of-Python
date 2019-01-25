PY=python3
TEST=pytest
RMDIR = rm -rf
MAKE = make


.PHONY: run test mantest doc clean

run:
	$(PY) src

test:
	$(TEST) src

mantest:
	$(PY) src/manualTests.py

doc:
	doxygen doxConfig
	cd Doc/Design/MIS/latex && $(MAKE) && pdflatex refman.tex  
	mv Doc/Design/MIS/latex/refman.pdf  Doc/Design/MIS/MIS.pdf
		

		
clean:
	@- $(RMDIR) html
	@- $(RMDIR) latex

