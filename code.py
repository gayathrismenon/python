class Mentor:
    'common base class'
    typeof = 'l'
    def __init__(self,name):
        self.name = name
   
    def setMentorOrLearner(self):
        val = input("Are you are a mentor? If yes,click Y else N")
        if val == 'Y':
            Mentor.typeof = 'm'
            return Mentor.typeof
           
    def addStacks(self):
        stack=[]
        a = input("Add field of interest or expertise")
        stack.append('a')
       
    def setAvailableTime(self):
        if Mentor.typeof == 'm'
            time = input("set available time please")
   
    def getMentor(self):
       
       
   
emp1 = Mentor("Gayathri")
if emp1.setMentorOrLearner() == 'm':
    emp1.setAvailableTime()
    emp1.addStacks()
     