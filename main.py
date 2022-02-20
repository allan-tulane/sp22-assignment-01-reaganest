"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if (x <= 1):
     return x
    else:
      ra = (foo(x-1))
      rb = (foo(x-2))
      return ra + rb

def longest_run(mylist, key):
  length = 1
  my_set = set()
  if key not in mylist:
    return 0
  for i, key in enumerate(mylist):
    if i > 0: 
      if key == mylist[i - 1]:
        length += 1
      else:
        my_set.update([length])
        length = 1
  my_set.update([length])
  return max(my_set)


      
  pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
def combination(base1:Result, base2:Result):

  base = Result(0,0,0,'F')
  
  if base1.is_entire_range == 'T' and base2.is_entire_range == 'T':
    base.is_entire_range ='T'
    base.left_size = base2.left_size+ base1.left_size
    base.right_size = base2.right_size+ base1.right_size
    base.longest_size = base2.longest_size+ base1.longest_size

  elif (base1.is_entire_range == 'T' and base2.is_entire_range == 'F'):
    base.is_entire_range ='F'
    base.left_size = base2.left_size + base1.left_size
    base.right_size = base2.right_size +base1.right_size
    base.longest_size = base1.longest_size + base2.longest_size
  elif (base1.is_entire_range == 'F' and base2.is_entire_range == 'T'):
    base.is_entire_range ='F'
    base.left_size = base2.left_size + base1.left_size
    base.right_size = base2.right_size + base1.right_size
    base.longest_size = max(base1.longest_size, base2.longest_size)

  else:  
    base.is_entire_range ='F'
    base.left_size = base2.left_size base1.left_size
    base.right_size = max(base2.right_size, base1.right_size)
    base.longest_size = max(base2.longest_size,base1.longest_size)
    
  return(base)
    
    
def longest_run_recursive(mylist, key):
  middle = len(mylist)//2
  left = mylist[:middle]
  right = mylist[middle:]

  if len(mylist) <= 1:
    if mylist[0] == key:
      base=Result(1,1,1,'T')
      return base
    else:
      base=Result(0,0,0,'F')
      return base
  else:
    base1=longest_run_recursive(left, key)
    base2=longest_run_recursive(right, key)
    bases_combo = combination( base1,base2 )
    return bases_combo
  
 

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


