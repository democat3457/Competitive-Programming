"""
BEGIN ANNOTATION
PROBLEM URL: https://open.kattis.com/problems/irrationaldivision
TAGS: math, parity, game theory
EXPLANATION: since both players are playing optimally, they will never take a row/column of the
grid such that they lose happiness points. if the row/col has an even number of squares, then
taking any number of that row/col will net 0 points, but if the row/col has an odd number of
squares, then taking an even number of that row/col will net 0 points, but taking an odd number of
that row/col nets either +1 or -1 points, depending on the number of white/dark squares in the
adjacent row/col.

in a grid of p x q where p and q are positive *even* integers, there are various possibilities for
the player to take, but the only good ones are where the player takes an even number of columns; if
the player takes an odd number, the sister will have an advantage because the bottom row will have
more dark squares than white squares:
|----|            |---|
|x x |            | x |
| x x| take 1 col |x x|
|x x | ---------> | x |    this row gives sister the advantage, taking one row forces player to
| x x|         -> |x x| <- eventually take a -1 point total
|----|            |---|
as such, a grid of p x q where p and q are positive even integers will always result in a value
of 0, because it is optimal for both players to take even amounts on their turn.

this situation can be extended to grids of p x q where p is a positive even integer and q is any
positive integer; since the player can take any number of columns, but they will always net 0, the
player can take columns until the parity of the number of columns remaining is even. this ensures
that no matter what the sister does, both the sister and player will net 0 afterwards.

a similar situation can be shown with grids of p x q where p and q are positive odd integers. since
p times q is an odd number, the difference between the player and the sister must be an odd integer
as well. it can also be shown that the optimal strategy in this case is to take any odd number of
columns to gain a +1 advantage, since the adjacent column has one more dark square than white
square. no matter what the sister does, it is impossible for her to gain the advantage as she is
left with an even number of columns, and thus will always net 0. this strategy includes the simpler
strategy of taking the entire piece of chocolate, as the player still nets +1 happiness point.

finally, the case is a little more complex with grids of p x q where p and q are positive integers
but p is odd and q is even. the ultimate goal of a player in such grids is to force the other
person to take the white square in the top left. because p is odd, the player can start off with
a +1 advantage by taking an odd number of columns- however, it will be shown later that it is
optimal to take exactly one column. after the player takes an odd number of columns, the row
adjacent to the sister will have more white squares than dark squares, meaning she needs to take an
even number of rows to net 0 points. this means that the number of rows is still odd, but since the
player took an odd number of rows on their first turn, the column adjacent to the player also has
more white squares than dark squares, meaning that the player also needs to take an even number of
rows to maintain their +1 advantage. the optimal number of rows/cols for both players to take after
the player's first turn is 2, as it is an inverse race- the players each want to reach the top
right corner last, so they want to "advance" as slow as possible to try and force the other player
to take the last square. this reasoning also explains why it is optimal for the player to take one
column on their first turn.

after various examples of grids as specified above, it is evident that in a grid of p x q where q
is greater than p, the player wins the inverse race, forcing the sister to take the remaining white
square, netting her -1 points and making the total difference 2 (the +1 advantage at the start,
minus the sister's -1 points). when q is instead less than p, the sister wins the inverse race,
forcing the player to take the white square and eliminating the player's +1 advantage, making the
total difference 0.
END ANNOTATION
"""
p,q = map(int, input().split())
if p % 2 == 0:
    print(0)
elif q % 2 == 1:
    print(1)
elif q > p:
    print(2)
else:
    print(0)
