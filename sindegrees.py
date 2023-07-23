import random as rand

print("\n+ instructions +\n")
print("In this excersise, you will have to answer 10 questions of what the value of the sine of an angle is.\nThe angles are displayed in degrees. They are given randomly.\nTo enter a value containing a square root, simply type, for example, 'sqrt(2)/2'.\nAt the end, your score out of 10 will be displayed.\n")

values = ["0", "sqrt(3)/2", "sqrt(2)/2", "1/2", "1"]
negative_values = ["-sqrt(3)/2", "-sqrt(2)/2", "-1/2", "-1"]
theta_d = ["0", "30", "45", "60", "90", "120", "135", "150", "180", "210", "225", "240", "270", "300", "315", "330", "360"]

score = 0

for i in range(10):
    rand_r = rand.choice(theta_d)
    answer = input("What is the sine of " + str(rand_r) + " ")
    # 0 & 360 & 180
    if rand_r == theta_d[0] or rand_r == theta_d[16] or rand_r == theta_d[8]:
        if answer == values[0]:
            score += 1
    # 30 & 150
    if rand_r == theta_d[1] or rand_r == theta_d[7]:
        if answer == values[3]:
            score += 1
    # 45 & 135
    if rand_r == theta_d[2] or rand_r == theta_d[6]:
        if answer == values[2]:
            score += 1
    # 60 & 120
    if rand_r == theta_d[3] or rand_r == theta_d[5]:
        if answer == values[1]:
            score += 1
    # 90
    if rand_r == theta_d[4]:
        if answer == values[4]:
            score += 1
    
    # 210 & 330
    if rand_r == theta_d[9] or rand_r == theta_d[15]:
        if answer == negative_values[2]:
            score += 1
    # 225 & 315
    if rand_r == theta_d[10] or rand_r == theta_d[14]:
        if answer == negative_values[1]:
            score += 1
    # 240 & 300
    if rand_r == theta_d[11] or rand_r == theta_d[13]:
        if answer == negative_values[0]:
            score += 1

    # 270
    if rand_r == theta_d[12]:
        if answer == negative_values[3]:
            score += 1

print("~ Congratulations! Your score was: " + str(score) + "/10 ~")

leave = input("\n = To return to homescreen, type 'return' and press enter =\n")
if leave == "return":
    import homescreen