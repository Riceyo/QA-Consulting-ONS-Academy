DATA results; * begin data step with given name;

TITLE1 "Student Results Data"; * give the data set a title;
TITLE2 "&SYSDATE &SYSTIME"; * multiple titles; * get date and time from system;

FOOTNOTE1 "QA Consulting 2017"; * give the data set a footnote;
FOOTNOTE2 "Office for National Statistics 2017"; * multiple footnotes;

INFILE DATALINES DSD MISSOVER; * DSD = Delimiter Sensitive Data; * MISSOVER = set missing variables if end of line;

LENGTH name $ 20; * set length of the name variable to max 20;

INPUT name $ phy che mat; * specified input of the data ($ = string);

LABEL phy = "physics"; LABEL che = "chemistry"; LABEL mat = "mathematics";

CARDS; * specifies that data lines follow; * missing data OK due to MISSOVER;
	Richmond,70,75,85
	Luke,65,90,85
	David
	Anton,65,75,90
	Binay,70
	Jack,65,75,65
	Harvey,80,75,70
; * end data;

PROC PRINT LABEL;

PROC PRINT;
	VAR NAME; * limit print to only name variable;
	
DATA resultsnameonly; SET results; * create new data set from results data set;
	KEEP NAME; * only keep these variables;
	
PROC PRINT DATA = resultsnameonly;

DATA resultsnoname; SET results; * create new data set from results data set;
	DROP NAME; * drop these variables;
	
PROC PRINT DATA = resultsnoname;
