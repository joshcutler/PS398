class Athlete(object):
  
  def __init__(self, name, height, weight, number):
    self.name = name
    self.height = height
    self.weight = weight
    self.number = number  
  
  def endorse(self):
    return "I endorse things"
        
class BaseballPlayer(Athlete):
  
  def set_batting_average(self, average):
    self.batting_average = average
  
  def get_batting_average(self):
    return self.batting_average
    
  def set_AL(self, al):
    self.AL = al
    
  def endorse(self):
    return "I " + str(self.name) + " endorse Rawlings"
    
class FootballPlayer(Athlete):
  
  def set_special_teams(self, sp_teams):
    self.special_teams = sp_teams
  
  def get_special_teams(self):
    return self.special_teams
    
  def endorse(self):
    return "I strongly " + str(self.name) + " endorse Football things"