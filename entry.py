#!/usr/bin/env python

import numpy as np 
import math 
import copy 

# sused to record tile position, value, and any possible options for assignment
class Entry:
    def __init__(self, i_row, i_col, tiles):
        self.row = i_row
        self.col = i_col
        self.value = 0
        self.block_size = int(math.sqrt(len(tiles)))
        self.lower_bound_row = i_row - (i_row % self.block_size)
        self.lower_bound_col = i_col - (i_col % self.block_size)
        self.full_set = set([1,2,3,4,5,6,7,8,9])
        self.options = list(self.calc_options(tiles))

    def calc_options(self, puzzle):
        non_options = self.non_options(puzzle)
        return self.full_set.symmetric_difference(non_options)

    def non_options(self, puzzle):
        domain_col = self.get_taken_col_entries(puzzle)
        domain_row = self.get_taken_row_entries(puzzle)
        domain_block = self.get_taken_block_entries(puzzle)
        options = (domain_col.union(domain_row)).union(domain_block)
        return options

    def get_taken_col_entries(self, puzzle):
        full_col = puzzle[:, self.col]
        taken_entries = set(full_col[full_col != 0])
        # domain_col = np.setdiff1d(self.full_set, taken_entries)
        # return domain_col
        return taken_entries

    def get_taken_row_entries(self, puzzle):
        full_row = puzzle[self.row]
        taken_entries = set(full_row[full_row != 0])
        # domain_row = np.setdiff1d(self.full_set, taken_entries)
        # return domain_row
        return taken_entries

    def get_taken_block_entries(self, puzzle):
        l_row = self.lower_bound_row
        u_row = l_row + self.block_size

        l_col = self.lower_bound_col
        u_col = l_col + self.block_size

        block = puzzle[l_row:u_row, l_col:u_col]

        flattened_grid = block.flatten()
        taken_entries = set(flattened_grid[flattened_grid != 0])

        return taken_entries

    def __str__(self):
        s = '[' + str(self.row) +  ', ' + str(self.col) + ']: ' + str(self.value)
        return s 






