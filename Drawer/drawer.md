# DRAWER.PRG
The original DRAWER.PRG script accepted the day's receipts, cash, and checks as input and tallied the business for the day.
The output has been modified to be more immediately understood at a glance and thus easier to reconcile at the end of each day.
Originally, the only output was printed hardcopy which was kept in a drawer should it need to be referenced again. Now it also creates a copy of the output as a txt file and stores it on the company server, arranged by date for easier reference.
# drawjs.prg
The data is also saved as a json file for future programmatic use. 
# drawerjs.py
dBase appends an "end of file" character to the end of any file it generates. This causes errors and I don't think it can be stopped. So this script removes the offending character and pretty formats the json as well. 
# drStart.PRG
Similar to DRAWER.PRG except it produces a report of what cash is in the drawer at the end of the day, so it's a Start Sheet for the next day's business.