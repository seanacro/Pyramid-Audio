# DAYEND.PRG
This tallies all of the records marked as having transacted one way or another for the day. It prints a report to hardcopy which is reconciled with the drawer report. By hand. Which is something I aim to fix. Because comparing two sheets of paper by hand to determine if computers agree seems like a not great way to do it. 
# dayendjs.prg
Formats the same data as json for future programmatic use.
# dayendjs.py
dBase appends an "end of file" character to the end of any file it generates. This causes errors and I don't think it can be stopped. So this script removes the offending character and pretty formats the json as well. 