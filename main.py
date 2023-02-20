# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

count_name1 = (lower_case_name1.count("t") + lower_case_name1.count("r") + lower_case_name1.count("u") + lower_case_name1.count("e") + lower_case_name2.count("t") + lower_case_name2.count("r") + lower_case_name2.count("u") + lower_case_name2.count("e"))
count_name2 = (lower_case_name1.count("l") + lower_case_name1.count("o") + lower_case_name1.count("v") + lower_case_name1.count("e") + lower_case_name2.count("l") + lower_case_name2.count("o") + lower_case_name2.count("v") + lower_case_name2.count("e"))
count_name1_str = str(count_name1)
count_name2_str = str(count_name2)
love_score = count_name1_str + count_name2_str
love_score_as_int = int(love_score)
if love_score_as_int < 10 or love_score_as_int > 90:
    print(f"Your score is {love_score_as_int}, you go together like coke and mentos.")
elif love_score_as_int >= 40 and love_score_as_int <= 50:
    print(f"Your score is {love_score_as_int}, you are alright together.")
else:
    print(f"Your score is {love_score_as_int}")














#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:45]
    for x in f2:
      file.write("    " + x)


import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print):
    with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer=['David Beckham', 'Victoria Beckham'], expected_print='Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n')

  def test_2(self):
    self.run_test(given_answer=['Han Solo', 'Princess Leia Organa'], expected_print='Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n')

  def test_3(self):
    self.run_test(given_answer=['Pierre Curie', 'Marie Curie'], expected_print='Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n')

  def test_4(self):
    self.run_test(given_answer=['Mark Antony', 'Cleopatra'], expected_print='Welcome to the Love Calculator!\nYour score is 54.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n')
print('Your score is 43, you are alright together.\n')
print('\nRunning some tests on your code with different name combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
