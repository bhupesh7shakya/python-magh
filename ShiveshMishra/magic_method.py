class Player:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __eq__(self,obj):
        return self.weight!=obj.weight  
rohit=Player('rohit',72)
virat=Player('virat',72)
ravindra=Player('ravindra',72)
print(rohit==virat==ravindra)
  


