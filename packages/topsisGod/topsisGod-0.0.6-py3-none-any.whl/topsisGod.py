# data will be a data frame
# w is the weights list
# i is the impact list
# returns a list of the ranks of the alternatives
import numpy as np

def Normalize(dataset, nCol, weights):
    for i in range(0, nCol):
        temp = 0
        # Calculating Root of Sum of squares of a particular column
        for j in range(len(dataset)):
            temp = temp + dataset.iloc[j, i]**2
        temp = temp**0.5
        # Weighted Normalizing a element
        for j in range(len(dataset)):
            dataset.iat[j, i] = (dataset.iloc[j, i] / temp)*weights[i-1]
    return dataset

def Calc_Values(dataset, nCol, impact):
    p_sln = (dataset.max().values)[0:]
    n_sln = (dataset.min().values)[0:]
    for i in range(0, nCol):
        if impact[i-1] == '-':
            p_sln[i-1], n_sln[i-1] = n_sln[i-1], p_sln[i-1]
    return p_sln, n_sln

def topsis(data, w, i):
    data = Normalize(data, data.shape[1], w)
    p_sln, n_sln = Calc_Values(data, data.shape[1], i)
    score = []
    for i in range(len(data)):
        temp_p, temp_n = 0, 0
        for j in range(data.shape[1]):
            temp_p = temp_p + (p_sln[j-1] - data.iloc[i, j])**2
            temp_n = temp_n + (n_sln[j-1] - data.iloc[i, j])**2
        temp_p, temp_n = temp_p**0.5, temp_n**0.5
        score.append(temp_n/(temp_p + temp_n))
    return score



def rerank(data, score):
    data['Score'] = score
    data['Rank'] = data['Score'].rank(method='max', ascending = False)
    return data