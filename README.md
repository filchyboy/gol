# Game of Life Metrics

Exploring and visualizing output from the Game of Life.

## About the Game of Life

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced players, by creating patterns with particular properties.[[2](https://computersciencewiki.org/index.php/Game_of_Life#cite_note-2)]


The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

	Any live cell with fewer than two live neighbors dies, as if by under population.
	Any live cell with two or three live neighbors lives on to the next generation.
	Any live cell with more than three live neighbors dies, as if by overpopulation.
	Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.[[3](https://computersciencewiki.org/index.php/Game_of_Life#cite_note-3)]

*Taken from [Game of Life problem set on Computer Science Wiki](https://computersciencewiki.org/index.php/Game_of_Life)*


## Goals

The standard presentation of the Game of Life, which was initially developed by Conley (insert full name), is done by creating a grid of asterisks, or some other marker, and a relief entity. My take on this involves using `1` & `0` as the markers and making the expected two-dimensional grid into a one-dimensional line. I intend to create a flat time series of the grown cells and present that within a Plotly dash application time-series visualization. I suspect that this perspective will show patterns not easily seen within the classic game of life model.

## Methods

### Generating a Random Sequence on a Grid

First, I am generating a random sequence of `1` & `0` and then make an integral division of the length of that sequence by its square root to determine the side length of the game of life grid. So, for example, in our test case, my initial series is 670 integers. By applying the integral division to this, I find that with this number of cells, I can use 625 of them to make a square grid with 25 cells per side. I then strip the remaining 45 cells off the tail of the sequence. The grid itself uses `X, Y` coordinates of `0, 0`  incremented positive `X` coordinates, and negative `Y` coordinates. The subsequent grid shows the top left corner to be `0, 0` and the bottom right corner to be at `25, 25`.

Next, I add to this sequence a host of accompanying data points that show each cell in the context of 8 empty cells around it, plus information on the list's re-factored length, its side length, and it's series. That's then added to a DB of initial seeds for later analysis. 

TODO: Enable a series of seeds. Currently, all of this is manual. This step will come as part of a deployment build. There will be a toggled control to choose a specific seed for analysis.

### Running Through Generations of the Game of Life

In the generator portion of this project, I retrieve the initial cell states list from the DB and begin matching the cell node values from each of the surrounding eight coordinates to tabulate a total number of live cells around each node.  

Next, I add to this sequence a host of accompanying data points that show each cell in the context of 8 empty cells around it, plus information on the list's re-factored length, its side length, and it's series. That's then added to a DB of initial seeds for later analysis.

TODO: Enable a series of seeds. Currently, all of this is manual. This step will come as part of a deployment build. There will be a toggled control to choose a specific seed for analysis.

### Running Through Generations of the Game of Life

In the generator portion of this project, I retrieve the initial cell states list from the DB and begin matching the cell node values from each of the surrounding eight coordinates to tabulate a total number of live cells around each node. Then the rules of life are applied, and the individual cell node reflects the new state of `1` or `0`.  This new sequence, added to the database, then goes through the same steps until the set generations limit.

Please note that this exercise quickly ran against inherent limitations to DB structures. This exercise currently handles no more than 625 cells as each cell is assigned a unique DB feature. Any number of cells above the number easily handled by MySQL will require a change in the data store.

TODO: Explore using NoSQL as a data store. The initial data could be potentially a million digits long and still be possible to generate and analyze.

### Analyzing the Results


Here's a screen shot of the total live cells at each generation:

![](https://github.com/filchyboy/gol/raw/main/Screen_Shot_2020-10-26_at_5.37.08_PM.png)

And here's a screen shot of the number of cells which have not evolved at each generation:

![](https://github.com/filchyboy/gol/raw/main/Screen%20Shot%202020-10-26%20at%205.47.40%20PM.png)

At the most basic level the data analyzation is being presented through a plotly dash application. Currently this is a proof of concept. In future iterations this dashboard into the data will become more verbose and will incorporate callbacks to handle time sequence and other parameters.



