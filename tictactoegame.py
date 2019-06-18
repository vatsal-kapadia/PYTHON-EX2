box = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
   
state = Running    
Mark = 'X'    
def box():    
    print(" %c | %c | %c " % (box[1],box[2],box[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (box[4],box[5],box[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (box[7],box[8],box[9]))    
    print("   |   |   ")    
def Position(x):    
    if(box[x] == ' '):    
        return True    
    else:    
        return False    
def Win():    
    global state    
        
    if(box[1] == box[2] and box[2] == box[3] and box[1] != ' '):    
        state = Win    
    elif(box[4] == box[5] and box[5] == box[6] and box[4] != ' '):    
        state = Win    
    elif(box[7] == box[8] and box[8] == box[9] and box[7] != ' '):    
        state = Win    
        
    elif(box[1] == box[4] and box[4] == box[7] and box[1] != ' '):    
        state = Win    
    elif(box[2] == box[5] and box[5] == box[8] and box[2] != ' '):    
        state = Win    
    elif(box[3] == box[6] and box[6] == box[9] and box[3] != ' '):    
        state=Win    
       
    elif(box[1] == box[5] and box[5] == box[9] and box[5] != ' '):    
        state = Win    
    elif(box[3] == box[5] and box[5] == box[7] and box[5] != ' '):    
        state=Win    
        
    elif(box[1]!=' ' and box[2]!=' ' and box[3]!=' ' and box[4]!=' ' and box[5]!=' ' and box[6]!=' ' and box[7]!=' ' and box[8]!=' ' and box[9]!=' '):    
        state=Draw    
    else:            
        state=Running    
    
 
print("Player 1: [X]\n")    
print("Player 2: [O]\n") 
print()    
    
   
while(state == Running):    
       
 box()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(Position(choice)):    
        box[choice] = Mark    
        player+=1    
        Win()    
    
     box()    
if(state==Draw):    
    print("Game Draw")    
elif(state==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won") 