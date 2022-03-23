import pickle
path = '/Users/Documents/tmp/nnUNetPlansv2.1_plans_2D.pkl'
with open(path, 'rb') as f:
    data = pickle.load(f)
    print(data)
