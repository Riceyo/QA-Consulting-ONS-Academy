DATA results; * begin data step with given name;

INFILE DATALINES DSD MISSOVER; * DSD = Delimiter Sensitive Data; * MISSOVER = set missing variables/records if end of line;

LENGTH name $ 20; * set length of the name variable/record to 20;

INPUT name $ phy che mat; * specified input of the data ($ = string);

CARDS; * specifies that data lines follow;
	Richmond,70,75,85
	Luke,80,90,85
	David,90,95,85
	Anton,65,75,90
	
PROC FREQ DATA = results; * runs buildin freq function;

RUN;
