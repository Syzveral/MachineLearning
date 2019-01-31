from random import choice;

rock = 0;
paper = 0;
scissors = 0;

def BigSmall(a,b,c):
        if (a > b and a > c):
            return True;
        return False;

def printc(text=""):
    print("Computer: " + text);
def pInput(text=""):
    return input("Player: " + text);

while True:
    printc("Rock, Paper, or Scissors?");
    playerMove = pInput("I choose ").lower();
    computerMove = "";

    #Creating probabilities
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
        elif (computerMove == "Scissors"):
            printc("You win");

    elif (playerMove == "paper"):
        paper += 1;
        if (computerMove == "Paper"):
            printc("No winner");
        elif (computerMove == "Scissors"):
            printc("I win");
        elif (computerMove == "Rock"):
            printc("You win");

    elif (playerMove == "scissors"):
        scissors += 1;
        if (computerMove == "Scissors"):
            printc("No winner");
        elif (computerMove == "Rock"):
            printc("I win");
        elif (computerMove == "Paper"):
            printc("You win");

    print();
    



