# Animal Rush


Welcome to the amazing game Animal Rush. The objective of the game is to reach the opposite bank of the river you are spawned in within the minimum time, and in the process dodge maximum obstacles in the river. There are strips of land in between, creating partitions, and on the land are fixed obstacles, while the river currents cause the obstacles in the river to be moving. Player 1 would be spawned as an owl on the lower bank, and would have to go towards the upper bank. Player  2 would be spawned as a tiger on the upper bank, and would have to go towards the lower bank. You need to dodge the cars, fishes, sharks, trees, mountains and many other obstacles that come in your path to victory.

## Installing the game
To start playing the game, make sure you have python3 and pygame installed on your system.
To install Python 3.7 on your system, use command
```sh
$ sudo apt-get update
$ sudo apt-get install python3.6
```
Now, install pip3 tool, using the command 
```sh
$ sudo apt-get install python3-pip
```
Now, install pygame, using the command
```sh
$ python3 -m pip install -U pygame --user
```
Now, you can play the game, by using the command
```sh
$ python3 newgame.py
```
when in the directory where the game is stored.

## Rounds
  - There would be 3 rounds for the game, with Player 1 playing the first match in the round, and Player 2 going for the second match in the round.
  - The result of the rounds played before the current round would be displayed on the top centre of the screen.
  - After each match is over, you can press Enter to begin the next match. At the end of the round, the winner of the round would be displayed on the screen.
  - In case of tie in a round, both players shall be declared winners of the round.
  - After the 3 rounds, the player who has won most number of rounds shall be declared the winner of the game.
  - The current round going on is displayed at the top centre of the screen.

## Scoring
  - The scoring is based on time, as well as the number of obstacles crossed, and also upon whether the river has been crossed or not.
  - Crossing each fixed obstacle will fetch you 5 points.
  - Crossing each moving obstacle will fetch you 10 points.
  - Reaching the End bank of the river would get you 100 extra points.
  - For every passing time in the round, your score will keep decreasing until you die or reach the end of the river. This speed of reduction in score of the player increases with every increasing round.
  - The score of both Player 1 and Player 2 appear on the top left corner of the game. 

## Obstacles
  - There are different types of obstacles - fixed and moving. The moving obstacles only exist in the river, and not on the ground.
  - Every moving obstacle has different speed, which increases in the next round if a player wins a particular round.
  - The number of obstacles keeps increasing as the rounds progress, making it tougher to cross, but also gives more points as number of obstacles increases.
  
## Controls
The controls for player 1 to move around in the Game are the up, down, left, right arrow keys, while the controls for Player 2 are the keys "W S A D" to move up, down, left right.

## Winner
  - The game will consist of three rounds.
  - The player who wins most number of rounds from the 3 rounds would be declared as the winner. 
  - In case both tie at the end of the 3 rounds, the game would be declared as tied.
