USE TODAY
SET CENTURY ON
SET TALK OFF

COUNT ALL TO RECS
GOTO TOP

IF RECS>0
	SET ALTERNATE TO dayend.jso
	SET ALTERNATE ON
	SET CONSOLE OFF

	?'{'
	DO WHILE .NOT.EOF()
		TCK=STR(TICKET)
		DO CASE
			CASE PAIDDATE=DATE()
				?'"'+LTRIM(TCK)+'":{'
				?'"method":"'+TRIM(TYPE_PAY)+'",'
				?'"value":'+STR(BALANCE,7,2)+','
				?'"name":"'+TRIM(LAST)+', '+TRIM(FIRST)+'"}'
				IF RECNO()<RECS
					?','
				ENDIF
				SKIP
			CASE DATE_DEP=DATE()
				?'"'+LTRIM(TCK)+'":{'
				?'"method":"'+TRIM(TYPE_DEP)+'",'
				?'"value":'+STR(AMT_DEP,7,2)+','
				?'"name":"'+TRIM(LAST)+', '+TRIM(FIRST)+'"}'
				IF RECNO()<RECS
					?','
				ENDIF
				SKIP
			OTHERWISE
			SKIP
		ENDCASE
	ENDDO
	?'}'
	SET ALTERNATE TO
	SET CONSOLE ON
ENDIF
*run dayendjs.exe

