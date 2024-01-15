USE DRAWER
set talk off

STORE "CC"$UPPER(WHAT) TO CC
STORE "CH"$UPPER(WHAT) TO CH
STORE "EBAY"$UPPER(WHAT) TO EB
COUNT ALL TO RECS

SUM (QTY2-qty1)*VALUE FOR RECNO()<16 to CASH

SET ALTERNATE TO drawer.jso
SET ALTERNATE ON

??'{'
?'"Cash":{'
?'"method": "S",'
?'"value": ',CASH, '}'
DO CASE
	CASE RECS >15
		?','
		goto 16
		DO WHILE .NOT.EOF()
			LNG=LEN(TRIM(WHAT))-5
			PAY=SUBSTR(WHAT,1,LNG-1)
			TIK=SUBSTR(WHAT,LNG)
			?'"'+TRIM(TIK)+'":{"method":"'+TRIM(PAY)+'",'
			?'"value":',VALUE,'}'
			IF RECNO()<RECS
				?','
			ENDIF
			skip
		ENDDO
		?'}'
	OTHERWISE
ENDCASE
SET ALTERNATE TO
run start drawjs.exe
set talk on
