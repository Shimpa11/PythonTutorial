# process is an application or running program . each process has at least one thread  called main thread
# thread is a saperate  unit of execution  in process
import requests
import threading

"""class PrintingTask:
    def printDocument(self,name,copies):
        for i in range(1,copies+1):
            print("Printing{}| copy {}".format(name,i))
            """

# IS-A Relationship -> PrintingTask IS-A Thread

class fetchNewsTask(threading.Thread):
    def run(self):
            url="http://newsapi.org/v2/everything?q=bitcoin&from=2020-01-17&sortBy=publishedAt&apiKey=31c21508fad64116acd229c10ac11e84"
            response=requests.get(url)
            print(response.text)

class PrintingTask(threading.Thread):


    """def __init__(self,name,copies):
         threading.Thread.__init__(self)#execute parent's init
         self.name=name
         self.copies=copies
         """


    def addPrintingDetails(self,name,copies):
        self.name=name
        self.copies=copies


    # override method

    def run(self):
        for i in  range(1,self.copies+1):
            print("Printing{} Copy#{}".format(self.name,i))

def main():

         print("App Started")
         task=PrintingTask()
         task.addPrintingDetails("Learning Python.pdf",10)
         # task.printDocument("Learning Python.pdf",10)

         newsTask=fetchNewsTask()
         newsTask.start()
         task.start()

         for i in range(1,11):
             print("i is: ",i)
         print("App Finished")

print(threading.active_count())
print(threading.current_thread())
print(threading.enumerate())
if __name__=="__main__":
     main()
