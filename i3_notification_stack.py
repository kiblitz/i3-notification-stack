from sys import argv
from subprocess import call
import pickle

def run(args):
  try:
    stack = open("stack.p", "rb")
    contents = pickle.load(stack)
    if args[0] == "push":
      command = ["command"]
      command.extend(args[1:])
      if contents["stackmode"]:
        contents["stack"].append(command)
      else:
        call(command)
    elif args[0] == "toggle":
      if contents["stackmode"]:
        for command in contents["stack"]:
          call(command)
        contents["stack"] = []
      contents["stackmode"] = not contents["stackmode"]
    stack.close()
    stack = open("stack.p", "wb")
    pickle.dump(contents, stack)
    stack.close() 
  except:
    initStack()

def initStack():
  stack = open("stack.p", "wb")
  contents = {}
  contents["stackmode"] = False
  contents["stack"] = []
  pickle.dump(contents, stack)

run(argv)
