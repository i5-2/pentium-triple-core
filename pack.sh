rm -rf assignment3.tgz
rm -rf assignment3
mkdir assignment3
cp board_util.py assignment3/board_util.py
cp gtp_connection.py assignment3/gtp_connection.py
cp readme.txt assignment3/readme.txt
cp simple_board.py assignment3/simple_board.py
cp Gomoku.py assignment3/Gomoku.py
cp Gomoku3.py assignment3/Gomoku3.py
cp presubmission.log assignment3/presubmission.log
cp assignment3-public-tests.gtp assignment3/assignment3-public-tests.gtp
tar cfz assignment3.tgz assignment3
rm -rf assignment3