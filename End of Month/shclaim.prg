set talk off
use login
goto bottom
skip -2000

do while .not.eof()
  store UPSCOST to cost
  do case
    case NOTAX<>0
      skip
    case cost=0
      skip

    case cost<20.01
      replace NOTAX with 20
      ? TICKET, 'claims', NOTAX, 'on our cost', cost

    case cost<25.01
      replace NOTAX with 25
      ? TICKET, 'claims', NOTAX, 'on our cost', cost

    case cost<30.01
      replace NOTAX with 30
      ? TICKET, 'claims', NOTAX, 'on our cost', cost

    case cost<35.01
      replace NOTAX with 35
      ? TICKET, 'claims', NOTAX, 'on our cost', cost

    case cost>35
      replace NOTAX with cost
      ? TICKET, 'claims', NOTAX, 'on our cost', cost

    otherwise
  endcase
enddo
set talk on
