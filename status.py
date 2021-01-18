#!/usr/bin/env python

class Status:
    def __init__(self, status_val):
        self.status = status_val

    def set_status(self, stat):
        self.status = stat

    def check(self):
        return self.status

    def __str__(self):
        s, c = self.format_status(self.status)
        msg = 'PUZZLE STATUS: [' + str(s) + ']\n'
        s = c + msg + self.bcolors.ENDC
        return s

    # def status_msg(self, clr, msg):
    #     print(clr + msg + self.bcolors.ENDC)

    def format_status(self, val):
        if val == 0:
            return 'NOT RUNNING', self.bcolors.OKBLUE
        elif val == 1:
            return 'NOT SOLVED', self.bcolors.WARNING
        elif val == 2:
            return 'SOLVED', self.bcolors.OKGREEN
        elif val == 3:
            return 'FAILED', self.bcolors.FAIL
        else:
            return 'N/A', self.bcolors.WARNING

    ######## COLORS ########
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'