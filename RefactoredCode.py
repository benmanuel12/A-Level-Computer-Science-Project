from tkinter import *
from random import *
from time import sleep
import glob
from tkinter import filedialog

# current_save_file is [level_Name, healthy, infected,
# sev_infected, dead, immune, reputation, availible_cures, virus_level,
# virus_speed, virus_infect]

global default_save_file
default_save_file = ['Default Save File',
                     ['Tutorial-Cold',50,50,0,0,0,100,30,1,1,1],
                     ['Flu',100,50,40,0,10,100,120,1,2,2],
                     ['Something Deadly',100,200,100,50,50,100,100,3,2,1],
                     ['Overlapping DNA',200,400,250,0,0,100,300,3,2,3],
                     ['Doomsday Virus',0,300,500,150,50,100,200,3,3,3]]

global current_save_file
current_save_file = ['',
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
global level_num
level_num = 1

global active_file_name
active_file_name = ''

# Render the Gameplay window (also referred to as the Game Window or Main Window)
def render_gameplay(virus):
    global Gameplay
    Gameplay = Toplevel()
    Gameplay.title('Game Window')
    global level_name, healthy, infected, sev_infected, dead, immune, reputation, availible_cures, news_feed_content, virus_level, virus_speed, virus_infect

    level_name = StringVar()
    healthy = IntVar()
    infected = IntVar()
    sev_infected = IntVar()
    dead = IntVar()
    immune = IntVar()
    availible_cures = IntVar()
    reputation = IntVar()
    news_feed_content = StringVar()
    virus_level = IntVar()
    virus_speed = IntVar()
    virus_infect = IntVar()
    
    level_name.set(current_save_file[level_num][0])
    healthy.set(current_save_file[level_num][1])
    infected.set(current_save_file[level_num][2])
    sev_infected.set(current_save_file[level_num][3])
    dead.set(current_save_file[level_num][4])
    immune.set(current_save_file[level_num][5])
    reputation.set(current_save_file[level_num][6])
    availible_cures.set(current_save_file[level_num][7])
    news_feed_content.set('Welcome to the Game')
    virus_level.set(current_save_file[level_num][8])
    virus_speed.set(current_save_file[level_num][9])
    virus_infect.set(current_save_file[level_num][10])

    # Creates title and images
    Level_Name_Label = Label(Gameplay, textvariable=level_name, font=("Arial bold", 16))
    Virus_Marker = Label(Gameplay, image=virus)

    # Creates Information panel
    Counter_Frame = Frame(Gameplay, height=2, bd=1, relief="sunken")
    Healthy_Label = Label(Counter_Frame, text='Healthy', font=("Arial", 16))
    Infected_Label = Label(Counter_Frame, text='Infected', font=("Arial", 16))
    Dead_Label = Label(Counter_Frame, text='Dead', font=("Arial", 16))
    Healthy_Counter = Label(Counter_Frame, textvariable=healthy, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Infected_Counter = Label(Counter_Frame, textvariable=infected, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Dead_Counter = Label(Counter_Frame, textvariable=dead, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Immune_Label = Label(Counter_Frame, text='Immune', font=("Arial", 16))
    Immune_Counter = Label(Counter_Frame, textvariable=immune, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Infected2_Label = Label(Counter_Frame, text='Severely Infected', font=("Arial", 16))
    Infected2_Counter = Label(Counter_Frame, textvariable=sev_infected, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))

    # Creates Information strip
    Other_Frame = Frame(Gameplay, height=2, bd=1, relief="sunken")
    Reputation_Label = Label(Other_Frame, text='Reputation', font=("Arial", 16))
    Reputation_Counter = Label(Other_Frame, textvariable=reputation, borderwidth=2, bg='white', font=("Arial", 16))
    Cure_Number_Label = Label(Other_Frame, text='Mega Cures', font=("Arial", 16))
    Cure_Number_Counter = Label(Other_Frame, textvariable=availible_cures, borderwidth=2, bg='white', font=("Arial", 16))
    Extra_Label = Label(Other_Frame, text='', font=("Arial", 16))
    Load_Button = Button(Other_Frame, text='Load', font=("Droid Sans Mono", 16), command=lambda: load_level(level_name.get()))
    Score_Button = Button(Other_Frame, text='High Scores', font=("Droid Sans Mono", 16), command=lambda: render_scores())

    # Creates News Feed
    News_Feed = Label(Gameplay, textvariable=news_feed_content, font=("Courier New", 16), width=60, height = 2)

    # Creates Button rack
    Button_Frame = Frame(Gameplay, height=5, bd=1, bg='SteelBlue3', relief="raised")
    Cure_Button = Button(Button_Frame, text='Cure', font=("Droid Sans Mono", 16), height=3, width=10, command=Cure_Button_Combined)
    Cure2_Button = Button(Button_Frame, text='Mega Cure', font=("Droid Sans Mono", 16), height=3, width=10, command=Mega_Cure_Button_Combined)
    Kill_Button = Button(Button_Frame, text='Kill', font=("Droid Sans Mono", 16), height=3, width=10, command=Kill_Button_Combined)
    Leave_Button = Button(Button_Frame, text='Leave', font=("Droid Sans Mono", 16), height=3, width=10, command=Leave_Button_Combined)

    # Grids Title and image
    Level_Name_Label.grid(row=0, column=0, columnspan=8, padx=10, pady=10)
    Virus_Marker.grid(row=1, column=4, columnspan=4, rowspan=2, padx=5)

    # Grids Information panel
    Counter_Frame.grid(row=1, column=0, rowspan=3, columnspan=4, padx=10)
    Healthy_Label.grid(row=0, column=0, padx=10, pady=10)
    Healthy_Counter.grid(row=0, column=1, padx=10, pady=10)
    Infected_Label.grid(row=0, column=2, padx=10, pady=10)
    Infected_Counter.grid(row=0, column=3, padx=10, pady=10)
    Dead_Label.grid(row=1, column=0, padx=10, pady=10)
    Dead_Counter.grid(row=1, column=1, padx=10, pady=10)
    Immune_Label.grid(row=1, column=2, padx=10, pady=10)
    Immune_Counter.grid(row=1, column=3, padx=10, pady=10)
    Infected2_Label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
    Infected2_Counter.grid(row=2, column=2, padx=10, pady=10, columnspan=2)

    # Grids Information strip
    Other_Frame.grid(row=3, column=0, columnspan=8, padx=10, pady=10, sticky='EW')
    Reputation_Label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    Reputation_Counter.grid(row=0, column=2, columnspan=1, padx=10, pady=10)
    Cure_Number_Label.grid(row=0, column=4, columnspan=1, padx=10, pady=10)
    Cure_Number_Counter.grid(row=0, column=5, columnspan=1, padx=10, pady=10)
    Extra_Label.grid(row=0, column=6, padx=10, pady=10)
    Load_Button.grid(row=0, column=7, padx=10, pady=10)
    Score_Button.grid(row=0, column=8, padx=10, pady=10)

    # Grids News Feed
    News_Feed.grid(row=4, column=0, columnspan=8, padx=10, pady=10)

    # Grids Button rack
    Button_Frame.grid(row=5, column=0, columnspan=8, padx=10, pady=10)
    Cure_Button.grid(row=0, column=0, padx=10, pady=10)
    Cure2_Button.grid(row=0, column=1, padx=10, pady=10)
    Kill_Button.grid(row=0, column=2, padx=10, pady=10)
    Leave_Button.grid(row=0, column=3, padx=10, pady=10)

    # Mainloop
    Gameplay.mainloop()

# Main Login Procedure
def login_submit(new_username):

    # Extract username from screen and convert to file name
    global current_save_file
    
    # Validate username and reject incorrect ones
    if len(new_username)<= 15:
        file_name = new_username + '.txt'
        global active_file_name
        # Try to open an existing save file of the name given
        try:
            f = open(file_name, 'r') #check for file existance
            f.close()
            file_to_list(file_name)
            active_file_name = file_name
        
        # If no file exists, creates such a file
        except FileNotFoundError:
            current_save_file = default_save_file
            current_save_file[0] = new_username
            active_file_name = file_name
            list_to_file()
            
            
        render_levelselect()
    else:
        # Error Message
        print('Your username is too long at ' + str(len(new_username)) + ' chars.')

def render_login():
    def get_username(event):
        new_username = Username_Entry.get()
        login_submit(new_username)

    Login = Tk()
    Login.title('Login')

    Title = Label(Login, text='Login', font=('Arial', 16, 'bold'))
    Exp = Label(Login, text='Enter your username in the box and submit.\n'
                'If this username is new, a new save file will be created upon submission\n'
                'If the username matches a already existing save file,\n'
                ' that save file will be loaded upon submission\n'
                '15 characters limit, Case-Sensitive.'
                , font=('Arial', 12), padx=30, pady=30)

    Username_Entry = Entry(Login, width=15, font=("default", 12))
    Submit_Button = Button(Login, text='Submit', font=('Arial', 12), command=lambda:login_submit(Username_Entry.get()))
    Username_Entry.bind('<Return>', get_username)

    Title.grid(column=0, row=0)
    Exp.grid(column=0, row=1)
    Username_Entry.grid(column=0, row=2)
    Submit_Button.grid(column=0, row=3, pady=10)
    mainloop()

def render_levelselect():
    LevelSelect = Tk()
    LevelSelect.title('Level Select')

    Title = Label(LevelSelect, text='Level Selection', font=('Arial', 16, 'bold'))
    Subtitle = Label(LevelSelect, text='Select a Level:', font=('Arial', 12))
    Level1_Button = Button(LevelSelect, text='Level 1 - Tutorial', font=('Arial', 16, 'bold'), height=2, width=25, command=load_Level_1)
    Level2_Button = Button(LevelSelect, text='Level 2 - Flu', font=('Arial', 16, 'bold'), height=2, width=25, command=load_Level_2)
    Level3_Button = Button(LevelSelect, text='Level 3 - Something Deadly', font=('Arial', 16, 'bold'), height=2, width=25, command=load_Level_3)
    Level4_Button = Button(LevelSelect, text='Level 4 - Overlapping DNA', font=('Arial', 16, 'bold'), height=2, width=25, command=load_Level_4)
    Level5_Button = Button(LevelSelect, text='Level 5 - Doomsday Virus', font=('Arial', 16, 'bold'), height=2, width=25, command=load_Level_5)

    Title.grid(column=0, row=1, columnspan=2)
    Subtitle.grid(column=0, row=2, columnspan=2)
    Level1_Button.grid(column=0, row=3, columnspan=2, padx=30, pady=30)
    Level2_Button.grid(column=0, row=4, padx=30, pady=30)
    Level3_Button.grid(column=1, row=4, padx=30, pady=30)
    Level4_Button.grid(column=0, row=5, padx=30, pady=30)
    Level5_Button.grid(column=1, row=5, padx=30, pady=30)

    mainloop()
    
def render_scores():
    name_list = []
    for filename in glob.glob('*.txt'):
        f = open(filename, 'r')
        new_line = f.readline()
        name_list.append(new_line)
        f.close()
    score_string = ''
    for i in name_list:
        score_string = score_string + i + '\n'
    
    HighScores = Tk()
    HighScores.title('High Scores')
    Title = Label(HighScores, text='High Scores', font=('Arial', 16, 'bold'))
    Score_Box = Message(HighScores, text=score_string, borderwidth=2, bg='white', font=("Arial", 12),width=500)

    Title.grid(column=0, row=1)
    Score_Box.grid(column=0, row=3, padx=20, pady=20)
    
    mainloop()

def list_to_file():
    global current_save_file
    f = open(active_file_name, 'w')
    f.write(str(current_save_file[0] + '\n'))
    
    for i in range(1,6):
        line_write = current_save_file[i][0] + ',' +\
        str(current_save_file[i][1]) + ',' +\
        str(current_save_file[i][2]) + ',' +\
        str(current_save_file[i][3]) + ',' +\
        str(current_save_file[i][4]) + ',' +\
        str(current_save_file[i][5]) + ',' +\
        str(current_save_file[i][6]) + ',' +\
        str(current_save_file[i][7]) + ',' +\
        str(current_save_file[i][8]) + ',' +\
        str(current_save_file[i][9]) + ',' +\
        str(current_save_file[i][10]) + '\n'
        f.write(line_write)
    f.close()

def file_to_list(file_name):
    f = open(file_name, 'r')
    global current_save_file
    current_save_file[0] = f.readline()
    current_save_file[0]= current_save_file[0][:len(current_save_file[0])-1] #get rid of newline character at end (\n)
    for i in range(1, 6):
        data = f.readline()
        data = data.split(',')
        current_save_file[i][0] = data[0]
        current_save_file[i][1] = int(data[1])
        current_save_file[i][2] = int(data[2])
        current_save_file[i][3] = int(data[3])
        current_save_file[i][4] = int(data[4])
        current_save_file[i][5] = int(data[5])
        current_save_file[i][6] = int(data[6])
        current_save_file[i][7] = int(data[7])
        current_save_file[i][8] = int(data[8])
        current_save_file[i][9] = int(data[9])
        current_save_file[i][10] = int(data[10])
    f.close()

def load_single_level_data(file_name, level_name):
    f = open(file_name, 'r')
    for i in range(0, 6):
        line = f.readline()
        line_split = line.split(',')
        if line_split[0] == level_name:
            healthy.set(int(line_split[1]))
            infected.set(int(line_split[2]))
            sev_infected.set(int(line_split[3]))
            dead.set(int(line_split[4]))
            immune.set(int(line_split[5]))
            reputation.set(int(line_split[6]))
            availible_cures.set(int(line_split[7]))
            virus_level.set(int(line_split[8]))
            virus_speed.set(int(line_split[9]))
            virus_infect.set(int(line_split[10]))
    f.close()

# Check for a win or loss
def Check_Win_Loss():
    global Gameplay
    if infected.get() == 0 and sev_infected.get() == 0 and reputation.get() >= 50 and healthy.get() > dead.get():
        Gameplay.destroy()
        render_game_end_window('You have won the game')
        return True
    elif healthy.get() == 0 and immune.get() == 0:
        Gameplay.destroy()
        render_game_end_window('You have lost the game')
        return True
    else:
        return False

# Save Level
def save_level():
    print('Saving...')
    current_save_file[level_num][1]=str(healthy.get())
    current_save_file[level_num][2]=str(infected.get())
    current_save_file[level_num][3]=str(sev_infected.get())
    current_save_file[level_num][4]=str(dead.get())
    current_save_file[level_num][5]=str(immune.get())
    current_save_file[level_num][6]=str(reputation.get())
    current_save_file[level_num][7]=str(availible_cures.get())
    current_save_file[level_num][8]=str(virus_level.get())
    current_save_file[level_num][9]=str(virus_speed.get())
    current_save_file[level_num][10]=str(virus_infect.get())
    list_to_file()
    print('Done')

# Load Level
def load_level(level_name):
    print('Loading...')
    file_name = filedialog.askopenfilename()
    load_single_level_data(file_name, level_name)

# Load_Level1
def load_Level_1():
    global level_num
    level_num = 1
    render_gameplay(L1_image) 

# Load_Level2
def load_Level_2():
    global level_num
    level_num = 2
    render_gameplay(L2_image)

# Load_Level3
def load_Level_3():
    global level_num
    level_num = 3
    print('Load_Level3, level_num is ' + str(level_num))
    render_gameplay(L3_image)

# Load_Level4
def load_Level_4():
    global level_num
    level_num = 4
    render_gameplay(L4_image)
    
# Load_Level5
def load_Level_5():
    global level_num
    level_num = 5
    render_gameplay(L5_image)

#--------------General Action Functions------------------------------

# Infected Dies (-1 infected, +1 dead)
def infectedDies(cause):
    infected.set(infected.get()-1)
    dead.set(dead.get()+1)
    news_feed_content.set("You let an infected person die") if cause == "player" else news_feed_content.set("The virus killed an infected person")

# Seriously Infected Dies (-1 infected2, +1 dead)
def infected2Dies(cause):
    sev_infected.set(sev_infected.get()-1)
    dead.set(dead.get()+1)
    news_feed_content.set("You let a seriously infected person die") if cause == "player" else news_feed_content.set("The virus killed a seriously infected person")

# Healthy Dies (-1 healthy, +1 dead)
def healthyDies(cause):
    healthy.set(healthy.get()-1)
    dead.set(dead.get()+1)
    news_feed_content.set("You let an healthy person die") if cause == "player" else news_feed_content.set("The virus killed a healthy person")

# Healthy Infected (-1 healthy, +1 infected)
def healthyInfected(cause):
    healthy.set(healthy.get()-1)
    infected.set(infected.get()+1)
    news_feed_content.set("You let a healthy person get infected") if cause == "player" else news_feed_content.set("The virus infected a healthy person")

# Healthy Seriously Infected (-1 healthy, +1 infected2)
def healthySeriouslyInfected(cause):
    healthy.set(healthy.get()-1)
    sev_infected.set(sev_infected.get()+1)
    news_feed_content.set("You let a healthy person get seriously infected") if cause == "player" else news_feed_content.set("The virus seriously infected a healthy person")
    
# Infection Worsens (-1 infected, +1 infected2)
def InfectionWorsens(cause):
    infected.set(infected.get()-1)
    sev_infected.set(sev_infected.get()+1)
    news_feed_content.set("You let an infected person's infection get worse") if cause == "player" else news_feed_content.set("An infected person's infection got worse")

# Infected Cured (-1 infected, +1 healthy)
def infectedCured(cause):
    infected.set(infected.get()-1)
    healthy.set(healthy.get()+1)
    news_feed_content.set("You cured an infected person") if cause == "player" else news_feed_content.set("An infected person got better")

# Seriously Infected Cured (-1 infected2, +1 healthy)
def infected2Cured(cause):
    sev_infected.set(sev_infected.get()-1)
    healthy.set(healthy.get()+1)
    news_feed_content.set("You cured a seriously infected person") if cause == "player" else news_feed_content.set("A seriously infected person got better")

# Gain Immunity (-1 healthy, +1 immune)
def gainImmunity(cause):
    healthy.set(healthy.get()-1)
    immune.set(immune.get()+1)
    availible_cures.set(availible_cures.get()+1)
    news_feed_content.set("You gave a healthy person the vaccine") if cause == "player" else news_feed_content.set("A healthy person gained immunity")

# No Action
def noAction(cause):
    start = "You " if cause == "player" else "The virus "
    news_feed_content.set(start + "took no action this turn")

#--------------------------------------------------------------------

#--------------Virus Functions---------------------------------------

# Virus_Turn_Master
def Virus_Turn_Master():
    # Gives virus a number of actions per turn equal to its speed stat. Actions can fail
    for i in range(virus_speed.get()):
        print('----------Starting Virus Turn----------')
        Virus_Turn()
        sleep(1)
        print('----------Ending Virus Turn----------')
        print('')

# Virus Turn
def Virus_Turn():  
    # Randomiser
    turn_action = randint(1, 10)

    # Different if statement for each combination of levels. The lower the number the weaker the stat. Level 1 gets 1/5 chance of something happening,
    # Level 2 get 3/10 chance, and Level 3 has a 2/5 chance. This seems small, but since both Level and Infect check the same randomiser,
    # a 3/3 virus has a 4/5 chance of doing an action per action chance and 3 action chances per turn
    
    # #---------- Level: 1-----Infectiousness: 1----------
    if virus_level.get() == 1 and virus_infect.get() == 1:
        if turn_action == 1 or turn_action == 2:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6:
            virus_Infecting()
        else:
            noAction("virus")

    # #---------- Level: 1-----Infectiousness: 2----------
    elif virus_level.get() == 1 and virus_infect.get() == 2:
        if turn_action == 1 or turn_action == 2:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6 or turn_action == 7:
            virus_Infecting()
        else:
            noAction("virus")

    # #---------- Level: 1-----Infectiousness: 3----------
    elif virus_level.get() == 1 and virus_infect.get() == 3:
        if turn_action == 1 or turn_action == 2:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6 or turn_action == 7 or turn_action == 8:
            virus_Infecting()
        else:
            noAction("virus")

    # #---------- Level: 2-----Infectiousness: 1----------
    elif virus_level.get() == 2 and virus_infect.get() == 1:
        if turn_action == 1 or turn_action == 2 or turn_action == 3:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6:
            virus_Infecting()
        else:
            noAction("virus") 

    # #---------- Level: 2-----Infectiousness: 2----------
    elif virus_level.get() == 2 and virus_infect.get() == 2:
        if turn_action == 1 or turn_action == 2 or turn_action == 3:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6 or turn_action == 7:
            virus_Infecting()
        else:
            noAction("virus")

    # #---------- Level: 2-----Infectiousness: 3----------
    elif virus_level.get() == 2 and virus_infect.get() == 3:
        if turn_action == 1 or turn_action == 2 or turn_action == 3:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6 or turn_action == 7 or turn_action == 8:
            virus_Infecting()
        else:
            noAction("virus")

    # #---------- Level: 3-----Infectiousness: 1----------
    elif virus_level.get() == 3 and virus_infect.get() == 1:
        if turn_action == 1 or turn_action == 2 or turn_action == 3 or turn_action == 4:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6:
            virus_Infecting()
        else:
            noAction("virus")

    # #---------- Level: 3-----Infectiousness: 2----------
    elif virus_level.get() == 3 and virus_infect.get() == 2:
        if turn_action == 1 or turn_action == 2 or turn_action == 3 or turn_action == 4:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6 or turn_action == 7:
            virus_Infecting()
        else:
            noAction("virus")

    # #---------- Level: 3-----Infectiousness: 3----------
    elif virus_level.get() == 3 and virus_infect.get() == 3:
        if turn_action == 1 or turn_action == 2 or turn_action == 3 or turn_action == 4:
            virus_Killing()
        elif turn_action == 5 or turn_action == 6 or turn_action == 7 or turn_action == 8:
            virus_Infecting()
        else:
            noAction("virus")
    else:
        print("Warning - Virus Level and/or Virus Infectiousness outside of expected parameters")
        print(virus_level.get())
        print(virus_infect.get())

    print(news_feed_content.get())

def virus_Killing():
    action = randint(1, 4)
    if action == 1 or action == 2:
        if sev_infected > 0:
            infected2Dies("virus")
        elif infected.get() > 0:
            infectedDies("virus")
        else:
            noAction("virus")
    elif action == 3:
        infectedDies("virus") if infected.get() > 0 else noAction("virus")
    elif action == 4:
        healthyDies("virus") if healthy.get() > 0 else noAction("virus")

def virus_Infecting():
    action = randint(1,2)
    if action == 1:
        healthyInfected("virus") if healthy.get() > 0 else noAction("virus")
    elif action == 2:
        healthySeriouslyInfected("virus") if healthy.get() > 0 else noAction("virus")
#--------------------------------------------------------------------

#--------------Player Functions--------------------------------------

#  has 1/3 chance of curing a severely ill person and a 2/3 chance of curing an ill person      
def cure_Proc():       
    # print('cure_Proc, level_num is ' + str(level_num))
##    if current_save_file[level_num][14] == False:
##        pass
##    else:
       
    player_action = randint(1,3)
    if player_action == 1:
        if sev_infected.get() > 0:
            infected2Cured("player")
            reputation.set(reputation.get()+1)
        elif infected.get() > 0:
            infectedCured("player")
            reputation.set(reputation.get()+1)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    elif infected.get() > 0:
        infectedCured("player")
        reputation.set(reputation.get()+1)
    else:
        news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    print(news_feed_content.get())

# stronger cure – has ½ chance of either healing a severely or regularly ill person, either way makes them immune to being reinfected
def cure2_Proc():
    if availible_cures.get()>0:
        
        player_action = randint(1,2)
        if player_action == 1:
            if sev_infected.get()>0:
                reputation.set(reputation.get()+2)
                infected2Cured("player")
                gainImmunity("player")
            elif infected.get()>0:
                reputation.set(reputation.get()+2)
                infectedCured("player")
                gainImmunity("player")
            else:
                news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
        elif infected.get()>0:
            reputation.set(reputation.get()+2)
            infectedCured("player")
            gainImmunity("player")
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    else:
        news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    print(news_feed_content.get())
        
# has an equal chance of killing an infected or severely infected person
def kill_Proc():        
##    if current_save_file[level_num][14] == False:
##        pass
##    else:
        
    player_action = randint(1,2)
    if player_action == 1:
        if sev_infected.get()>0:
            infected2Dies("player")
            reputation.set(reputation.get()-2)
        elif infected.get()>0:
            infectedDies("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    else:
        if infected.get() > 0:
            infectedDies("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    print(news_feed_content.get())

# has a 1/9 chance of doing anyone of the 9 possible actions
def leave_Proc():
    player_action = randint(1,9)
    if player_action == 1:
        if healthy.get() > 0:
            healthyDies("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 2:
        if healthy.get() > 0:
            healthyInfected("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 3:
        if healthy.get() > 0:
            healthySeriouslyInfected("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
            
    elif player_action == 4:
        if infected.get() > 0:
            infectedDies("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 5:
        if sev_infected.get() > 0:
            infected2Dies("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 6:
        if infected.get() > 0:
            InfectionWorsens("player")
            reputation.set(reputation.get()-2)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 7:
        if infected.get() > 0:
            infectedCured("player")
            reputation.set(reputation.get()+1)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 8:
        if sev_infected.get() > 0:
            infected2Cured("player")
            reputation.set(reputation.get()+1)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 9:
        if healthy.get() > 0:
            gainImmunity("player")
            reputation.set(reputation.get()+1)
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    print(news_feed_content.get())

#--------------------------------------------------------------------

#--------------Action Button Combined Functions----------------------

def Generic_Button(button_action):
    print('----------Starting Player Turn----------')
    button_action()
    print('----------Ending Player Turn----------')
    print('')
    save_level()
    if not Check_Win_Loss():
        Virus_Turn_Master()
        save_level()
        Check_Win_Loss()    

def Cure_Button_Combined():
    Generic_Button(cure_Proc)
    
def Mega_Cure_Button_Combined():
    Generic_Button(cure2_Proc)
    
def Kill_Button_Combined():
    Generic_Button(kill_Proc)
    
def Leave_Button_Combined():
    Generic_Button(leave_Proc)

def render_game_end_window(window_message):
    Game_End_Window = Tk()
    Game_End_Window.title('Game Over')

    Message = Label(Game_End_Window, text=window_message, font=('Arial', 16, 'bold'))
    Message.grid(column=0, row=0)
    mainloop()

#--------------------------------------------------------------------

# Render Launcher window
root = Tk()
root.title('Launcher')
root.minsize(width=250, height=75)
global L1_image
global L2_image
global L3_image
global L4_image
global L5_image
L1_image = PhotoImage(file='L1 image.png')
L2_image = PhotoImage(file='L2 image.png')
L3_image = PhotoImage(file='L3 image.png')
L4_image = PhotoImage(file='L4 image.png')
L5_image = PhotoImage(file='L5 image.png')

Heading = Label(root, text='Launcher', font = ('Arial', 16, 'bold'))
Login_Button=Button(root, text='Login', command=render_login, font = ('Arial', 12))
Heading.pack()
Login_Button.pack()