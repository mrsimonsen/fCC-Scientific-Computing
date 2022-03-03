def arithmetic_arranger(problems, answers=False):
  arranged_problems = ''
  converted = []
  # problem max length is 5
  if len(problems)>5:
    return "Error: Too many problems."
  
  #problems must have + or -
  for p in problems:
    if ('+' not in p) and ('-' not in p):
      return "Error: Operator must be '+' or '-'."
    data = p.split(' ')
    #operands cannot be more than 4 digits
    if len(data[0])>4 or len(data[2])>4:
        return "Error: Numbers cannot be more than four digits."
    #length of problem (number of -s needed)
    if len(data[0])>len(data[2]):
      max = len(data[0])+2
    else:
      max = len(data[2])+2
    #operands must only contain digits
    try:
      data[0] = int(data[0])
      data[2] = int(data[2])
    except ValueError:
      return "Error: Numbers must only contain digits."
    if data[1]=='-':
      data.append(data[0]-data[2])
    else:
      data.append(data[0]+data[2])
    converted.append(
      (
        f"{data[0]: >{max}}",
        f"{data[1]} {data[2]: >{max-2}}",
        "-"*max,
        f"{data[3]: >{max}}"
      )
    )
  top = ''
  mid = ''
  bot = ''
  ans = ''
  for i in range(len(converted)-1):
    top += converted[i][0]+(" "*4)
    mid += converted[i][1]+(" "*4)
    bot += converted[i][2]+(" "*4)
    ans += converted[i][3]+(" "*4)
  top += converted[-1][0]
  mid += converted[-1][1]
  bot += converted[-1][2]
  ans += converted[-1][3]
  arranged_problems = top+'\n'+mid+'\n'+bot
  if answers:
      arranged_problems += '\n'+ans
  return arranged_problems