print "Scores and Grades"
import random
for i in range ( 10 ):
    randomScore = random.randint( 60, 100 )
    if randomScore >=60 and randomScore < 70:
        print "Score:", randomScore, "; Your grade is D"
    elif randomScore >=70 and randomScore < 80:
        print "Score:", randomScore, "; Your grade is C"
    elif randomScore >=80 and randomScore < 90:
        print "Score:", randomScore, "; Your grade is B"
    elif randomScore >=90 and randomScore < 100:
        print "Score:", randomScore, "; Your grade is A"
    else:
        print "Grading error"
