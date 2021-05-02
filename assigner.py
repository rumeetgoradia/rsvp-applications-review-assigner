import os
import random as rnd

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

applicantsFile = open(os.path.join(DIRECTORY, "applicants.txt"), "r")
applicants = []
numApplicants = 0
reviewsPerApplicant = 3  # this number can be changed
for line in applicantsFile:
    applicants += (reviewsPerApplicant * [line.strip()])
    numApplicants += 1
applicantsFile.close()

boardFile = open(os.path.join(DIRECTORY, "board.txt"), "r")
boardMembers = []
numBoard = 0
boardAssignments = {}
for line in boardFile:
    boardMembers.append(line.strip())
    boardAssignments[line.strip()] = []
    numBoard += 1
boardFile.close()

i = 0
while len(applicants) > 0:
    boardMember = boardMembers[i]
    assignments = boardAssignments[boardMember]
    applicantIndex = int(rnd.random() * len(applicants))
    while applicants[applicantIndex] in assignments:
        applicantIndex = int(rnd.random() * len(applicants))
    applicant = applicants[applicantIndex]
    assignments.append(applicant)
    applicants.remove(applicant)
    i += 1
    if i >= len(boardMembers):
        i = 0

assignmentsFile = open(os.path.join(DIRECTORY, "assignments.txt"), "w")
for boardMember in boardAssignments:
    assignmentsFile.write(boardMember + " (" + str(len(boardAssignments[boardMember])) + " assignments)" + "\n")
    for assignment in boardAssignments[boardMember]:
        assignmentsFile.write("\t" + assignment + "\n")
    assignmentsFile.write("\n")
assignmentsFile.close()
