
USE AD

* Did you know that if you ask dBase how many records
* are in an empty table, it will return a "1" instead
* of "0"? Anyway, that means we have to be slightly
* more creative about how we tell dBase where to start.
COUNT FOR TICKET > 1 TO REC
REC = REC + 1
USE

* This python script will open a popup window
* and will ask the user for ticket numbers.
* This is the part where new records get added to the
* AD table.
RUN "C:\vDosPlus\start.exe" python "C:\dbase\pyScripts\eBay\eBay.py"

* dBase has no way of knowing that the above python script
* is or is not still working we have to make it wait for
* the user to let it know when it may continue
WAIT "Press ENTER to continue"
CLEAR
USE AD
GOTO REC

* At this point, all the new records have been
* added to the AD table but we still need to put
* a an entry into dBtext and print the ticket.
* This will go through every record that wasn't
* already in AD and do that, while prompting the
* user so tickets and records stay matched up.
DO WHILE .NOT.EOF()
	? "Load TICKET #", TICKET, "into dot matrix printer"
	WAIT "Press ENTER to start print"
	DO EBAYPRT
	DO TXTDBT
	CLEAR
	SKIP
ENDDO

? "Now go to eBay and print the labels"

