import math
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def showPoint(self):
        print("{},{}".format(self.x,self.y))
    #
    def calculateDistance(self,point1,point2):
        distance= math.sqrt((point2.y-point1.y)**2-(point2.x-point1.x)**2)
        return distance


    # def calculateDistance(self,point):
    #     distance= math.sqrt((point.y-self.y)**2-(point.x-self.x)**2)
    #     return distance


    #
    # @staticmethod
    # def calculateDistance(point1,point2):
    #     distance= math.sqrt((point2.y-point1.y)**2-(point2.x-point1.x)**2)
    #     return distance

    # reading  1 point from csv file

    @staticmethod
    def createPoint():
        file=open("point.csv","r")
        line=file.readline()
        data=line.split(",")
        point=Point(int(data[0]),int(data[1]))
        return point


# for reading  more than 1 point fron csv file
    @staticmethod
    def createPoints():
        points=[]
        file=open("point.csv","r")
        lines=file.readlines()
        # creating objects from filedata
        for line in lines:
            data=line.split(",")
            point=Point(int(data[0],int(data[1])))
            points.append(point)
        return points

#
#     @classmethod
#     def createPointsAgain(cls):
#         print(cls)
#         print(cls.__dict__)
#         # point=Point(10,20)
#         point=cls(10,20)
#         return point
#
#         point=[]
#         file=open("point.csv","r")
#         lines=file.readlines()
#         for line in lines:
#             data=line.split(",")
#             point=cls(int(data[0],int(data[1])))
#             points.append(point)
#
#         return points


#
# point=Point.createPoint()
# print(point)
# print(point.__dict__)


points=Point.createPoints()
print(points)
# points[0].showPoint()
# points[1].showPoint()
#
# for point in points:
#     point.createPoints()
#
#     print(point)
#     print(point.__dict__)
#
# points=Point.createPointsAgain()
# # print(points)

#
# for point in points:
#
#     point(point.__dict__)


#
pRef1=Point()
pRef2=Point()



pRef1.showPoint()
pRef2.showPoint()

# result=pRef1.calculateDistance(pRef1,pRef2)
# result=pRef1.calculateDistance(pRef2)
# result=Point.calculateDistance(pRef1,pRef2)
# print("the distance is:",result)
