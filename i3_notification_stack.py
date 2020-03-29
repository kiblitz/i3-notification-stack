from sys import argv
from subprocess import call

num_args = len(argv)
call(["notify-send", argv[0]])
