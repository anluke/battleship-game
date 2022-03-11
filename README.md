
![Battleship Banner](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/battleship_banner.png?raw=true)
# BATTLESHIP GAME

This project was built for Code Institute's Portfolio 3 Assessment.

**Battleship** is a Python terminal game that runs in the Code Institute mock terminal on Heroku.

The live website can be found [here](https://battleship-game-p3.herokuapp.com/).

<br />

## How To Play

The Battleship game is based on the classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))  
In this version, the player is welcomed with a quick intro on top that described the game layout.  
From the start of the game it randomly places a computer ship somewhere on the grid.  
If a player guesses the location it will mark that spot with **'X'** and end the game with the player being victorious.  
If a player misses the turn it will mark the spot with **'O'** and continue turns.

<br />

## Features

### Start Game - Intro

![Start Game](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/game_start_intro.png?raw=true)

  - The Battleship board generates from the start and the computer places a ship at a random location.
  - The player cannot see where the computer's ship is.
  - The game also starts with a **Turn** counter. The game will have a maximum of 8 Turns. It is also displayed in the game intro.
  - The player cannot see where the computer's ship is.

<br />

### Win Game

![Win Game](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/win_game.png?raw=true)

 - If the player manages to hit the computer's battleship, the game ends with the player as a winner.
 - It also positions the **'X'** mark on the battleship board to easily distinguish the location of the computer ship.
 - In the print statement above the board it displays the coordinates of the ship. 
 - It also displays a winning statement congratulating the player on the success.

<br />

### Lose Game

![Lose Game](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/lose_game.png?raw=true)

 - The player will lose if he runs out of Turns.
 - The console will print out the statement that the player lost and that he was unsuccessful in locating a computer ship.
 - This ends the game and the player has to start anew.

<br />

 ### Miss Battleship


![Miss Battleship](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/battleship_miss.png?raw=true)

 - If the player misses the battleship, the statement will appear and **'O'** mark will appear on the coordinates selected.

![Board Miss](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/board_filling.png?raw=true)

- As the Turns go, the board starts to fill up with players' misses as seen in the above image.

<br />

## Input Validation

![Out of Bounds](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/out_of_bounds.png?raw=true)  ![Used Coordinates](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/used_coordinates.png?raw=true)

- During the game it's important to capture the wrong data and prompt the player to type the correct value.
- As you can see in the upper-left image, if a player inputs the value larger than what is required, the error message prints with a reminder that a number required is between **0** and **7**.
- There is also a case where a player could use the same coordinates as shown in the upper-right example.
- If so it will accept the input but print out a statement that those coordinates were used.
- Both of these examples will take the player's input and continue **Turn**. The reason being is that data was correct just not within game rules.


<br />
<br />


![Emptry String](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/empty_string.png?raw=true)  ![Word](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/word_error.png?raw=true)

 - The player is not allowed to input an empty string or a word. As seen above the console will print that the number is needed.
 - The code will not continue so **Turn** will freeze for the time being.
 - The console will keep prompting the player for a number and once the number has been input, the game will continue.

<br />

## Data Model

The main function of the game is ```print_board``` which automatically creates a **7** by **7** starting from the index **0**.  

I also defined functions to create a random row and column which are activated automatically and set coordinates for the computer's ship.  

The for loop will check for the player's input and return feedback depending on the value.


### Future implementations

 - In the future, the game could be updated with a larger **Color Coded** battleship board.
 - It could be a multiplayer game consisting of more than 1 player.
 - I wanted to use the learned content and build something simple and comprehensive. Nevertheless, there is more potential to this game.

<br />


## Testing

I have manually tested this project by doing the following:  

 - Passed the code through a PEP8 linter and confirmed there are no problems
 - Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice.
 - Tested in my local terminal and the Code Institute Heroku terminal.

### Bugs

 **Solved Bugs**
  - When I wrote the ```try``` and ```except``` rule it did not catch ```ValueError``` as I anticipated so I realised that my mistake was indentation and position of my Exception rule.

### Remaining Bugs

  - No bugs remaining

<br />

### Validator Testing
 
 #### PEP8

   - No errors were returned from [PEP8 Python Validator](http://pep8online.com/)

  ![PEP8 Check](https://github.com/anluke/battleship-game/blob/main/assets/images/readme_snips/pep8_check.png?raw=true)

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

 - Steps for deployment:
     - Fork or clone this repository
     - Create a new Heroku app
     - Set the build-backs to ```Python``` and ```NodeJS``` in that order
     - Link the Heroku app to the repository
     - Click on **Deploy**

## Credits

 - Sample [README.md](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/) file from P3 Project Scope. I used this as a general guide and structured my README file using this as an example.

 - [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) link on the top of the README file to provide more info on the Battleship game.

 - I used YouTube as a starting reference point. The content creator is [Knowledge Mavens](https://www.youtube.com/channel/UC7CTkf5Za9VD6JU1C0ZXWlg). His video helped me create a battleship board the way I wanted. A link to the video can be found [here](https://www.youtube.com/watch?v=tF1WRCrd_HQ). 

- [CodeAcademy](https://www.codecademy.com/) site was also helpful as a reference point. I quickly went through their small Battleship game project which can be found [here](https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship). I used a similar layout for the base of my game.

- The image for the README banner was downloaded from [PNG WING](https://www.pngwing.com/) and the link to the banner can be found [here](https://www.pngwing.com/en/free-png-nzrax)