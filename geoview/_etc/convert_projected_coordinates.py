from pyproj import Proj, transform

result = []
with open('./tests/test.csv', "r") as f:
    for line in f:
        result.append(map(float, line.split()))

print result[0]

f_out = open('./tests/out.csv', 'w')

inProj = Proj(init='epsg:4326')
outProj = Proj(init='epsg:32632')
i = 0
outCoord = []
for i in range(len(result)):
    #outCoord.append(transform(inProj,outProj,result[i][0], result[i][1]))
    x2,y2 = transform(inProj,outProj,result[i][0], result[i][1])
    f_out.write("%s, %s\n" % (x2,  y2))
    i = i + 1

#print outCoord

x1,y1 = 55.3401791889,37.7340903999
x2,y2 = transform(inProj,outProj,x1,y1)
print x2,y2