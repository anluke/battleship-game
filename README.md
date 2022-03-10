# BATTLESHIP GAME

This project was built to for Code Institute's Porfolio 3 Assessment.

**Battleship** is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

The live website can be found [here](link).


## How To Play

Battleship game is based on the classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))  
In this version the player is welcomed with a quick intro on top that described the game layout.  
From the start of the game it randomly places a computer ship somewhere on the grid.  
If a player guesses the location it will mark that spot with **'X'** and end the game with player being victorious.  
If a player misses the turn it will mark the spot with **'O'** and continue turns.


## Features



Connect your GitHub repository and deploy as normal.

## Testing

I have manually tested this project by doing the following:  

 - Passed the code through a PEP8 linter and confirmed there are no problems
 - Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice.
 - Tested in my local terminal and the Code Institute Heroku terminal.

### Bugs

**Solved Bugs**
 - When I wrote the ```try``` and ```except``` rule it did not catch ```ValueError``` as I anticipated so I realised that my mistake was indentation and position of my Exception rule.

 **Remaining Bugs**

  - No bugs remaining


**Validator Testing**
 - PEP8
    - No errors were returned from PEP8online.com

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

 - Steps for deployment:
     - Fork or clone this repository
     - Create a new Heroku app
     - Set the buildbacks to ```Python``` and ```NodeJS``` in that order
     - Link the Heroku app to the repository
     - Click on **Deploy**

## Credits

 - Sample README.md file from P3 Project Scope. I used this as a general guide and structured my README file using this as an example.

 - Wikipedia link on the top of the README file to provide more info on the Battleship game.

 - 