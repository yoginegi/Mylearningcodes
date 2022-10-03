import random                                                                 
while True:                                                                   
    choice=["rock", "paper", "scissors"]                                      
    comp= random.choice(choice)                                               
    user= None                                                                
                                                                              
    while user not in choice:                                                 
        user=input("Choose rock,paper or scissor: ").lower()                  
                                                                              
    print("Computer chose: "+comp)                                            
    print("you chose: "+user)                                                 
                                                                              
    if comp == user:                                                          
        print("its a draw")                                                   
    elif user == "rock":                                                      
        if comp == "paper":                                                   
            print("You lost!")                                                
        else:                                                                 
            print("You won!")                                                 
    elif user == "scissors":                                                  
        if comp == "rock":                                                    
            print("You lost!")                                                
        else:                                                                 
            print("You won!")                                                 
    elif user == "paper":                                                     
        if comp == "rock":                                                    
            print("You Won!")                                                 
        else:                                                                 
            print("You Lost!")                                                
    else:                                                                     
        print("Error")                                                        
                                                                              
    again = input("play again?(YES/NO): ").lower()                            
    if again != "yes":                                                        
        break                                                                 
print("bye")                                                                  
