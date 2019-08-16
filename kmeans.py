print('CPSC-51100, [Summer] [2019]') 
print('NAME: David Kennedy and Nisha George') 
print('PROGRAMMING ASSIGNMENT #2') 


# Import file and put contents into a list.
lineList = [line.rstrip('\n') for line in open('C:/Users/JoAnne/Desktop/prog2-input-data.txt')] 
floatList = [float(x) for x in lineList] 
     
# Ask user for amount of clusters, assign number of clusters to k. 
k = input("Enter the number of clusters: ") 
k = int(k) 
 
 
# Initialize variables to store points and update centroids. 
centroids = dict(zip(range(k), floatList[0:k])) 
clusters = dict(zip(range(k), [[] for i in range(k)])) 
mapping = dict(zip(range(k), [[] for i in range(k)])) 


c = 0 
temp2 = 0 
while temp2 != centroids:  # Program runs until centroids converge. 
    c = c + 1 
    temp2 = centroids.copy() 
    print(' ') 
    print('Iteration ' + str(c)) 
 
# Clears clusters for next run. 
clusters = dict(zip(range(k), [[] for i in range(k)])) 
      
#Find differences between points and centroid, stores in mapping dictionary. 
for i in range(0, len(floatList)): 
    for ii in range(0, k): 
        mapping[ii] = (floatList[i], ii, abs(floatList[i] - centroids[ii])) 

                    
# Find and add point with smallest difference to the cluster. 
temp = (10, (100, 100, 100)) 
for key, value in dict(mapping).items(): 
    aa = (key, value) 
if temp[1][2] < aa[1][2]: 
    aa = temp 
    temp = aa 
    clusters[aa[1][1]].append(aa[1][0]) 
 
 
# Update centroids and print output. 
for i in range(0, k): 
    centroids[i] = sum(clusters[i])/len(clusters[i]) 
    print(str(i) + ' ' + str(clusters[i])) 
    print(' ')  
    text = []  
    for point in lineList: 
        for key, value in clusters.items(): 
            for x in value: 
                if point == str(x): 
                    print('Point ' + str(point) + ' in cluster ' + str(key)) 

text.append('Point ' + str(point) + ' in cluster ' + str(key)) 
 
# Output file.                 
f = open('prog2-output-data.txt', 'w') 
for sentence in text: 
    f.write('\n' + str(sentence)) 
