DATA results; * begin data step with given name;

INFILE DATALINES DSD MISSOVER; * DSD = Delimiter Sensitive Data; * MISSOVER = set missing variables if end of line;

LENGTH name $ 20; * set length of the name variable to max 20;

INPUT name $ phy che mat; * specified input of the data ($ = string);

CARDS; * specifies that data lines follow;
	Richmond,70,75,85
	Luke,80,90,85
	David,90,95,85
	Anton,65,75,90
	
PROC FREQ DATA = results; * runs frequency table procedure on the data;
	TABLE phy che mat; * limit procedure to these variables;

RUN;
