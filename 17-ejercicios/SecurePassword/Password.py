import random
class Password:
  __password = ''
  __validAsciiCodes = []

  def __init__(self):
    self.__validAsciiCodes = self.__setAsciiValidCodes()

  def set(self,password):
    self.__password = password

  def get(self):
    return self.__password

  def setSecurePassword(self):
    passwordList = [] 
    countChars = len(self.__validAsciiCodes) - 1
    for number in range(0,5):
      passwordList.append(chr(self.__validAsciiCodes[random.randint(0,countChars)]))
    
    passwordList.extend(self.__appendStrictRules())
    random.shuffle(passwordList)
    self.__password = self.__password.join(passwordList)

  def __appendStrictRules(self):
    strictRules = []
    strictRules.append(str(random.randint(0,9)))
    strictRules.append(chr(random.randint(36,45)))
    strictRules.append(chr(random.randint(97,122)).upper())
    return strictRules

  def __setAsciiValidCodes(self):
    return list(range(48,57)) + list(range(97,122))