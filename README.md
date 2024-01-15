
## My company largely runs on dBase III, 
which is a legacy database system released in 1984. That's right, our company infrastructure is so old it wears white New Balance sneakers and thinks culture peaked at Woodstock '99. There have been no upgrades, (almost) all of the system was scripted by my boss and "features" have been bolted on by him as needed and as time has allowed. This has left us with a very spartan infrastructure that is mostly known only to him as the naming conventions and logic of the various scripts, tables, and features were all implemented by him as he thought of them.
<br><br>
Migrating to a modern solution is out of the question for a number of reasons but the important takeaway is that dBase III is our chosen business platform, dBase III is mission critical, and compatibility with dBase III is the primary consideration for any software or hardware decisions. Half of the PCs in our shop still run a 32 bit installation of Windows 10 and the rest rely on VDOSplus as an emulation layer because dBase won't run natively on 64 bit architecture. 
###### I expect that this will be a significant problem when Windows 10 hits EOL since Win11 does not and will not offer a 32 bit option.</h> But I digress.
<br>
There are several challenges to using this system and one of them is that very few people are familiar with Command Line Interfaces, much less ancient CLIs that interface with dead business software. Training new hires on the technological equivalent of Latin can difficult.
<br><br>
So, with all that said: I have two primary goals with this project. 
<br>
  1) I want to sand down as many of the rough edges as I can, as smooth as I can. If a person is doing something by hand that can be scripted, it should be scripted. If a person is having to unnecessarily remember the name of a script or table or expression, it should be worked into the background as much as possible. System output (onscreen and printed) should be formatted in a human-friendly, easy to understand manner that any person with any level of experience at the company will understand immediately and intuitively.
<br>
  2) A massive amount of our data is transcribed by hand. Often more than once. All things considered, we actually have a very low error rate. But the potential for errors, including catastrophic errors, is *ernormous*. If we have data that exists digitally, as a PDF, on a website, in our own system, etc... it should be programmatically copied to any tables, emails, forms, etc that require it.
