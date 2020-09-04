def arithmetic_arranger(problems, display=False):

  # Check Error: Too many problems.
  if len(problems) > 5:
    return 'Error: Too many problems.'

  operators = ['+', '-']
  firstLine = ''
  secondLine = ''
  dashes = ''
  results = ''
  offset = ' ' * 4

  for problem in problems:
    [first, op, second] = problem.split()

    # Check Error: Operator must be '+' or '-'.
    if op not in operators:
      return 'Error: Operator must be \'+\' or \'-\'.'

    # Check Error: Numbers must only contain digits.
    try:
      int(first)
      int(second)
    except:
      return "Error: Numbers must only contain digits."

    # Check Error: Numbers cannot be more than four digits.
    if len(first) > 4 or len(second) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Chech if answers should be displayed
    if display:
      if op == '+':
        result = int(first) + int(second)
      else:
        result = int(first) - int(second)

    """
    - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
    - Numbers should be right-aligned.
    - There should be four spaces between each problem.
    - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.
    """
    if len(first) > len(second):
      firstLine += (' ' * 2) + first + offset
      secondLine += op + (' ' * (1 + len(first) - len(second))) + second + offset
      dashes += ('-' * (2 + len(first))) + offset
      if display:
        results += str(result).rjust(2 + len(first)) + offset
    elif len(second) > len(first):
      firstLine += (' ' * (2 + len(second) - len(first))) + first + offset
      secondLine += op + ' ' + second + offset
      dashes += ('-' * (2 + len(second))) + offset
      if display:
        results += str(result).rjust(2 + len(second)) + offset
    else:
      firstLine += (' ' * 2) + first + offset
      secondLine += op + ' ' + second + offset
      dashes += ('-' * (2 + len(first))) + offset
      if display:
        results += str(result).rjust(2 + len(first)) + offset

  arranged_problems = firstLine.rstrip() + '\n' + secondLine.rstrip() + '\n' + dashes.rstrip()

  if display:
    arranged_problems += '\n' + results.rstrip()

  return arranged_problems