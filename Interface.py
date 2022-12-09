def dept_con(Department):
  if Department == 'sales':
    result = 0
  elif Department == 'accounting':
    result = 1
  elif Department == 'hr':
    result = 2                
  elif Department == 'technical':
    result = 3                             
  elif Department == 'support':
    result = 4                                 
  elif Department == 'management':
    result = 5                                
  elif Department == 'IT':
    result = 6                               
  elif Department == 'product_mng':
    result = 7                               
  elif Department == 'marketing':
    result = 8                             
  elif Department == 'RandD':
    result = 9
  return result

def work_acc(Work_accident):
  if Work_accident == 'no':
    result = 0
  elif Work_accident == 'yes':
    result = 1
  return result

def promote(promotion_last_5years):
  if promotion_last_5years == 'no':
    result = 0
  elif promotion_last_5years == 'yes':
    result = 1
  return result