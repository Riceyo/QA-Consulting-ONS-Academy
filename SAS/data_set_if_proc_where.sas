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

DATA resultsallpassed;
	SET results;
	IF phy > 69 AND che > 69 AND mat > 69; * only include data in new data set that meets this IF clause;
	
PROC PRINT;

PROC MEANS DATA = results;
	WHERE phy > 69 AND che > 69 AND mat > 69; * only run the procedure on data that meets this WHERE clause;
