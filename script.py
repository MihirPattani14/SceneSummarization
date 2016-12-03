from os import listdir, system
import asift
from kst import kruskal_mst

#Stores each pairs matched keypoints
allKeypointPairs={}

#The folder containing images
folder_path="data/trial"
files = [f for f in listdir(folder_path)]
print (files)
#Matches every image with the other
for i in range(0, len(files)):
    for j in range(0, len(files)):#For undirected graph

        allKeypointPairs[(i,j)]=asift.start("sift", folder_path+"/"+files[i], folder_path+"/"+files[j])
	print ("*********")	

#Sorts the dict based on the number of matches, returns a list of only the dict's indices ie the sorted image pairs
sortedKeypointPairs = [k for (k,v) in sorted(allKeypointPairs.items(), key=lambda x: len(x[1]),reverse=True)]	
print (sortedKeypointPairs)
#print (allKeypointPairs[(0,2)])
##Greedy Algorithm to form the spanning tree##

#initialze the adjacency matrix
spanningTree=kruskal_mst(range(0, len(files)),sortedKeypointPairs)
print (spanningTree) 

tracks=[]
for image_pair in spanningTree:
    for keypoint_pair in allKeypointPairs[image_pair]:
	tracked=0
    	for track in tracks:
	    if image_pair[0] in track[0] and keypoint_pair[0] in track[1]:
		track[0].append(image_pair[1])
		track[1].append(keypoint_pair[1])
		tracked=1
		break
	    elif image_pair[1] in track[0] and keypoint_pair[1] in track[1]:
		track[0].append(image_pair[0])
		track[1].append(keypoint_pair[0])
		tracked=1
		break
	if tracked==0:
	    tracks.append([[image_pair[0],image_pair[1]],[keypoint_pair[0],keypoint_pair[1]]])

for t in tracks:
    if len(t[0])>2:
    	print (t[0]),
    	print (len(t[1]))
    


    
    






