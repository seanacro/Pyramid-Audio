## dBtext is an idea that came up several years ago 
where new customer records in dBase would be duplicated as text files in a folder called dbtext. The idea was that the text file would be a good place to add arbitrary notes, part lists, and other miscellania that don't necessarily fit on a handwritten service ticket or in the dBase record (which has extremely limited space for input). Also, it makes it easy to copy/paste long part lists. 

### It turns out there's a lot more than part lists
that make sense to keep track of with a record that won't go into dBase. Emails, copies of receipts, photos of various damage that we find to customer units, etc, etc. 

### So dBtext.py 
takes about a decade worth of *999999.txt* files and creates self named directories that contain the *999999.txt* file and make an intuitive place to store and find any other relevant assets to that ticket.

### repair.py
An early iteration of dBtext.py had an error that caused a bunch of unwanted folders to populate where they weren't wanted. This simply removed those errant folders. This is a good place to note that I have no formal instruction with or professional experience with scripting. I'm wingin' it here, y'all. 

### dbtOrg is basically a scraper
It went throught the folders where we'd been dumping files related to tickets kind of willy nilly, figuring out which ticket (almost) all of the files go with, and moving them to the appropriate folder. This worked out really well and organized data going back as far as 2006 into the new folder scheme. I'm actually really happy with how well this one ended up going. 