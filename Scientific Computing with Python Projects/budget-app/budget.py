class Category:
  def __init__(self, name):
	self.name = name
	self.ledger = []
	self.__balance = 0

  def __str__(self):
	stars = (30-len(self.name))//2
	stars *= '*'
	rep = f"{stars}{self.name}{stars}\n"
	for i in self.ledger:
	  rep += f"{i['description'][:23]:<23}"
	  rep += f"{i['amount']:7.2f}"
	  rep += "\n"
	rep += f"Total: {self.__balance:.2f}"
	return rep

  def get_balance(self):
	return self.__balance

  def check_funds(self, amount):
	if amount > self.__balance:
	  return False
	else:
	  return True
  
  def deposit(self, amount, description=''):
	self.__balance += amount
	self.ledger.append({"amount":amount, "description":description})

  def withdraw(self, amount, description=''):
	if self.check_funds(amount) > 0:
	  self.__balance -= amount
	  self.ledger.append({"amount": -amount, "description":description})
	  return True
	else:
	  return False

  def transfer(self, amount, other):
	if self.check_funds(amount):
	  self.ledger.append({"amount":-amount, "description":f"Transfer to {other.name}"})
	  self.__balance -= amount
	  other.__balance += amount
	  other.ledger.append({"amount":amount, "description":f"Transfer from {self.name}"})
	  return True
	else:
	  return False


def create_spend_chart(categories):
  total = 0
  max = 0
  cat_spend = {}
  #category spending totals and longest name
  for cat in categories:
	cat_spend[cat.name] = 0
	if len(cat.name)>max:
	  max = len(cat.name)
	for i in cat.ledger:
	  if i['amount']<0:
		total += i['amount']
		cat_spend[cat.name] += i['amount']
  #create the y axis headers
  rows = []
  for i in range(100,-1,-10):
	rows.append(f"{i: >3}|")
  cols = len(categories) * 3
  #calculate number of o's 
  for cat in cat_spend.keys():
	temp = cat_spend[cat] / total * 100
	temp -= (temp%10)
	temp /= 10
	temp = int(temp)+1
	for i in range(11):
	  if temp > 0:
		temp -= 1
		s = " o "
	  else:
		s = "   "
	  rows[10-i] += s
  #seperating x axis bar
  rows.append((" "*4)+("-"*(cols+1)))
  names = []
  #format and create x axis header
  for i in range(len(categories)):
	names.append(f"{categories[i].name: <{max}}")
  bot = []
  for i in range(max):
	bot.append(" "*4)
  for name in names:
	for i in range(max):
	  bot[i] += f" {name[i]} "
  #create output string
  out = "Percentage spent by category\n"
  rows += bot
  for i in rows:
	if "-" in i:
	  out+= i+"\n"
	else:
	  out += i+' \n'
  
  out = out[:-1]
  return out
	  
	