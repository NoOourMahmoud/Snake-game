import sys
import cx_Freeze

executables = [cx_Freeze.Executable("snakeTutorial.py")]

cx_Freeze.setup(
	name = "Snake" ,
	options = {"build_exe":{"packages":["pygame"], "include_files":["apple.png", "icon.png", "snakehead.png"]}},
	discription = "Snake Game Tutorial" ,
	executables = executables
	)
