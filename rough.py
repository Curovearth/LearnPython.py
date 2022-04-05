class IntSet(object):
  def __init__(self):
    self.vals = []
  
  def insert(self,e):
    if e not in self.vals:
      self.vals.append(e)
    
  def remove(self,e):
    try:
      self.vals.remove(e)
    except:
      raise ValueError(str(e)+' not found.')

  def member(self,e):
    return e in self.vals

  def getMembers(self):
    return self.vals

  
  def __str__(self):
    self.vals.sort()
    for e in self.vals:
      return e


s = IntSet()

list = [34,21,53,87]

for e in list:
  s.insert(e)

print(s.member(4))
print(s.member(34))
print(s.remove(87))
print(s.insert(22))

print(s.getMembers())

# print(s.remove(3))

  
  