class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = list()

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})

  def withdraw(self, amount, description=''):
    # I think the description of the check_funds method is wrong.
    if not self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description': description})
      return True

    return False

  def get_balance(self):
    balance = 0
    for element in self.ledger:
      balance += element['amount']

    return balance

  def transfer(self, amount, category):
    if not self.check_funds(amount):
      self.withdraw(amount, 'Transfer to ' + category.category)
      category.deposit(amount, 'Transfer from ' + self.category)
      return True

    return False

  def check_funds(self, amount):
    # I think the description of the check_funds method is wrong.
    return False if amount < self.get_balance() else True

  def __str__(self):
    title = self.category.center(30, '*') + '\n'
    items = ''

    for item in self.ledger:
      desc = item['description'][:23]
      amount = '{:.2f}'.format(float(item['amount']))
      items += '{:<23s}{:>7s}'.format(desc, amount) + '\n'

    return title + items + 'Total: ' + str(self.get_balance())


def create_spend_chart(categories):
  title = 'Percentage spent by category\n'
  print(len(title))
  rows = ''
  names = ''
  spentByCategory = list()
  spent = 0
  totalSpent = 0

  # Get amount spent by category and total amount spent  
  for category in categories:
    for element in category.ledger:
      if element['amount'] < 0:
        spent += element['amount']

    spentByCategory.append(-spent)
    totalSpent += -spent
    spent = 0

  # Get percentage spent by category
  percentages = [round(sbc * 100 / totalSpent) for sbc in spentByCategory]

  # Draw bar char rows
  for percentLabel in range(100, -10 , -10):
    rows += '{:3d}|'.format(percentLabel)
    for percentage in percentages:      
      if percentage >= percentLabel:
        rows += ' o '
      else:
        rows += ' ' * 3
    rows += ' \n'

  # Draw dashes
  dashes = (' ' * 4) + (('-' * 3) * len(percentages)) + '-\n'

  # Draw category name
  maxLength = max(len(category.category) for category in categories)
  for x in range(maxLength):
    names += ' ' * 4
    for category in categories:
      if x < len(category.category):
          names += ' ' + category.category[x] + ' '
      else:
          names += ' ' * 3
    if x != maxLength -1:
      names += ' \n'
  
  names += ' '

  return title + rows + dashes + names