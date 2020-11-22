import numpy as np
import argparse 

parser = argparse.ArgumentParser(description='Process lipid compositions to count tails')
parser.add_argument('infile', type=str,
                    help='an input file to count tails')
args = parser.parse_args()


# eg usage python tail_counter.py AAtreated_with_comments.dat
        

class lipid(object):
    """docstring for lipid"""
    def __init__(self, typ, name, tails):
        super(lipid, self).__init__()
        self.typ = typ
        self.name = name
        self.tails = tails


# read lipids from a composition file
lipids = []
with open(args.infile, 'r') as f:
    lines = f.readlines()
    for line in lines[1:-1]: #first line is blank
        toks = line.split()
        lipid_t = toks[0]
        lipid_string = toks[1]
        tail1 = toks[2]
        tail2 = toks[3]
        tail3 = toks[4]
        tail4 = toks[5]
        tail_list = [tail1,tail2,tail3,tail4]
        filtered_tails = [t for t in tail_list if t != '-']
        abundance = int(toks[6])
        for l in range(abundance):
            newlipid = lipid(lipid_t, lipid_string, filtered_tails)
            lipids.append(newlipid)

tails = [l.tails for l in lipids]
flat_tails = []
for sublist in tails:
    for item in sublist:
        flat_tails.append(item)
n_tails = len(flat_tails)

# ref types to count, must be updated manually
tail_types = ['14:0','16:0', '16:1', '16:2','17:0', '18:0', '18:1','18:2','18:3', '20:4', '20:5', '21:1',  '22:6']


print('\nWELCOME TO THE LIPID TAIL COUNTER\n')
print(f'the number of tails is {n_tails}')
store_dict = dict()
norm_dict  = dict()
for tail in tail_types:
    c = flat_tails.count(tail)
    store_dict[tail] = c
    norm_dict[tail]  = c/n_tails*100

print(' non normalised tail composition')
print('################################\n')
for k,v in store_dict.items():
    print(f'Tail: {k} has number of tails {v}')
print()    
print(' normalised tail composition')
print('############################\n')
for k,v in norm_dict.items():
    print(f'Tail: {k} has  normalised number of tails {v}')

sm = 0
for k,v in norm_dict.items():
    sm += v
print(f'sum of the normalised compositions is {sm}')





