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
 - [ ] Implement a priority pattern finder (check A2 for an implementation)
   - [ ] Win Pattern (X.XXX, .XXXX, etc...)
   - [ ] Block Win (like win pattern, but block the opponent's)
     - [ ] Special Case: .XXXX. should return both open points
   - [ ] Open Four (ex: .XXX.. => .XXXX.)
   - [ ] Block Open Four
   - [ ] If none of the above patterns are matched, return a legal move
 - [ ] Implement new GTP Commands
   - [ ] policy `policytype` (policytype={`random`, `rulebased`})
   - [ ] policy_moves => `MoveType move1 move2 move3`
     - [ ] Example: with `random` policy output: `Random E4 E5 E6...`
     - [ ] With `rulebased` policy output MoveType={Win, BlockWin, OpenFour, BlockOpenFour, Random} and the move
   - [ ] genmove color (generate a move based on rulebased policy)
 - [ ] ben_tests.tst should probably still pass, except for test #220
 - [ ] create extra tests to test the above functionality