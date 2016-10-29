# Display email and count of max emailing user

#9.4 Write a program to read through the mbox-short.txt and figure out
#who has the sent the greatest number of mail messages. The program
#looks for 'From ' lines and takes the second word of those lines as
#the person who sent the mail. The program creates a Python dictionary
#that maps the sender's mail address to a count of the number of times
#they appear in the file. After the dictionary is produced, the program
#reads through the dictionary using a maximum loop to find the most
#prolific committer.

fname = raw_input("Enter file name: ")
if len(fname) < 1: 
    fname = "mbox-short.txt"

fh = open(fname)
maxcnt = 0

lwords = list()
emailcnt = dict()

for line in fh:
    if line.startswith('From:'):
        lwords = line.split()
        email = lwords[1]  # email ID from line
        emailcnt[email] = emailcnt.get(email,0) + 1
        if emailcnt[email] > maxcnt:  
            maxcnt = emailcnt[email]
            maxemail = email


print maxemail, maxcnt

