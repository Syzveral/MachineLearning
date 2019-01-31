from random import choice;

sensitivity = 1;

rock = 0;
paper = 0;
scissors = 0;

cScore = 0;
pScore = 0;

moves = [];

def BigSmall(a,b,c):
        if (a > b and a > c):
            return True;
        return False;

def printc(text=""):
    print("Computer: " + text);
def pInput(text=""):
    return input("Player: " + text);

while True:
    printc("Current Score: " + str(cScore) + " , " + str(pScore));
    printc("Rock, Paper, or Scissors?");
    playerMove = pInput("I choose ").lower();
    computerMove = "";
    moves.append(playerMove);
        
    #Creating probabilities
    if (len(moves) > 2):
        lastMove = moves[-1];
        penultimate = moves[-2];
        if (lastMove == penultimate):
            a = (rock + paper + scissors) /3
            #Take into account a possible repetition of moves
            if (penultimate == "rock"):
                rock = paper = scissors = a;
                rock += sensitivity;
            elif (penultimate == "paper"):
                rock = paper = scissors = a;
                paper += sensitivity;
            elif (penultimate == "scissors"):
                rock = paper = scissors = a;
                scissors += sensitivity;
                
                
    e = rock + paper + scissors;
    if (e == 0):
        e += 1;
    r = rock / e;
    p = paper / e;
    s = scissors / e;
    
    #Comparing probabilities
    if (BigSmall(r,p,s)):
        computerMove = "Paper";
    elif (BigSmall(p,s,r)):
        computerMove = "Scissors";
    elif (BigSmall(s,r,p)):
        computerMove = "Rock";
    else:
        computerMove = choice(["Rock","Paper","Scissors"]);

    print();
    printc(computerMove);
    print();
    
    #Compare answers and adjust probability
    if (playerMove == "rock"):
        rock += 1;
        if (computerMove == "Rock"):
            printc("No winner");
        elif (computerMove == "Paper"):
            printc("I win");
            cScore += 1;
        elif (computerMove == "Scissors"):
            printc("You win");
            pScore += 1;

    elif (playerMove == "paper"):
        paper += 1;
        if (computerMove == "Paper"):
            printc("No winner");
        elif (computerMove == "Scissors"):
            printc("I win");
            cScore += 1;
        elif (computerMove == "Rock"):
            printc("You win");
            pScore += 1;

    elif (playerMove == "scissors"):
        scissors += 1;
        if (computerMove == "Scissors"):
            printc("No winner");
        elif (computerMove == "Rock"):
            printc("I win");
            cScore += 1;
        elif (computerMove == "Paper"):
            printc("You win");
            pScore += 1;

    print();
