import alphaBetaPruning
import game
import time


board=game.create()
game.whoIsFirst(board)
while not game.isFinished(board):
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
     #   start_time = time.time()
        board=alphaBetaPruning.go(board)
      #  print('---%s seconds seconds---' % (time.time() - start_time))
game.printState(board)


