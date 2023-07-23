import turtle as trtl

print("\n + instructions + \n")
print("The program will draw out a unit circle, and for each point the cursor stops on, you will have to identify what the angle is in both radians and degrees.\nTo type a value with pi in it, simply type, for example, '4pi/3'.\nAfter you finish going through the whole unit circle, your score of how many questions you answered correctly will be displayed down below.\n")

theta_r = ["0", "pi/6", "pi/4", "pi/3", "pi/2", "2pi/3", "3pi/4", "5pi/6", "pi", "7pi/6", "5pi/4", "4pi/3", "3pi/2", "5pi/3", "7pi/4", "11pi/6", "2pi", " "]
theta_d = ["0", "30", "45", "60", "90", "120", "135", "150", "180", "210", "225", "240", "270", "300", "315", "330", "360", " "]

trtl.right(90)
trtl.penup()
trtl.forward(200)
trtl.pendown()
trtl.left(90)
trtl.circle(200)
trtl.penup()
trtl.home()
trtl.pendown()
trtl.fillcolor("red")

score = 0

def questions():
    global first
    global second
    first = input("What angle is this in radians? ")
    second = input("What angle is this in degrees? ")
def thirty_d():
    trtl.backward(200)
    trtl.left(30)
    trtl.forward(200)
def fifteen_d():
    trtl.backward(200)
    trtl.left(15)
    trtl.forward(200)

trtl.forward(200)
questions()
if first == theta_r[0]:
    score += 1
if second == theta_d[0]:
    score += 1

#first quadrant
thirty_d()
questions()
if first == theta_r[1]:
    score += 1
if second == theta_d[1]:
    score += 1
fifteen_d()
questions()
if first == theta_r[2]:
    score += 1
if second == theta_d[2]:
    score += 1
fifteen_d()
questions()
if first == theta_r[3]:
    score += 1
if second == theta_d[3]:
    score += 1
thirty_d()
questions()
if first == theta_r[4]:
    score += 1
if second == theta_d[4]:
    score += 1

#second quadrant
thirty_d()
questions()
if first == theta_r[5]:
    score += 1
if second == theta_d[5]:
    score += 1
fifteen_d()
questions()
if first == theta_r[6]:
    score += 1
if second == theta_d[6]:
    score += 1
fifteen_d()
questions()
if first == theta_r[7]:
    score += 1
if second == theta_d[7]:
    score += 1
thirty_d()
questions()
if first == theta_r[8]:
    score += 1
if second == theta_d[8]:
    score += 1

#third quadrant
thirty_d()
questions()
if first == theta_r[9]:
    score += 1
if second == theta_d[9]:
    score += 1
fifteen_d()
questions()
if first == theta_r[10]:
    score += 1
if second == theta_d[10]:
    score += 1
fifteen_d()
questions()
if first == theta_r[11]:
    score += 1
if second == theta_d[11]:
    score += 1
thirty_d()
questions()
if first == theta_r[12]:
    score += 1
if second == theta_d[12]:
    score += 1

#fourth quadrant
thirty_d()
questions()
if first == theta_r[13]:
    score += 1
if second == theta_d[13]:
    score += 1
fifteen_d()
questions()
if first == theta_r[14]:
    score += 1
if second == theta_d[14]:
    score += 1
fifteen_d()
questions()
if first == theta_r[15]:
    score += 1
if second == theta_d[15]:
    score += 1
thirty_d()
questions()
if first == theta_r[16]:
    score += 1
if second == theta_d[16]:
    score += 1

print(". - Your score was: " + str(score) + "/34 - .")

leave = input("\n = To return to homescreen, type 'return' and press enter =\n")
if leave == "return":
    import homescreen

trtl.mainloop()