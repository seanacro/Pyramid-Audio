
* prints the ticket
set talk off
* ACCEPT 'ENTER TICKET # ' TO ZTICKET
* LOCATE FOR TICKET=&ZTICKET
*replace next 1 date_in with date() for year(date_in)=0
store shipper to zshipper
store date_in to zdate_in
store upper(first) to zfirst
store upper(last) to zlast
store upper(street) to zstreet
if 'A  '$CITY
 replace city with 'AUSTIN'
 else
 endif
store trim(city) to zcity
if len(trim(state))=0
 replace state with 'TX'
 else
 endif
store trim(state) to ZSTATE
store trim(str(zip)) to zzip
store phone1 to zphone1
store phone2 to zphone2
store substr(make,1,10) to zmake
store substr(model,1,10) to zmodel
store serial to zserial
store dealer to zdealer
store dop to zdop
set device to printer
set print on
set talk off
@ prow() +1,2  say zshipper
@ prow()   ,38 say zdate_in
@ prow() +2,3  say zfirst
@ prow()   ,15 say zlast
@ prow() +2,3  say TRIM(zstreet)
* if phone2>0
*  @ prow(),32 say zphone2
*  else
*  endif
@ prow() +2,3  say trim(zcity)
@ prow(),pcol()+1 say trim(zstate)
@ prow(),pcol()+1 say ltrim(TRIM(zzip))
* @ prow(),18 say zphone1
* @ prow(),41 say zdealer

@ prow() +2,3  say trim(zmake)
@ prow()   ,15 say trim(zmodel)
@ prow()   ,27 say trim(zserial)
* if year(dop)=0
*  else
*  @ prow(),42 say zdop
*  ENDIF
?'  '
?comp
@       15,4  SAY " "
?PARTS
@       28,38 SAY TYPE_DEP
@PROW()   ,45 SAY AMT_DEP
@PROW() +4,45 SAY PAID_PARTS
@PROW() +2,45 SAY PAID_LABOR
@PROW() +3,45 SAY NOTAX
@PROW() +2,10 SAY TECH
@PROW()   ,16 SAY DATE_OUT
@PROW() +1,45 SAY AMT_DEP

@PROW()+10,12 SAY TYPE_DEP
@PROW()   ,25 SAY AMT_DEP
@PROW() +1,2  SAY MAKE
@PROW()   ,15 SAY MODEL

Eject

set print off
CLEAR
