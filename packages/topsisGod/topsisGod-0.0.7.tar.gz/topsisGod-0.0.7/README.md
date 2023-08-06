# Topsis Score Calculation package

>pip install topsisGod

>from topsisGod import topsis

Input: Three parameters

1. data: data should contain only integer fields so preprocess the data and temporarily remove the model names
2. Weights: weight of each attribute, considered to be an integer list
3. Impact: Considered to be a character list

Weight = [1, 1, 1, 1]

Impact = ['+', '-', '-', '+']

Output: Returns the score of each row

To calculate the rank based on the score, append the score list as:

>data['Score'] = topsis(data, w, i)

>data['Rank'] = data['Score'].rank(method = 'max', ascending = False)

Github link : [GitHub]("https://github.com/Sahil-Chhabra-09/TOPSIS-Package")