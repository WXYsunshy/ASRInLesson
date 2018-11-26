from sklearn.metrics.pairwise import cosine_similarity
#a=[[1,3,6,6],[2,2,8,8]]
#print(cosine_similarity(a))


from scipy.spatial import distance
dataSetI = [1, 2, 3, 4]
dataSetII =[[2, 4, 6, 8],[4,5,6,7]]
#result = 1 - distance.cosine(dataSetI, dataSetII)
#print(result)
print(cosine_similarity(dataSetI, dataSetII))