DATA results; * begin data step with given name;

TITLE1 "Student Results Data"; * give the data set a title;
TITLE2 "Playing With Procedures"; * multiple titles;

FOOTNOTE "QA Consulting 2017"; * give the data set a footnote;

INFILE DATALINES DSD MISSOVER; * DSD = Delimiter Sensitive Data; * MISSOVER = set missing variables if end of line;

LENGTH name $ 20; * set length of the name variable to max 20;

INPUT name $ phy che mat; * specified input of the data ($ = string);

CARDS; * specifies that data lines follow;
	Richmond,70,75,85
	Luke,80,90,85
	David,90,95,85
	Anton,65,75,90	
; * end data;

PROC MEANS DATA = results; * run the means procedure on the data;

PROC CORR DATA = results; * run the correlation procedure on the data;

PROC UNIVARIATE DATA = results; * run the univariate procedure on the data;
	var phy che; * only run on these variables;

RUN;
