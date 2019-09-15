import csv
studentNumber  = input("Student Number: ")

def MakeTimetable(studentNumber, lines, blankTimetable, studentData, day , period):
    with open(lines) as e:
        for line in csv.reader(e):
            subjects = line
    rownum=0
    studentTimetable = []
    with open(studentData, newline='') as f:
        for row in csv.DictReader(f):
            if row['StudentNum'] == studentNumber:
                studentRow = (row)
            rownum+=1
    with open(blankTimetable, newline = '') as g:
        for row1 in csv.reader(g):
            studentTimetableUnreplaced = ' '.join(row1)
            for i in range(len(subjects)-1):
                studentTimetableUnreplaced = (studentTimetableUnreplaced.replace(subjects[i], studentRow[subjects[i]]))
            studentTimetable.append(studentTimetableUnreplaced)

        for i in range(len(studentTimetable)):
            studentTimetable[i]= studentTimetable[i].split()

##        for item in studentTimetable:
##            print(item)
            
    return (studentTimetable[day-1][period])


print(MakeTimetable(studentNumber, "Lines.csv", "timetable.csv","studentData.csv", 3,1))
