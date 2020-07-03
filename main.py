
'''The four lines here below are the default locations for python to click on for the automation to
The setup of the program is ver simple, just enter the values below with the first numbers being 
the X-axis and the second number the Y-axis. These are the default values assuming you have discord installed
window maximized and on a 1920x1080 screen.

The only thing that you might have to change is the first location, which is the discord icon for python to click on,

I personally run windows have turned of the big white search bar on the task bar, and have the discord icon moved to the
forth location on the task bar from left to right. It is likely you would have a different one than me, so please adjust the
coordinates of "discord_app_icon"

If the program crashes on launch, please run the following command in your command prompt:

        "pip3 install pyautogui" and "pip3 install pyperclip"
        
Good luck AFK on Dank Memer xD
'''

discord_app_icon = (270, 1060)
textinput_box = (405, 995)
search_text_location = (405, 940)
guess_hint_location = (405, 915)

'''Ignore the code below if you dont understand python'''





# run "pip3 install pyautogui" and "pip3 install pyperclip" in the command prompt if modules have not been installed
import pyautogui as pya
import random, pyperclip
from time import sleep, time

pya.PAUSE = 1 # Allows each function to be slowed down by X second, to reduce error rate, "1" is default and possibly the best for my case
pya.FAILSAFE = True

'''
The user can quit the program by moving their mouse to the most left side of their screen
and scrub your mouse up and down and it would raise an error to close the program
'''
def ran_inter():
    return random.uniform(0.01, 0.05)

def get_ran(range1, range2, times):
    # Generate a list of three numbers
    global nums
    try:
        nums = random.sample(range(range1, range2), times)
    except:
        #1,2 or 9,10
        print('Unlikely Case Occured!')
        if range2 == 2:
            nums = [1, 1]
        elif range1 == 10:
            nums = [10, 10]
        else:
            nums = [range1, range2]
            print('Impossible Error Occured')

def guess(): # No cool down, bot takes 6.3 seconds to process this
    global nums
    pyperclip.copy("") # Clear the clipboard
    # Start the Guessing Game
    pya.typewrite('pls guess\n', interval=ran_inter())
    get_ran(1,11,3) # Get 3 random non-repeating of numbers from 1 to 10
    pya.typewrite(f'{nums[0]}\n', interval=ran_inter())
    pya.typewrite(f'hint\n', interval=ran_inter())
    
    # Select and copy the hint the bot has given us
    pya.tripleClick(guess_hint_location)
    
    pya.hotkey('ctrl', 'c')
    sleep(0.05) # A slight pause to allow python to retrieve clipboard data
    pya.click(textinput_box)
    string = pyperclip.paste()
            
    # Analyse the hint and get the number the bot has given us
    numbers = 0
    #print('String: ' + string) <--- Debug xD
    for word in string.split():
        word = word.replace('(','').replace(')','')
        if word.isdigit():
            numbers = numbers + int(word)
    
    #print('Numbers: ' + str(numbers))  <--- Debug xD
    # Check for keywords in the hint
    if "high" in string:
        get_ran(1, numbers, 2)
    elif "low" in string:
        get_ran(numbers + 1, 11, 2)
    else:
        nums.pop(0)
    
    #print(nums)  <--- Debug xD
    # Type the two new guesses and hopefully gets it right
    pya.typewrite(f'{nums[0]}\n', interval=ran_inter())
    pya.typewrite(f'{nums[1]}\n', interval=ran_inter())

def beg(): # cool down: 40 seconds
    pya.click(textinput_box)
    sleep(0.05)
    pya.typewrite(f'pls beg\n', interval=ran_inter())

def search(): # cool down: 30 seconds
    methods = ('search','scout')
    pya.typewrite(f'pls {random.choice(methods)}\n', interval=ran_inter())
    pya.tripleClick(search_text_location)
    pya.hotkey('ctrl', 'c')
    sleep(0.05)
    pya.click(textinput_box)
    search_string = str(pyperclip.paste()).split(',') # 'dresser, laundromat, pantry'
    
    for i in range(len(search_string)):
        search_string[i] = search_string[i].replace(' ','').lower() # ['dresser','laundromat','pantry']
    
    if 'dog' in search_string:
        pya.typewrite(f'dog\n', interval=ran_inter())
    elif 'dog' in search_string:
        pya.typewrite(f'dog\n', interval=ran_inter())
    elif 'hospital' in search_string:
        pya.typewrite(f'hospital\n', interval=ran_inter())
    elif 'discord' in search_string:
        pya.typewrite(f'discord\n', interval=ran_inter())
    elif 'sewer' in search_string:
        pya.typewrite(f'sewer\n', interval=ran_inter())
    else:
        pya.typewrite(f'{random.choice(search_string)}\n', interval=ran_inter())

def deposit():
    pya.click(textinput_box)
    sleep(0.05)
    pya.typewrite(f'pls dep all\n', interval=ran_inter())

def start_gambling():
    try:
        while True:
            beg()
            deposit()
            search()
            for i in range(5):
                guess()

    except KeyboardInterrupt:
        print('\nDone.')
        
if __name__ == "__main__":
    # This is only for my desktop, which needs to be exactly 1920x1080
    pya.click(discord_app_icon) # Opens up discord (assuming we are already in the chat of the gambling bot)
    pya.click(textinput_box) # Clicks on the text input bar in discord app (assuming your discord is already maximized)
    
    start_gambling() # Start the program