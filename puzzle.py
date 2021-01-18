#!/usr/bin/env python
from status import Status 
from entry import Entry 
import numpy as np 
import math 
import copy 
import time

class Puzzle:
    def __init__(self, _tiles):
        self.tiles = _tiles
        self.grid_size = int(math.sqrt(len(_tiles)))
        self.DIM = len(_tiles)
        self.status = Status(0)
        self.domain_choices = [1,2,3,4,5,6,7,8,9]
        self.states = []
        self.init_state_to_evaluate = None
        self.init_sudoku()

    # Store all the unassigned states 
    def init_sudoku(self):
        states = []
        for row_index in range(self.DIM):
            for col_index in range(self.DIM):
                if self.tiles[row_index][col_index] == 0: # if the tile is unassigned, put it in the states list 
                    unassigned_state = Entry(row_index, col_index, self.tiles)
                    states.append(unassigned_state)
        self.states = states
        self.state_to_evaluate = states.pop()
        self.print_all_curr_data('init')
        time.sleep(1)
        
    def solve(self):
        self.status.set_status(1)
        self.print_all_curr_data('solve')
        time.sleep(1)
        self.recursively_solve(self.state_to_evaluate, self.states, self.tiles)

    #use recursive function to realize Forward checking
    def recursively_solve(self, state, unassigned_states, SUDOKU):
        # self.print_status()
        for assignment_option in state.options:
            state.value = assignment_option
            
            # check if the assignment option can satisfy the SUDOKU 
            if state.value in state.calc_options(SUDOKU):
                SUDOKU[state.row][state.col] = state.value
                
                # check if solved
                if len(unassigned_states) == 0:
                    self.status.set_status(2)
                    self.tiles = SUDOKU
                    self.print_all_curr_data('complete')
                    time.sleep(1)
                    break

                else:
                    next_state = unassigned_states.pop()
                    self.recursively_solve(next_state, unassigned_states, SUDOKU)

                    # if the function did not find the solution in this branch, it will come back to the most recent situation
                    SUDOKU[state.row][state.col] = 0
                    SUDOKU[next_state.row][next_state.col] = 0
                    next_state.value = 0

                    # no solution found, add the state back to the unassigned_states list
                    unassigned_states.append(next_state)

    def message_string(self, state):
        s = "\n********************************\n"
        if state == 'init':
            s = s + "*** INITIALIZE SUDOKU PUZZLE ***\n"
            s = s + "********************************\n"
        elif state == 'solve':
            s = s + "***   BEGIN SOLVING PUZZLE   ***\n"
            s = s + "********************************\n"
        elif state == 'complete':
            s = s + "*** PUZZLE SOLVING COMPLETE  ***\n"
            s = s + "********************************\n"
        return s

    def print_all_curr_data(self, msg=''):
        s = self.message_string(msg) + str(self.tiles) + '\n' + str(self.status)
        print(s)

    def __str__(self):
        s = self.message_string(msg) + str(self.tiles) + '\n' + str(self.status)
        return s 

