USE  DRAWER
SET TALK  ON
replace all subttl with   (QTY2-QTY1)*VALUE

SUM (QTY2-qty1)*VALUE FOR RECNO()<16 to CASH
SUM QTY2*VALUE FOR 'CH'$upper(what) TO CHKSUM
SUM QTY2*VALUE FOR  'CC'$upper(WHAT) TO CCSUM
SUM QTY2*VALUE FOR  'EBAY'$upper(WHAT) TO EBSUM

SUM (QTY2-qty1)*VALUE TO TOTAL

STORE 1 TO CSQT
COUNT FOR 'CH'$UPPER(WHAT) TO CHQT
COUNT FOR 'CC'$UPPER(WHAT) TO CCQT
COUNT FOR 'EBAY'$UPPER(WHAT) TO EBQT

*SET PRINT ON
SET ALTERNATE TO START.TXT
SET ALTERNATE ON

?' DRAWER SUMMARY   ',DATE(),TIME()
?''
?''
LIST  WHAT,VALUE, QTY1,qty2, subttl off
?'==========================================='
?''
?CSQT,'Cash: ',CASH
?CHQT,'Check:',CHKSUM
?EBQT,'eBay: ',EBSUM
?CCQT,'Card: ',CCSUM
?''
?'TOTAL:',TOTAL

SET ALTERNATE TO
*SET PRINT OFF
*EJECT
