# ALien Apocalypse & Infection Problem using BFS or DFS

Task 1:
An educational institution “X” has hired someone to design a system known as an “Infected tracker. An infected tracker tries to figure out the region/number of surrounding people who can be affected by a single person. Then it prints the maximum region infected. Here Y can considered as being infected and N as not infected.

The task is to find the maximum region with Y i.e. max people infected in a region so that strict measures can be taken in that region using DFS keeping in mind that two people are said to be infected if two elements in the matrix are Y horizontally, vertically or diagonally. ==================================================================
Sample Input

N N N Y Y N N

N Y N N Y Y N

Y Y N Y N N Y

N N N N N Y N

Y Y N N N N N

N N N Y N N N

==================================================================

Sample Output

7

==================================================================

Task2:
There is an Alien(Xenomorph) Apocalypse in XCITY and every minute Aliens are attacking human beings around them.

Imagine XCITY as a grid where "A" represents the position of an Alien, "H" represents the position of a human being and "T" represents heat traps set up by humans which the Aliens cannot cross. The regions of the Aliens will not overlap, i.e. two or more Aliens will never have a common human to prey on.

An Alien can attack human beings on it's north,south,east and west simultaneously using its deadly advanced physical attributes. A human being becomes a host after an attack and a new Alien spawns in that position.

The task is to find out the minimum number of minutes it would take for the Aliens to attack all the humans around them using BFS. Also, print "No one survived" if no human beings survive the Apocalypse or "number_of_human_beings survived" otherwise.

==================================================================
Sample Input:

5

4

A H T H

H H T A

T T H H

A H T H

H T H H

Sample Output:

Time: 4 minutes

No one survived

Explanation: There are 3 regions here marked with Red, Green and Blue borders. The attacking Aliens have Yellow background and the humans being attacked have Red background.

At Time=1, three Aliens in 3 different regions attack the humans around them simultaneously (north, south, east, west). New Aliens spawn in place of the attacked humans.

At Time=2, two Aliens in Red and Blue regions attack the humans around them simultaneously and new aliens spawn in place of the attacked humans. The Green region has no more humans left.

At Time=3, only one Alien in the Blue region attacks the human to the south of it and a new alien spawns in place of the attacked human. The Red region has no more humans left.

At Time=4, only one Alien in the Blue region attacks the last human to the west of it and so in the final grid, no humans are left.
