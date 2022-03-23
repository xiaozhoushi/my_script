import os

input_path = ''
out_path = ''

with open(input_path, 'r') as f:
    vinfor = [tmp.strip('\n') for tmp in f.readlines()]
    