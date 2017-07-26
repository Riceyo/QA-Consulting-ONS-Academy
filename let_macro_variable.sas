DATA results; * begin data step with given name;

TITLE1 "Student Results Data"; * give the data set a title;
TITLE2 "&SYSDATE &SYSTIME"; * multiple titles; * get date and time from system;

FOOTNOTE1 "QA Consulting 2017"; * give the data set a footnote;
FOOTNOTE2 "Office for National Statistics 2017"; * multiple footnotes;

INFILE DATALINES DSD MISSOVER; * DSD = Delimiter Sensitive Data; * MISSOVER = set missing variables if end of line;

LENGTH name $ 20; * set length of the name variable to max 20;

INPUT idref name $ phy che mat; * specified input of the data ($ = string);

LABEL phy = "physics"; LABEL che = "chemistry"; LABEL mat = "mathematics";

CARDS; * specifies that data lines follow; * missing data OK due to MISSOVER;
	101,Richmond,70,75,85
	102,Luke,65,90,85
	103,David
	104,Anton,65,75,90
	105,Binay,70
	106,Jack,65,75,65
	107,Harvey,80,75,70
; * end data;

%LET passmark = 70;

PROC PRINT DATA = results;

PROC PRINT DATA = results;
	WHERE phy < &passmark;
