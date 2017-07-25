DATA results; * begin data step with given name;

TITLE1 "Student Results Data"; * give the data set a title;
TITLE2 "Playing With Procedures"; * multiple titles;

FOOTNOTE "QA Consulting 2017"; * give the data set a footnote;

INFILE DATALINES DSD MISSOVER; * DSD = Delimiter Sensitive Data; * MISSOVER = set missing variables if end of line;

LENGTH name $ 20; * set length of the name variable to max 20;

INPUT name $ phy che mat; * specified input of the data ($ = string);

LABEL phy = "physics"; LABEL che = "chemistry"; LABEL mat = "mathematics";

CARDS; * specifies that data lines follow;
	Richmond,70,75,85
	Luke,65,90,85
	David,90,95,85
	Anton,65,75,90	
; * end data;

PROC GCHART DATA = results; * run the gchart procedure on the data;
	VBAR phy/DISCRETE; * treats variable as discrete;

PROC GCHART DATA = results; * run the gchart procedure on the data;
	VBAR che/DISCRETE; * treats variable as discrete;
	
PROC GCHART DATA = results; * run the gchart procedure on the data;
	VBAR mat/DISCRETE; * treats variable as discrete;
