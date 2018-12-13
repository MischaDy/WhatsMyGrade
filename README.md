# WhatsMyGrade
## Overview
INTENDED FOR USERS OF UNI TÜBINGEN, GERMANY! Get the page source of your "Notenspiegel" from Campus, overwrite `source.txt` with it, go back to `grade_average_parser.py` and click run!

You can add the subjects you want to exlude in a comma-separated list (`TD-BLACKLIST`) at the top. 'Orientierungsprüfung' is included by default, since it's just a merge of two other subjects you've passed.

If you want to get a taste first, try it online:
https://repl.it/@Grust/AverageGrade/


## Features
- Exclude predefined subjects from consideration (unsing the blacklist).
- Automatically exclude failed subjects from consideration.
- Get a quick overview over all the subjects you've passed, their assigned number of ECTS Points, and the grade you've received.
- Most importantly, directly calculate your current average grade, weighted by the ECTS Points of the subjects.


## **_WARNING_**
This project comes with no warranty whatsoever! If you think that the script isn't calculating the true weighted average, then don't hesitate to contact me. However, I am generally not responsible for your usage of the program. In particular, any mistakes or suboptimal decisions you make regarding your study, which are based on a malfunctioning of the program, *are exclusively your personal responsibility*.
