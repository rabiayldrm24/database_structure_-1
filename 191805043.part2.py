#part2.py

class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None


class SLinkedList:

   def __init__(self):
      self.head = None

   
   def AtBegining(self,newdata):
      NewNode = Node(newdata)
      NewNode.next = self.head
      self.head = NewNode


   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.head is None:
         self.head = NewNode
         return
      laste = self.head
      while(laste.next):
         laste = laste.next
      laste.next=NewNode

   def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return
      NewNode = Node(newdata)
      NewNode.next = middle_node.next
      middle_node.next = NewNode   
    #Function to add node  



   def RemoveNode(self, Removekey):
      HeadVal = self.head
      if (HeadVal is not None):
         if (HeadVal.data == Removekey):
            self.head = HeadVal.next
            HeadVal = None
            return
      else:
         print("e")   
      while (HeadVal is not None):
         if HeadVal.data == Removekey:
            break  
         prev = HeadVal
         HeadVal = HeadVal.next

      if (HeadVal == None):
         print("Movie not found")
         return

      prev.next = HeadVal.next
      HeadVal = None
# Function to remove node


   def LListprint(self):
      printval = self.head
      while (printval):
         print(printval.data),
         printval = printval.next
#print the list


if __name__ == '__main__':
    print("+++++++Welcome+++++++\n")
    llist = SLinkedList()
    while True:
        print("\nAdd a movie : 1\nRemove a movie: 2\nPrint movies: 3\nExit: 4\n")
        inp = input()
        if inp == "4":
           break
        #llist.AtEnd(res)
            #llist.Inbetween(llist.head.next,res)
        elif inp =="1":
            inp0 = int(input("Movie Id: "))
            inp1 = str(input("Movie name : "))
            inp2 = input("Movie Director : ")
            inp3 = input("Movie category : ")
            inp4 = float(input("Movie IMDB rate :"))
            res = str(inp0) + " " + inp1 + " " + inp2 +" " + inp3 +" "+ str(inp4)
            llist.AtBegining(res)

        elif inp == "2":
            inp5 = input("Movie Id, name, director, category, IMDB rate : ")
            llist.RemoveNode(inp5)
        elif inp == "3":
            print("\n")
            llist.LListprint()