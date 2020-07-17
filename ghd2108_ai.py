#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: Gabriel Dong ghd@108
"""

import random
import sys
import time

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    p1_score = 0
    p2_score = 0
    val = 0
    score = get_score(board)

    #number of chips on board
    for x in range(len(board)):
      for y in range(len(board)):
        if board[x][y] == 1:
          p1_score += 1
        else:
          p2_score += 1
    
    #corners p1
    if (0,0) == 1:
      p1_score += 10
    if (0,7) == 1:
      p1_score += 10
    if (7,0) == 1:
      p1_score += 10
    if (7,7) == 1:
      p1_score += 10

    #corners p2
    if (0,0) == 2:
      p2_score += 10
    if (0,7) == 2:
      p2_score += 10
    if (7,0) == 2:
      p2_score += 10
    if (7,7) == 2:
      p2_score += 10
    
    #next to corners p1
    if (1,1) == 1:
      p1_score -= 5
    if (1,6) == 1:
      p1_score -= 5
    if (6,1) == 1:
      p1_score -= 5
    if (6,6) == 1:
      p1_score -= 5

    if (1,0) == 1:
      p1_score -= 5
    if (7,1) == 1:
      p1_score -= 5
    if (6,7) == 1:
      p1_score -= 5
    if (1,7) == 1:
      p1_score -= 5
    
    if (0,1) == 1:
      p1_score -= 5
    if (6,0) == 1:
      p1_score -= 5
    if (7,6) == 1:
      p1_score -= 5
    if (0,6) == 1:
      p1_score -= 5
    
    #next to corners p2
    if (1,1) == 2:
      p2_score -= 5
    if (1,6) == 2:
      p2_score -= 5
    if (6,1) == 2:
      p2_score -= 5
    if (6,6) == 2:
      p2_score -= 5
    
    if (1,0) == 2:
      p2_score -= 5
    if (7,1) == 2:
      p2_score -= 5
    if (6,7) == 2:
      p2_score -= 5
    if (1,7) == 2:
      p2_score -= 5
    
    if (0,1) == 2:
      p2_score -= 5
    if (6,0) == 2:
      p2_score -= 5
    if (7,6) == 2:
      p2_score -= 5
    if (0,6) == 2:
      p2_score -= 5
    
    if color == 1:
      val = p1_score - p2_score
    else:
      val = p2_score - p1_score

    return val

    

    

############ MINIMAX ###############################

def minimax_min_node(board, color, level, limit):
    moves = get_possible_moves(board, color)
    successors = []

    if len(moves) == 0:
      if color == 1:
        color = 2
      else:
        color = 1
      return compute_utility(board, color)

    for x in range(len(moves)):
      successors.append(play_move(board, color, moves[x][0], moves[x][1]))

    if color == 1:
      color = 2
    else:
      color = 1

    minval = 10000000000
    if level == limit:
      for x in successors:
        maxn = compute_utility(x, color)
        if maxn < minval:
          minval = maxn
    else:
      level+=1
      for x in successors:
        maxn = minimax_max_node(x, color, level, limit)
        if maxn < minval:
          minval = maxn

    return minval


def minimax_max_node(board, color, level, limit):
    moves = get_possible_moves(board, color)
    successors = []

    if len(moves) == 0:
      return compute_utility(board, color)

    for x in range(len(moves)):
      successors.append(play_move(board, color, moves[x][0], moves[x][1]))

    

    maxval = -100000
    if level == limit:
      for x in successors:
        minn = compute_utility(x, color)
        if minn > maxval:
          maxval = minn
    else:
      level += 1
      if color == 1:
       color = 2
      else:
        color = 1
      for x in successors:
        minn = minimax_min_node(x, color, level, limit)
        if minn > maxval:
          maxval = minn
    return maxval

    
def select_move_minimax(board, color, level, limit):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    successors = []
    moves = get_possible_moves(board, color)

    for x in range(len(moves)):
        successors.append((play_move(board, color, moves[x][0], moves[x][1]), moves[x]))
 

    if color == 1:
      color = 2
    else:
      color = 1

    nextm = (-1000000, 1)
    
    for x in successors:
      temp = (minimax_min_node(x[0], color, level, limit),x[1])
      if nextm < temp:
        nextm = temp
    return nextm[1]

#python othello_gui.py ghd2108_ai.py randy_ai.py
#python othello_gui.py randy_ai.py ghd2108_ai.py
#python othello_gui.py ghd2108_ai.py ghd2108_ai.py
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None


def select_move_alphabeta(board, color): 
    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color, 1, 3)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
