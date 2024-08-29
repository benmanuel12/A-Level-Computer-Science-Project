
'''
keybind enter
enlarge entry widget
Make use of or remove the is_Player_go or done_Turn_action Booleans
'''

# Computer Science Project Development Code

from tkinter import *
from random import *
from time import sleep
import glob, os
import winsound

Won_Game = False
Lost_Game = False
# current_save_file is basically [level_Name, healthy_People, infected_People,
# infected2_People, dead_People, immune_People, cure_Number, Reputation_number, virus_Image,
# , virus_Speed, virus_Infect, Game_Won, Game_Lost, is_Player_go,
# done_Turn_action]but data not variable names will be in it.

global default_save_file
default_save_file = ['Default Save File',
                     ['Tutorial-Cold',50,50,0,0,0,30,100,1,1,1,False,False,False,False],
                     ['Flu',100,50,40,0,10,120,100,1,2,2,False,False,False,False],
                     ['Something Deadly',100,200,100,50,50,100,100,3,2,1,False,False,False,False],
                     ['Overlapping DNA',200,400,250,0,0,300,100,3,2,3,False,False,False,False],
                     ['Doomsday Virus',0,300,500,150,50,200,100,3,3,3,False,False,False,False]]


global current_save_file
current_save_file = ['',
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False],
                     ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False]]
global level_num
level_num = 1

global file_name
file_name = ''

global Gameplay

# Render the Gameplay window (also referred to as the Game Window or Main Window)
def render_gameplay(virus):
    global Gameplay
    # print('rendering gameplay, level_num is ' + str(level_num))
    Gameplay = Toplevel()
    Gameplay.title('Game Window')  # replace with actual game name

    global level_name_content, healthy_num, infected_num, infected2_num, dead_num, immune_num, reputation_num, cure_number_num, news_feed_content, virus_level_num, virus_speed_num, virus_infect_num

    save_level_interrupt = False

    level_name_content = StringVar()
    healthy_num = IntVar()
    infected_num = IntVar()
    infected2_num = IntVar()
    dead_num = IntVar()
    immune_num = IntVar()
    reputation_num = IntVar()
    cure_number_num = IntVar()
    news_feed_content = StringVar()
    virus_level_num = IntVar()
    virus_speed_num = IntVar()
    virus_infect_num = IntVar()
    
    level_name_content.set(current_save_file[level_num][0])
    healthy_num.set(current_save_file[level_num][1])
    infected_num.set(current_save_file[level_num][2])
    infected2_num.set(current_save_file[level_num][3])
    dead_num.set(current_save_file[level_num][4])
    immune_num.set(current_save_file[level_num][5])
    reputation_num.set(current_save_file[level_num][7])
    cure_number_num.set(current_save_file[level_num][6])
    news_feed_content.set('Welcome to the Game')
    virus_level_num.set(current_save_file[level_num][8])
    virus_speed_num.set(current_save_file[level_num][9])
    virus_infect_num.set(current_save_file[level_num][10])

    # Creates title and images
    Level_Name = Label(Gameplay, textvariable=level_name_content, font=("Arial bold", 16))
    Virus_Marker = Label(Gameplay, image=virus)

    # Creates Information panel
    Counter_Frame = Frame(Gameplay, height=2, bd=1, relief="sunken")
    Healthy_Label = Label(Counter_Frame, text='Healthy', font=("Arial", 16))
    Infected_Label = Label(Counter_Frame, text='Infected', font=("Arial", 16))
    Dead_Label = Label(Counter_Frame, text='Dead', font=("Arial", 16))
    Healthy_Counter = Label(Counter_Frame, textvariable=healthy_num, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Infected_Counter = Label(Counter_Frame, textvariable=infected_num, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Dead_Counter = Label(Counter_Frame, textvariable=dead_num, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Immune_Label = Label(Counter_Frame, text='Immune', font=("Arial", 16))
    Immune_Counter = Label(Counter_Frame, textvariable=immune_num, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))
    Infected2_Label = Label(Counter_Frame, text='Severely Infected', font=("Arial", 16))
    Infected2_Counter = Label(Counter_Frame, textvariable=infected2_num, borderwidth=2, bg='white', font=("Droid Sans Mono", 16))

    # Creates Information strip
    Other_Frame = Frame(Gameplay, height=2, bd=1, relief="sunken")
    Reputation_Label = Label(Other_Frame, text='Reputation', font=("Arial", 16))
    Reputation_Counter = Label(Other_Frame, textvariable=reputation_num, borderwidth=2, bg='white', font=("Arial", 16))
    Cure_Number_Label = Label(Other_Frame, text='Mega Cures', font=("Arial", 16))
    Cure_Number_Counter = Label(Other_Frame, textvariable=cure_number_num, borderwidth=2, bg='white', font=("Arial", 16))
    Extra_Label = Label(Other_Frame, text='', font=("Arial", 16))
    Save_Button = Button(Other_Frame, text='Save', font=("Droid Sans Mono", 16), command=lambda: save_level_interrupt_trigger(save_level_interrupt))
    Load_Button = Button(Other_Frame, text='Load', font=("Droid Sans Mono", 16))
    Score_Button = Button(Other_Frame, text='High Scores', font=("Droid Sans Mono", 16), command=lambda: render_scores())

    # Creates News Feed
    News_Feed = Label(Gameplay, textvariable=news_feed_content, font=("Courier New", 16), width=60, height = 2)

    # Creates Button rack
    Button_Frame = Frame(Gameplay, height=5, bd=1, bg='SteelBlue3', relief="raised")
    Cure_Button = Button(Button_Frame, text='Cure', font=("Droid Sans Mono", 16), height=3, width=10, command=Cure_Button_Combined)
    Cure2_Button = Button(Button_Frame, text='Mega Cure', font=("Droid Sans Mono", 16), height=3, width=10, command=Mega_Cure_Button_Combined)
    Kill_Button = Button(Button_Frame, text='Kill', font=("Droid Sans Mono", 16), height=3, width=10, command=Kill_Button_Combined)
    Leave_Button = Button(Button_Frame, text='Leave', font=("Droid Sans Mono", 16), height=3, width=10, command=Leave_Button_Combined)

    Virus_Button = Button(Gameplay, text='Virus Turn', bg='Red',height=3, width=80, command=Virus_Turn_Master)

    # Grids Title and image
    Level_Name.grid(row=0, column=0, columnspan=8, padx=10, pady=10)
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
    #Save_Button.grid(row=0, column=7, padx=10, pady=10)
    #Load_Button.grid(row=0, column=8, padx=10, pady=10)
    Score_Button.grid(row=0, column=9, padx=10, pady=10)

    # Grids News Feed
    #News_Feed.grid(row=4, column=0, columnspan=8, padx=10, pady=10)

    # Grids Button rack
    Button_Frame.grid(row=5, column=0, columnspan=8, padx=10, pady=10)
    Cure_Button.grid(row=0, column=0, padx=10, pady=10)
    Cure2_Button.grid(row=0, column=1, padx=10, pady=10)
    Kill_Button.grid(row=0, column=2, padx=10, pady=10)
    Leave_Button.grid(row=0, column=3, padx=10, pady=10)
    #Virus_Button.grid(row=6, column=0, columnspan=8, padx=10, pady=10)

    # Mainloop
    Gameplay.mainloop()


def render_login():
    Login = Tk()
    Login.title('Login')

    Title = Label(Login, text='Login', font=('Arial', 16, 'bold'))
    Exp = Label(Login, text='Enter your username in the box and submit.\n'
                'If this username is new, a new save file will be created upon submission\n'
                'If the username matches a already existing save file,\n'
                ' that save file will be loaded upon submission\n'
                '15 characters limit, Case-Sensitive.'
                , font=('Arial', 12), padx=30, pady=30)

    Username_Entry = Entry(Login, width=15)
    Submit_Button = Button(Login, text='Submit', font=('Arial', 12), command=lambda:login_submit(Username_Entry))
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
        #print(new_line)
        f.close()
    #print(name_list)
    score_string = ''
    for i in name_list:
        score_string = score_string + i + '\n'
        #print(score_string) 
    
    HighScores = Tk()
    HighScores.title('High Scores')
    Title = Label(HighScores, text='High Scores', font=('Arial', 16, 'bold'))
    Exp = Label(HighScores, text='All player save files are listed here currently.\n Code to filter and sort them is too much effort for such a small part of the project.', font=('Arial', 12))
    Score_Box = Message(HighScores, text=score_string, borderwidth=2, bg='white', font=("Arial", 12),width=500)

    Title.grid(column=0, row=1)
    Exp.grid(column=0, row=2, padx=20)
    Score_Box.grid(column=0, row=3, padx=20, pady=20)
    
    mainloop()


def list_to_file():
    global current_save_file
    f = open(file_name, 'w')
    #print('Copying current_save_file to disk')
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
        str(current_save_file[i][10]) + ',' +\
        str(current_save_file[i][11]) + ',' +\
        str(current_save_file[i][12]) + ',' +\
        str(current_save_file[i][13]) + ',' +\
        str(current_save_file[i][14]) + '\n'
        #print(line_write)
        f.write(line_write)
    f.close()

def file_to_list():
    f = open(file_name, 'r')
    #print('Copying disk to current_save_file')
    global current_save_file
    current_save_file[0] = f.readline()
    current_save_file[0]= current_save_file[0][:len(current_save_file[0])-1] #get rid of newline character at end (\n)
    for i in range(1, 6):
        data = f.readline()
        data = data.split(',')
        #print(data)
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
        current_save_file[i][11] = data[11] == 'True'
        current_save_file[i][12] = data[12] == 'True'
        current_save_file[i][13] = data[13] == 'True'
        current_save_file[i][14] = data[14] == 'True'
    f.close()
    #print(current_save_file[0])
    #print(current_save_file[1])
    #print(current_save_file[2])
    #print(current_save_file[3])
    #print(current_save_file[4])
    #print(current_save_file[5])
        
# Main Login Procedure
def login_submit(Username_Entry):

    # Extract username from screen and convert to file name
    new_username = Username_Entry.get()
    global file_name
    global current_save_file
    file_name = new_username + '.txt'
    
    # Validate username and reject incorrect ones
    if len(new_username)<= 15:
        # Try to open an existing save file of the name given
        try:
            f = open(file_name, 'r') #check for file existance
            f.close()
            file_to_list()
        
        # If no file exists, creates such a file
        except IOError:
            current_save_file = default_save_file
            current_save_file[0] = new_username
            #print(current_save_file)
            list_to_file()
            
        render_levelselect()
    else:
        # Error Message
        print('Your username is too long at ' + str(len(new_username)) + ' chars.')



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
    

# Virus_Turn_Master
def Virus_Turn_Master():
    # Gives virus a number of actions per turn equal to its speed stat. Actions can fail
    for i in range(virus_speed_num.get()):
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
    
#---------- Level: 1-----Infectiousness: 1----------
    if virus_level_num.get() == 1 and virus_infect_num.get() == 1: 
        if turn_action == 1 or turn_action == 2: 
            turn_action2 = randint(1,2)
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('An infected person has died')
                else:
                    news_feed_content.set('The virus has taken no action')
                    
        elif turn_action == 3 or turn_action == 4: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                turn_action3 = randint(1, 2) 
                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')

#---------- Level: 1-----Infectiousness: 2----------
    elif virus_level_num.get() == 1 and virus_infect_num.get() == 2:
        if turn_action == 1 or turn_action == 2:
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2: 
                turn_action3 = randint(1, 2) 
                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')


        elif turn_action == 3 or turn_action == 4 or turn_action == 5: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('An infected person has died')
                else:
                    news_feed_content.set('The virus has taken no action')
    
            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')

#---------- Level: 1-----Infectiousness: 3----------
    elif virus_level_num.get() == 1 and virus_infect_num.get() == 3: 
        if turn_action == 1 or turn_action == 2: 
            turn_action2 = randint(1,2) 

            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')
    
            elif turn_action2 == 2: 
                turn_action3 = randint(1, 2) 
                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')
    
                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

     

        elif turn_action == 5 or turn_action == 6 or turn_action ==7 or turn_action == 8: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')

 

 
#---------- Level: 2-----Infectiousness: 1----------
    elif virus_level_num.get() == 2 and virus_infect_num.get() == 1: 
        if turn_action == 1 or turn_action == 2 or turn_action == 3: 
            turn_action2 = randint(1,2) 

            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2: 

                turn_action3 = randint(1, 2) 

                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

         

         

        elif turn_action == 5 or turn_action == 6: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')

 

 
#---------- Level: 2-----Infectiousness: 2----------
    elif virus_level_num.get() == 2 and virus_infect_num.get() == 2: 
        if turn_action == 1 or turn_action == 2 or turn_action == 3: 
            turn_action2 = randint(1,2) 

            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2: 

                turn_action3 = randint(1, 2) 

                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

        elif turn_action == 5 or turn_action == 6 or turn_action == 7: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')

 

 
#---------- Level: 2-----Infectiousness: 3----------
    elif virus_level_num.get() == 2 and virus_infect_num.get() == 3: 
        if turn_action == 1 or turn_action == 2 or turn_action == 3: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2: 

                turn_action3 = randint(1, 2) 

                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

        elif turn_action == 5 or turn_action == 6 or turn_action == 7 or turn_action == 8: 

            turn_action2 = randint(1,2) 

            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')
                    
#---------- Level: 3-----Infectiousness: 1----------
    elif virus_level_num.get() == 3 and virus_infect_num.get() == 1: 

        if turn_action == 1 or turn_action == 2 or turn_action == 3 or turn_action == 4: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2: 

                turn_action3 = randint(1, 2) 

                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

        elif turn_action == 5 or turn_action == 6: 

            turn_action2 = randint(1,2) 

            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')

 

 
#---------- Level: 3-----Infectiousness: 2----------
    elif virus_level_num.get() == 3 and virus_infect_num.get() == 2: 
        if turn_action == 1 or turn_action == 2 or turn_action == 3 or turn_action == 4: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2: 

                turn_action3 = randint(1, 2) 

                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

        elif turn_action == 5 or turn_action == 6 or turn_action == 7: 

            turn_action2 = randint(1,2) 

            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')

#---------- Level: 3-----Infectiousness: 3----------
    elif virus_level_num.get() == 3 and virus_infect_num.get() == 3: 
        if turn_action == 1 or turn_action == 2 or turn_action == 3 or turn_action == 4: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1) 
                    dead_num.set(dead_num.get()+1) 
                    news_feed_content.set('A healthy person has died')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2: 

                turn_action3 = randint(1, 2) 

                if turn_action3 == 1:
                    if infected_num.get() > 0:
                        infected_num.set(infected_num.get()-1) 
                        dead_num.set(dead_num.get()+1) 
                        news_feed_content.set('An infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

                elif turn_action3 == 2:
                    if infected2_num.get() > 0:
                        infected2_num.set(infected2_num.get()-1)
                        dead_num.set(dead_num.get()+1)
                        news_feed_content.set('An severely infected person has died')
                    else:
                        news_feed_content.set('The virus has taken no action')

        elif turn_action == 5 or turn_action == 6 or turn_action == 7 or turn_action == 8: 
            turn_action2 = randint(1,2) 
            if turn_action2 == 1:
                if healthy_num.get() > 0:
                    healthy_num.set(healthy_num.get()-1)
                    infected_num.set(infected_num.get()+1)
                    news_feed_content.set('A healthy person has become infected')
                else:
                    news_feed_content.set('The virus has taken no action')

            elif turn_action2 == 2:
                if infected_num.get() > 0:
                    infected_num.set(infected_num.get()-1)
                    infected2_num.set(infected2_num.get()+1)
                    news_feed_content.set('An infected person has become very infected')
                else:
                    news_feed_content.set('The virus has taken no action')
        else:
            news_feed_content.set('The virus has taken no action')
    else:
        news_feed_content.set('The virus has taken no action')

    print(news_feed_content.get())
    # Changes Is_Player_Go to true so the player can now take his/her turn.
current_save_file[level_num][14] = True

    

# Player Turn

#  has 1/3 chance of curing a severely ill person and a 2/3 chance of curing an ill person
def cure_Proc():
    # print('cure_Proc, level_num is ' + str(level_num))
##    if current_save_file[level_num][14] == False:
##        pass
##    else:
       
    player_action = randint(1,3)
    if player_action == 1:
        if infected2_num.get() > 0:
            infected2_num.set(infected2_num.get()-1)
            healthy_num.set(healthy_num.get()+1)
            reputation_num.set(reputation_num.get()+1)
            news_feed_content.set('You helped a seriously ill person get better')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    else:
        if infected_num.get() > 0:
            infected_num.set(infected_num.get()-1)
            healthy_num.set(healthy_num.get()+1)
            reputation_num.set(reputation_num.get()+1)
            news_feed_content.set('You helped an ill person get better')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    print(news_feed_content.get())

# stronger cure – has ½ chance of either healing a severely or regularly ill person, either way makes them immune to being reinfected
def cure2_Proc():
##    if current_save_file[level_num][14] == False:
##        pass
##    else:
    if cure_number_num.get()>0:
        
        player_action = randint(1,2)
        if player_action == 1:
            if infected2_num.get()>0:
                reputation_num.set(reputation_num.get()+2)
                cure_number_num.set(cure_number_num.get()-1)
                infected2_num.set(infected2_num.get()-1)
                immune_num.set(immune_num.get()+1)
                news_feed_content.set('You helped a seriously ill person become immune to the virus')
            else:
                news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
        else:
            if infected_num.get()>0:
                reputation_num.set(reputation_num.get()+2)
                cure_number_num.set(cure_number_num.get()-1)
                infected_num.set(infected_num.get()-1)
                immune_num.set(immune_num.get()+1)
                news_feed_content.set('You helped an ill person become immune to the virus')
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
        if infected2_num.get() >0:
            infected2_num.set(infected2_num.get()-1)
            dead_num.set(dead_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You euthanised a seriously ill person')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    else:
        if infected_num.get() > 0:
            infected_num.set(infected_num.get()-1)
            dead_num.set(dead_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You euthanised an ill person.')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    print(news_feed_content.get())


# has a 1/9 chance of doing anyone of the 9 possible actions

# WARNING- if you over use, you will lose (probably)
def leave_Proc():
##    if current_save_file[level_num][14] == False:
##        pass
##    else:
    player_action = randint(1,9)
    if player_action == 1:
        if healthy_num.get() > 0:
            healthy_num.set(healthy_num.get()-1)
            dead_num.set(dead_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You let a healthy person die.')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 2:
        if healthy_num.get() > 0:
            healthy_num.set(healthy_num.get()-1)
            infected_num.set(infected_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You let a healthy person fall ill')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 3:
        if healthy_num.get() > 0:
            healthy_num.set(healthy_num.get()-1)
            infected2_num.set(infected2_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You let a healthy person fall seriously ill.')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
            
    elif player_action == 4:
        if infected_num.get() > 0:
            infected_num.set(infected_num.get()-1)
            dead_num.set(dead_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You allowed an ill person to die.')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 5:
        if infected2_num.get() > 0:
            infected2_num.set(infected2_num.get()-1)
            dead_num.set(dead_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You allowed a seriously ill person to die.')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 6:
        if infected_num.get() > 0:
            infected_num.set(infected_num.get()-1)
            infected2_num.set(infected2_num.get()+1)
            reputation_num.set(reputation_num.get()-2)
            news_feed_content.set('You allowed an ill person to become seriously ill.')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 7:
        if infected_num.get() > 0:
            infected_num.set(infected_num.get()-1)
            healthy_num.set(healthy_num.get()+1)
            reputation_num.set(reputation_num.get()+1)
            news_feed_content.set('You helped an ill person get better')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 8:
        if infected2_num.get() > 0:
            infected2_num.set(infected2_num.get()-1)
            healthy_num.set(healthy_num.get()+1)
            reputation_num.set(reputation_num.get()+1)
            news_feed_content.set('You helped a seriously ill person get better')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')

    elif player_action == 9:
        if healthy_num.get() > 0:
            healthy_num.set(healthy_num.get()-1)
            immune_num.set(immune_num.get()+1)
            reputation_num.set(reputation_num.get()+1)
            news_feed_content.set('A healthy person just developed immunity to the virus.')
        else:
            news_feed_content.set('You cannot perform that action now. Consequently, you have taken no action this turn.')
    print(news_feed_content.get())

# After execuing a function set done_turn_action to true
current_save_file[level_num][14] = True

# Action Button Combined Functions

def Cure_Button_Combined():
    print('----------Starting Player Turn----------')
    cure_Proc()
    print('----------Ending Player Turn----------')
    print('')
    Save_Level()
    if not Check_Win_Loss():
        Virus_Turn_Master()
        Save_Level()
        Check_Win_Loss()    
    
    
def Mega_Cure_Button_Combined():
    print('----------Starting Player Turn----------')
    cure2_Proc()
    print('----------Ending Player Turn----------')
    print('')
    Save_Level()
    if not Check_Win_Loss():
        Virus_Turn_Master()
        Save_Level()
        Check_Win_Loss()
    
def Kill_Button_Combined():
    print('----------Starting Player Turn----------')
    kill_Proc()
    print('----------Ending Player Turn----------')
    print('')
    Save_Level()
    if not Check_Win_Loss():
        Virus_Turn_Master()
        Save_Level()
        Check_Win_Loss()
    

def Leave_Button_Combined():
    print('----------Starting Player Turn----------')
    leave_Proc()
    print('----------Ending Player Turn----------')
    print('')
    Save_Level()
    if not Check_Win_Loss():
        Virus_Turn_Master()
        Save_Level()
        Check_Win_Loss()
    

# Check for a win or loss
def Check_Win_Loss():
    global Gameplay
    if infected_num.get() == 0 and infected2_num.get() == 0 and reputation_num.get() >= 50 and healthy_num.get() > dead_num.get():
        current_save_file[level_num][12] = True
        news_feed_content.set('You have won the game')
        print(news_feed_content.get())
        sleep(5)
        Gameplay.destroy()
        return True
    elif healthy_num.get() == 0 and immune_num.get() == 0:
        current_save_file[level_num][13] = True
        news_feed_content.set('You have lost the game')
        print(news_feed_content.get())
        sleep(5)
        Gameplay.destroy()
        return True
    else:
        return False

# Save Level
def Save_Level():
    #['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False],
    print('Saving...')
    current_save_file[level_num][1]=str(healthy_num.get())
    current_save_file[level_num][2]=str(infected_num.get())
    current_save_file[level_num][3]=str(infected2_num.get())
    current_save_file[level_num][4]=str(dead_num.get())
    current_save_file[level_num][5]=str(immune_num.get())
    current_save_file[level_num][6]=str(cure_number_num.get())
    current_save_file[level_num][7]=str(reputation_num.get())
    current_save_file[level_num][8]=str(virus_level_num.get())
    current_save_file[level_num][9]=str(virus_speed_num.get())
    current_save_file[level_num][10]=str(virus_infect_num.get())
    list_to_file()
    print('Done')
    
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
# level_select_image = PhotoImage(file="level select image.png")
# high_scores_image = PhotoImage(file='high scores image.png')

# global level_select_image
# global high_scores_image

Heading = Label(root, text='Launcher', font = ('Arial', 16, 'bold'))
Login_Button=Button(root, text='Login', command=render_login)
#winsound.PlaySound('test_music.mp3',winsound.SND_FILENAME)
Heading.pack()
Login_Button.pack()
