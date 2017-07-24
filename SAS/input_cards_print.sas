DATA results; * begin data step with given name;

INPUT name $ phy che mat; * specified input of the data ($ = string);

CARDS; * specifies that data lines follow;
	Richmond 70 75 85
	Luke 80 90 85
	David 90 95 85
	Anton 65 75 90

PROC PRINT; * print the data;

RUN;
