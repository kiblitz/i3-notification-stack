from sys import argv
from subprocess import call
from os.path import dirname, abspath, exists
import pickle

def run(args):
  stack_file = dirname(abspath(__file__)) + "/stack.p"
  if not exists(stack_file):
    initStack(stack_file)
  stack = open(stack_file, "rb")
  contents = pickle.load(stack)
  if args[1] == "push":
    if contents["stackmode"]:
      contents["stack"].append(args[2:])
    else:
      command = ["notify-send"]
      command.extend(args[2:])
      call(command)
  elif args[1] == "toggle":
    if contents["stackmode"]:
      for elem in contents["stack"]:
        command = ["notify-send"]
        command.extend(elem)
        call(command)
      contents["stack"] = []
    contents["stackmode"] = not contents["stackmode"]
  stack.close()
  stack = open(stack_file, "wb")
  pickle.dump(contents, stack)
  stack.close() 

def initStack(stack_file):
  stack = open(stack_file, "wb")
  contents = {}
  contents["stackmode"] = False
  contents["stack"] = []
  pickle.dump(contents, stack)

run(argv)
