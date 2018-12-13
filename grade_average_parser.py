# -*- coding: utf-8 -*-
"""
Created on: Tuesday night after a rough day, 2018

@author: Def not Fifi
"""

import bs4
import re


###############################################
# Please copy and paste the page source from: #
#                                             #
# CAMPUS                                      #
# -> PRÜFUNGSVERWALTUNG                       #
# --> NOTENSPIEGEL                            #
# ---> (...) BACHELOR ^(i)                    #
# (You must click on the i.)                  #
#                                             #
# Then paste it into source.txt or save it to #
# source.txt and drag-and-drop it here.       #
###############################################


# Add comma-separated list of subjects you don't want to include here
TD_BLACKLIST = set(["Orientierungsprüfung"])

PATH = ["CAMPUS", "PRÜFUNGSVERWALTUNG",
        "NOTENSPIEGEL", "(...) BACHELOR ^(i)"]

GRADE_PATTERN = "^\d,\d$"

def generate_path(path_list):
    modded_path_list = [path_list[0]]
    for counter in range(1, len(path_list)):
        modded_path_list.append(counter*"-" + "> "
                                + path_list[counter])
    
    return "\n".join(modded_path_list)


def get_td(tds, index):
    return tds[index].contents[0].strip()

def is_grade(string):
    return re.match(GRADE_PATTERN, string) != None

def grade_to_float(grade):
    return float(grade.replace(",", "."))

def float_to_grade(float_num):
    rounded_float = round(float_num, 3)
    return str(rounded_float).replace(".", ",")


pathstr = generate_path(PATH)

''' source = input("Please copy and paste the page source at:\n"
		   + pathstr + "\n"
		   + "(You must click on the i.)\n\n")
'''
with open("source.txt", "r") as srcfile:
    source = srcfile.read()

### PARSE ###
soup = bs4.BeautifulSoup(source, "html.parser")
table_lists = soup.select("div.content > form > table")
grade_table = table_lists[1]
table_rows = grade_table.find_all("tr")

# Find rows containing relevant values like grade and number of ECTS Points
content_rows = []
for row in table_rows:
    if row.td != None and row.td.attrs["class"][0] == "tabelle1":
        content_rows.append(row)

# Find relevant table entries and calculate their weighted average
weighted_avgs = 0
total_credits = 0
for row in content_rows:
    current_tds = row.find_all("td")
    
    subject_name = get_td(current_tds, 1)
    if subject_name in TD_BLACKLIST:
        print(subject_name + " has been ignored as requested!\n")
        continue
    
    passed = get_td(current_tds, 5)
    if passed != "bestanden":
        print("You didn't pass " + subject_name + "! :(")
        continue
    
    grade = get_td(current_tds, 4)
    if not is_grade(grade):
        print("ERROR: Not a grade!!!")
        break
    
    credit_points = get_td(current_tds, 6)
    if not credit_points.isnumeric():
        print("ERROR: Not valid number of credits!!!")
        break
	
    print((   "SUBJECT: {}\n"
	    + "GRADE:   {}\n"
	    + "CREDITS: {}\n\n").format(subject_name,
					grade,
					credit_points))
    weighted_avgs += int(credit_points) * grade_to_float(grade)
    total_credits += int(credit_points)

average_grade = weighted_avgs / total_credits
print("Your average grade is: " + float_to_grade(average_grade))
