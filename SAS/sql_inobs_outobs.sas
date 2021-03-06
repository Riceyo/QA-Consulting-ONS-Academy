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

PROC SQL INOBS = 5; * limit the sas data set to 5 observations before running sql on the data set;
	SELECT name FROM results ORDER BY name;
QUIT;

PROC SQL;
	SELECT make, model, horsepower
	FROM sashelp.cars
	WHERE make = 'Volkswagen'
	;
QUIT;

PROC SQL OUTOBS = 10; * limit the output from sql to 10 observations;
	SELECT make, model, horsepower FROM sashelp.cars ORDER BY horsepower DESCENDING;
QUIT;

PROC SQL OUTOBS = 10; * limit the output from sql to 10 observations;
	SELECT make, model, invoice FROM sashelp.cars ORDER BY invoice DESCENDING;
QUIT;
