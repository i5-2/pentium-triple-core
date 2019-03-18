# Authors
hreherch (Bennett Hreherchuk) - 1399963
meinders (Mandy Meindersma) - 1433871
malik2 (Adil Malik) - 1477024

# FlatMC Gomoku Project

A Gomoku player for gogui that uses Flat Monte Carlo with
some rule/pattern identifying abilities.

## Notes

 * Only board sizes < 10 will be tested.
 * Move output should be capitalized. :)

## Requirements

 - [ ] Implement a Simple FlatMC player
   - [ ] At root: for each legal move simulate 10 games (win/loss/draw)
   - [ ] After, the move with the highest win rate is selected
   - [ ] The player should only resign or pass when the game is over
 - [x] Implement a priority pattern finder (check A2 for an implementation)
   - [x] Win Pattern (X.XXX, .XXXX, etc...)
   - [x] Block Win (like win pattern, but block the opponent's)
     - [x] Special Case: .XXXX. should return both open points
   - [x] Open Four (ex: .XXX.. => .XXXX.)
   - [x] Block Open Four
   - [x] If none of the above patterns are matched, return Random
 - [ ] Implement new GTP Commands
   - [x] policy `policytype` (policytype={`random`, `rulebased`})
   - [x] policy_moves => `MoveType move1 move2 move3`
     - [x] Example: with `random` policy output: `Random E4 E5 E6...`
     - [x] With `rulebased` policy output MoveType={Win, BlockWin, OpenFour, BlockOpenFour, Random} and the moves
   - [ ] genmove color (generate a move based on rulebased policy)
 - [ ] ben_tests.tst should probably still pass, except for test #220
 - [ ] create extra tests to test the above functionality

## Attribution

Some of this code was copied and continued from our assignment 2 code,
mainly the code in simple_board.py that detects winning and threat patterns.