import numpy as np

def visiters_per_city(visitors):
    uniques, counts = np.unique(visitors, return_counts=True)
    uniquecounts = zip(uniques, counts)

# example list of visitors
visitors = np.array(["amsterdam", "amsterdam","amsterdam","amsterdam", "utrecht", "den haag", "nijmegen", "den haag", "utrecht", "utrecht"])
