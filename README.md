# BATTLESHIP GAME

This project was built to for Code Institute's Porfolio 3 Assessment.

**Battleship** is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

The live website can be found [here](link).

<br />

## How To Play

Battleship game is based on the classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))  
In this version the player is welcomed with a quick intro on top that described the game layout.  
From the start of the game it randomly places a computer ship somewhere on the grid.  
If a player guesses the location it will mark that spot with **'X'** and end the game with player being victorious.  
If a player misses the turn it will mark the spot with **'O'** and continue turns.

<br />

## Features

### Start Game - Intro

![Start Game](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/game_start_intro.png?raw=true)

  - Battleship board generates from the start and the computer places a ship at the random location.
  - The player cannot see where the computer's ship is.
  - The game also starts with a **Turn** counter. The game will have maximum of 8 Turns. It is also displayed in the game intro.
  - The player cannot see where the computer's ship is.

### Win Game

![Win Game](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/win_game.png?raw=true)

 - If the player manages to hit computer's battleship, the game ends with player as a winner.
 - It also positions the **'X'** mark on the battleship board to easily distinguish the location of the computer ship.
 - In the print statement above the board it displays the coordinates of the ship. 
 - It also displayes a winning statement congratulating the player on the success.

### Lose Game

![Lose Game](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/lose_game.png?raw=true)

 - The player will lose if he runs out of Turns.
 - The console will print out the statement that player lost and that he was unsuccessful finding computer ship.
 - This ends the game and the player has to start anew.

 ### Miss Battleship


![Miss Battleship](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/battleship_miss.png?raw=true)

 - If the player misses the battleship, the statement will appear and **'O'** mark will appear on the coordinates selected.

![Board Miss](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/board_filling.png?raw=true)

- As the Turns go, the board starts to fill up with player's misses as seen in above image.


## Input Validation

![Out of Bounds](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/out_of_bounds.png?raw=true)  ![Used Coordinates](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/used_coordinates.png?raw=true)

- During the game it's important to capture the wrong data and prompt the player to type the correct value.
- As you can see in the upper-left image, if a player inputs the value larger then what is required, the error message prints with a reminder that a number required is between **0** and **7**.
- There is also a case where a player could use the same coordinates as shown in the upper-right example.
- If so it will accept the input but print out a statement that those coordinates were used.
- Both of these examples will take the players input and continue **Turn**. Reason being is that data was correct just not within game rules.


<br />
<br />


![Emptry String](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/empty_string.png?raw=true)  ![Word](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/word_error.png?raw=true)

 - The player is not allowed to input an emptry string or a word. As seen above the console will print that the number is needed.
 - The code will not continue so **Turn** will freeze for the time being.
 - Console will keep prompting the player for a number and once the number has been input, the game will continue.

<br />

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