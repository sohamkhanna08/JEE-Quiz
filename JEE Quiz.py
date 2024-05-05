restart_1=0
while (restart_1=="Y" or "y"):        
    Title = "* JEE Quiz *"
    print("*" * len(Title))
    print(Title)
    print("*" * len(Title))
    print("\nPlease pick a choice from the following :-")
    print(" 1. CBSE Level - The standard of the questions in this level will match the questions in CBSE Exam.")
    print(" 2. Mains Level - The standard of the questions in this level will match the questions in Mains Exam.")
    print(" 3. Advance Level - The standard of the questions in this level will match the questions in Advance Exam.")
    print(" 4. Exit Quiz")
    choice = int(input("\nEnter the quiz number you want to attempt : "))
    name = input("Enter your name : ")
    adm_no = int(input("Enter your admission number : "))
    print()
    
    # CBSE Level quiz : TASK 1
    if (choice==1):
        Title1 = "* CBSE QUIZ *"
        print("*" * len(Title1))
        print(Title1)
        print("*" * len(Title1))
        print()
        Title2 = "* Instructions For CBSE Quiz *"
        print("*" * len(Title2))
        print(Title2)
        print("*" * len(Title2))
        print()
        print("The maximum marks of this quiz is 40 . This level contains 10 jumbled questions of Physics , Chemistry and Mathematics . ")  
        print("Questions may contain NUMERIC as well as MCQ . All questiosn are compulsory . ")
        print("•Instruction for MCQ :- ")
        print("  Each question has 4 choices (1), (2), (3) and (4), out of which ONLY ONE CHOICE is correct. ")
        print("•Instruction for NUMERIC :- ")
        print("  The answer to each question is an integer ranging from 0 to 9 (both inclusive) ")
        print("•Marking Scheme :- ")
        print("  MCQ questions and NUMERIC questions :+4 for correct answer, -1 (negative marking) for incorrect answer, 0 for all other cases. ")
        print() 
        # show questions
        Title3 = "* Questions *"
        print("*" * len(Title3))
        print(Title3)
        print("*" * len(Title3))
        print()

        Questions = {  1 :{ "question" : "A bus travelling the first one third distance at a speed of 10km/h, the next one third at 20km/h and the last one third at 60km/h. \
    The average speed of the bus is :- \n1) 30km/hr \n2) 45km/hr \n3) 18km/hr \n4) 9km/hr" ,
                                   "answer" : "3" },
                       2 :{ "question" : "Two particles of masses 100 g and 400 g has position vectors (2i + 4j + 12k) cm and (-6i + 3j + 2k) cm respectively. \
    Find the position vector or centre of mass will be :- \n1) 4.4i + 3.2j + 4k \n2) -4i+7j+14k \n3) -8i+j+10k \n4) 4.8i+2.4j+3.6k",
                                   "answer" : "1" },
                       3 :{ "question" : "The density of water at room temperature is 1.0g/ml. How many molecules are there in a drop of water if its volume is 0.05ml ? \n1) 1.68×10²¹ \
    \n2) 6.022×10²³ \n3) 3.011×10²² \n4) 1.88×10²¹",
                                   "answer" : "1" },
                       4 :{ "question" : "Carbon tetrachloride has no net dipole moment because of :- \n1)Its planar structure \n2) Its regular tetrahedral geometry \
    \n3) Similar sizes of C and Cl atoms \n4) Similar electron affinities of C and Cl",
                                   "answer" : "2" }, 
                       5 :{  "question" : "The smallest set A such that A ∪ {4,5,6} = {1,2,3,4,5,6} is :- \n1) {1,2,3,4,5,6} \n2) {4,5,6} \n3) {1,2,3} \n4) {⌀}" ,
                                   "answer" : "3" },
                       6 :{ "question" : "The equation of the line passing through (1,5) and perpendicular to the line 3x – 5y + 7 = 0 is :- \n1) 5x + 3y - 20 = 0 \n2) 3x - 5y + 7 = 0 \
    \n3) 3x - 5y + 6 = 0 \n4) 5x + 3y + 7 = 0",
                                   "answer" : "1" },
                       7 :{ "question" : "If A.M and G.M of two positive numbers 'a' and 'b' (a < b) are 10 and 8 respectively, then a-b is :- \n1) ±12 \n2) 12 \n3) -12 \n4) 10",
                                   "answer" : "3" },
                       8 :{ "question" : "A crickter catches a ball of mass 150g in 0.1s, moving with speed 20m/s. The force experienced by him will be 10x Newton. Find the value of x ?",
                                   "answer" : "3" },
                       9 :{ "question" : "Numer of angular nodes for 4d orbital is ?" ,
                                   "answer" : "2" },
                       10 :{ "question" : "If i² = -1, then the sum i + i² + i³ +....upto 1000 terms is equal to ?",
                                   "answer" : "0" } }
        correct_ques=0               
        score=0                         
        i=0                            
        for question in Questions :
            while i<= len(Questions) :
                print("Question",i+1, )
                break
            print(Questions[question]['question'])
            user_answer = input("Enter Answer : ")
            
            if (user_answer == Questions[question]['answer']) :
              print("Correct Answer ! ")
              score+=4
              correct_ques+=1
            else :
              score-=1
              print("Incorrect Answer ! Correct answer is : ", Questions[question]['answer'] )
            print("\n")  
            i+=1
            
        print ( "{0} attempted {1} questions correctly out of 10".format(name,correct_ques) )
        print ( "{0}'s score is {1} out of 40".format(name,score) )

        if score == 40 :
            print ( "Excellent , Full Marks ! " )
        elif (score >= 30) :
            print ("Satisfactory Result ! ")
        elif (score >= 10) :
            print ("Have another practice ! ")    
        elif score <= 10 :
            print ("Poor Performance ! ")

    # MAINS Level quiz : TASK 2
    if (choice==2):
        Title4 = "* MAINS QUIZ *"
        print("*" * len(Title4))
        print(Title4)
        print("*" * len(Title4))
        print()
        Title5 = "* Instructions For MAINS Quiz *"
        print("*" * len(Title5))
        print(Title5)
        print("*" * len(Title5))
        print()
        print("The maximum marks of this quiz is 40 . This level contains 10 jumbled questions of Physics , Chemistry and Mathematics . ")  
        print("Questions may contain NUMERIC as well as MCQ . All questiosn are compulsory . ")
        print("•Instruction for MCQ :- ")
        print("  Each question has 4 choices (1), (2), (3) and (4), out of which ONLY ONE CHOICE is correct. ")
        print("•Instruction for NUMERIC :- ")
        print("  The answer to each question is an integer ranging from 0 to 9 (both inclusive) ")
        print("•Marking Scheme :- ")
        print("  MCQ questions and NUMERIC questions :+4 for correct answer, -1 (negative marking) for incorrect answer, 0 for all other cases. ")
        print() 
        # show questions
        Title6 = "* Questions *"
        print("*" * len(Title6))
        print(Title6)
        print("*" * len(Title6))
        print()
        
        Questions = {  1 :{ "question" : "If (3i + 2j + k) and (i - 2j + 3k) represent the adjacent sides of a parallelogram, then the area of this parallelogram is :- \n1) 4√3 \n2) 6√3\
    \n3) 8√3 \n4) 12√3" ,
                                   "answer" : "3" },
                       2 :{ "question" : "The velocity of the particle moving along the X-axis is given as a function of its position by: v(x) = 4 - 3x.\
    The acceleration of the particle as a function of its position is given by :- \n1) a(x) = 3(4 - 3x) \n2) a(x) = 3(3x - 4) \n3) a(x) = 6(4 - 3x) \n4) a(x) = 6(3x - 4)",
                                   "answer" : "2" },
                       3 :{ "question" : "The maximum number of electrons in a subshell having the same value of spin quantum number is given by :- \n1) l+2 \n2) 2l+1 \
    \n3) 2(2l+1) \n4) None",
                                   "answer" : "2" },
                       4 :{ "question" : "Which of the following orbitals has two spherical nodes ? \n1) 2s \n2) 4p  \n3) 3d \n4) 5f",
                                   "answer" : "2" }, 
                       5 :{  "question" : "If the focus and vertex of a parabola are (2,3) and (-1,1) respectively, then the directrix is :- \n1) 3x + 2y + 14 = 0 \n2) 3x + 2y - 25 = 0 \
    \n3) 2x - 3y + 10 = 0 \n4) 2x - 3y + 14 = 0" ,
                                   "answer" : "1 " },
                       6 :{ "question" : "The number of 4 letter words (with or without meaning) that can be formed from the 9 letters of the word ‘PRACTICAL’ is :- \
    \n1) 1206 \n2) 1566 \n3) 66 \n4) 1584",
                                   "answer" : "1" },
                       7 :{ "question" : "10 arithmetic means are inserted between 3 and 168, then the sum of first two arithmetic means is equal to :- \
    \n1) 71 \n2) 41 \n3) 51 \n4) 61",
                                   "answer" : "3" },
                       8 :{ "question" : "Starting from rest, a particle moves in a straight line with uniform acceleration 1m/s². The displacement (in metres) of the particle in the \
    third second of its motion is ?",
                                   "answer" : "2" },
                       9 :{ "question" : "The ratio of the masses of methane and ethane in a gas mixture is 4:5. The ratio of number of their molecules in the mixture is x:y. \
    The value of (x + y) is ? (Molar mass of C=12, H=1)" ,
                                   "answer" : "5" },
                       10 :{ "question" : "The number of five digit numbers with distinct digits and 3 at units place is (448)k, then k is equal to ?",
                                   "answer" : "6" } }
        correct_ques=0               
        score=0                         
        i=0                            
        for question in Questions :
            while i<= len(Questions) :
                print("Question",i+1, )
                break
            print(Questions[question]['question'])
            user_answer = input("Enter Answer : ")
            
            if (user_answer == Questions[question]['answer']) :
              print("Correct Answer ! ")
              score+=4
              correct_ques+=1
            else :
              score-=1
              print("Incorrect Answer ! Correct answer is : ", Questions[question]['answer'] )
            print("\n")  
            i+=1
            
        print ( "{0} attempted {1} questions correctly out of 10".format(name,correct_ques) )
        print ( "{0}'s score is {1} out of 40".format(name,score) )

        if score == 40 :
            print ( "Excellent , Full Marks ! " )
        elif (score >= 30) :
            print ("Satisfactory Result ! ")
        elif (score >= 10) :
            print ("Have another practice ! ")    
        elif score <= 10 :
            print ("Poor Performance ! ")
            
    # ADVANCE level quiz : TASK 1
    if (choice==3):
        Title8 = "* ADVANCE QUIZ *"
        print("*" * len(Title8))
        print(Title8)
        print("*" * len(Title8))
        print()
        Title9 = "* Instructions For ADVANCE Quiz *"
        print("*" * len(Title9))
        print(Title9)
        print("*" * len(Title9))
        print()
        print("The maximum marks of this is 40 . This level contains 10 jumbled questions of Physics , Chemistry and Mathematics . ")  
        print("Questions may contain NUMERIC as well as MCQ . The user may skip the question if not able to answer . ")
        print("•Instruction for MCQ :- ")
        print("  Each question has 4 choices (A), (B), (C) and (D), out of which ONLY ONE CHOICE is correct. ")
        print("•Instruction for NUMERIC :- ")
        print("  The answer to each question is an integer ranging from 0 to 9 (both inclusive) ")
        print("•Marking Scheme :- ")
        print("  MCQ questions :+4 for correct answer, -1 (negative marking) for incorrect answer, 0 for all other cases. ")
        print("  NUMERIC questions :+4 for correct answer, 0 for all other cases. There is no negative marking ")
        print() 
        # show questions
        Title10 = "* Questions *"
        print("*" * len(Title10))
        print(Title10)
        print("*" * len(Title10))
        print()
        Questions = {  1 :{  "question" : '''Select correct statement:- 
    1) Plaster of paris is a hemihydrate of CaSO4 obtained by heating the gypsum around 300 K.
    2) Sodium carbonate is used in hard-water softening. 
    3) Sodium peroxide reacts with hot water giving hydrogen peroxide.
    4) The mobilities of the alkali metal ions in aqueous solutions are Li+ > Na+ > K+ > Rb+ > Cs+''',
                                   "answer" : "2" },
                       2 :{ "question" : '''Equation of possible common tangents to y^2 = 8(x – 3) and x^2 = 8(y – 3) is :\n1) 2x + y = 1\n2) x – y = 5
    3) x – 2y + 5 = 0\n4) None of these''',
                                   "answer" : "3" },
                       3 :{ "question" : '''Two cars X and Y are moving with speed 15 m/s and 11 m/s respectively in opposite directions approaching
    each other from far. The driver in car X blows a horn which has components of frequencies ranging from 650 Hz to 800 Hz. The band width of frequencies
    is thus 150 Hz, speed of sound is 340 m/s. The correct statement for observer in car Y is :\n1) The bandwidth of frequencies is 150 Hz
    2) The bandwidth of frequencies is 122 Hz\n3) Speed of sound of horn is 351 m/s\n4) None of these''',
                                   "answer" : "3" },
                       4 :{ "question" : '''In a hypothetical solid, C atoms forming cubical closed packed lattice. A atoms occupy all tetrahedral void and
    B atom occupy all octahedral voids. There is no distortion in ccp lattice. Fraction of body diagonal not covered up by atoms is :
    1) 0.76\n2) 0.24\n3) 0.68\n4) 0.12 ''',
                            "answer" : "2" }, 
                       5 :{  "question" : '''Consider the planes P1 : 2x + y + z + 4 = 0, P2 : y – z + 4 = 0 and P3 : 3x + 2y + z + 8 = 0. Let L1, L2, L3
    be the lines of intersection of the planes P2 and P3, P3 and P1, and P1 and P2 respectively. Then :
    1) Atleast two of the lines L1, L2 and L3 are non-parallel\n2) The three planes intersect in a line\n3) The three planes form a triangular prism
    4) None of these ''' ,
                                   "answer" : "2" },
                       6 :{ "question" : '''If the quadratic equation x^2 + 2ax + b(a – 1) = 0 has real roots for all real values of a and b, then
    which of the following is correct :\n1) Greatest value of b is 2\n2) No such value of b is possible\n3) Least value of b is 0\n4) b can be any integer''',
                                   "answer" : "3" },
                       7 :{ "question" : '''Which molecule is having same electronic geometry as well as molecular geometry as ZrF3^- :
    1) IF\n2) IF3\n3) IF5\n4) IF7''',
                                   "answer" : "4" },
                       8 :{ "question" : '''A string of mass 0.2 kg and length 2m is tied at two ends to fixed supports under a tension of 10 N. A point P
    on the string is found to travel from one extreme to other in 0.1s. Taking one end as x = 0 and the other end x = 2 m and t = 0 as the time when P is at
    rest. (Position of P is x) The correct statement will be :\n1) For 0 < t < 0.1s, energy flows across P in positive x-direction for 0 < x < 1 m .
    2) For 0 < t < 0.05 s, energy flows across P in negative x-direction for 0 < x < 1m\n3) At t = 0.05 s, rate of energy flow through P is zero for x = 0.5 m .
    4) None of these''',
                            "answer" : "2" },
                       9 :{  "question" : '''If a, b, c be three natural numbers in A.P. and a + b + c = 30, then the possible number of values of
    a, b, c is ______''' ,
                                   "answer" : "19" },
                       10 :{ "question" : '''Which molecule is having same electronic geometry as well as molecular geometry as XeFO4:
    1) NCl3\n2) PCl5\n3) CH4\n4) SF4''',
                                   "answer" : "2" } }
        correct_ques=0               
        score=0                         
        i=0                            
        for question in Questions :
            while i<= len(Questions) :
                print("Question",i+1, )
                break
            print(Questions[question]['question'])
            user_answer = input("Enter Answer : ")
            
            if (user_answer == Questions[question]['answer']) :
              print("Correct Answer ! ")
              score+=4
              correct_ques+=1
            else :
              score-=1
              print("Incorrect Answer ! Correct answer is : ", Questions[question]['answer'] )
            print("\n")  
            i+=1
            
        print ( "{0} attempted {1} questions correctly out of 10".format(name,correct_ques) )
        print ( "{0}'s score is {1} out of 40".format(name,score) )
        

        if score == 40 :
            print ( "Excellent , Full Marks !" )
        elif (score >= 30) :
            print ("Satisfactory Result ! ")
        elif (score >= 10) :
            print ("Have another practice ! ")    
        elif score <= 10 :
            print ("Poor Performance ! ")
    if (choice==4):
        Title11 = "* THANK YOU FOR TAKING QUIZ *"
        print("*" * len(Title11))
        print(Title11)
        print("*" * len(Title11))
        print()
    if (choice>=5):    
        print("Invalid Choice")
        
    print()
    restart_1=input("Do you want to take Quiz again ( Y/N ) : ")
    print()
            
    if(restart_1.upper()=="Y") : # go back to top
       continue
    print("*********************************") 
    print("*** THANK YOU FOR TAKING QUIZ ***")
    print("*********************************")
    break
