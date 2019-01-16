# This is the answers file for the CMPSC 473 - Spring 2019 - Project #1 
# Answers data structures
# DO NOT MODIFY THESE VARIABLES HERE
wordy = {
    "1b": None,
    "1d": None,
    "1e": None,
    "2b": None,
    "2c": None,
    "2d": None,
    "2e": None,
    "3b": None,
    "3c": None,
    "4a": None,
    "4bi": None,
    "4bii": None,
    "4biii": None,
    "4biv": None,
    "4bv": None,
    "4bvi": None
}
numerical = {
    "1a": None,
    "1c": None,
    "1cbis": None,
    "2ai": None,
    "2aii": None,
    "2aiii": None,
    "3ai": None,
    "3aii": None,
    "3aiii": None,
}

# FILL OUT YOUR ID AND ANSWERS BELOW
# PSU ID (e.g. xyz1234)
ID = ""

# 1. Stack, heap, and system calls:
# (a) What is the size of the process stack when it is waiting for user input?
numerical["1a"] = None

# (b) Which addresses are for the local variables and which ones are for the dynamically allocated variables? What are the directions in which the stack and the heap grow on your system?
wordy["1b"] = None

# (c) What is the size of the process heap when it is waiting for user input?
numerical["1c"] = None

# (cbis) What is the size of the process stack?
numerical["1cbis"] = None

# (d) What are the address limits of the stack and the heap?
wordy["1d"] = None

# (e) For each unique system call, write in your own words (just one sentence should do) what purpose this system call serves for this program.
wordy["1e"] = None

# 2. Debugging refresher:
# (a) Observe and report the differences in the following for the 32 bit and 64 bit executables:
# (i) size of compiled code:
numerical["2ai"] = None

# (ii) size of code during run time
numerical["2aii"] = None

# (iii) size of linked libraries
numerical["2aiii"] = None

# (b) Use gdb to find the program statement that caused the error
wordy["2b"] = None

# (c) Explain the cause of this error.
wordy["2c"] = None

# (d) Examine individual frames in the stack to find each frame’s size. Estimate the number of invocations of the recursive function that should be possible. How many invocations occur when you actually execute the program?
wordy["2d"] = None

# (e) What are the contents of a frame in general? Which of these are present in a frame corresponding to an invocation of the recursive function and what are their sizes?
wordy["2e"] = None

# (3) More debugging
# (a) Observe and report the differences in the following for the 32 bit and 64 bit executables:
# (i) size of compiled code, 
numerical["3ai"] = None

# (ii) size of code during run time, 
numerical["3aii"] = None

# (iii) size of linked libraries
numerical["3aiii"] = None

# (b) Use valgrind to find the cause of the error including the program statement causing it
wordy["3b"] = None

# (c) How is this error different than the one for prog2?
wordy["2c"] = None

# (4) And some more:
# (a) Describe the cause and nature of these errors. How would you fix them?
wordy["4a"] = None

# (b) Modify the program to use getrusage for measuring the following:
# (i) user CPU time used, 
wordy["4bi"] = None

# (ii) system CPU time used - what is the difference between (i) and (ii)?, 
wordy["4bii"] = None

# (iii) maximum resident set size - what is this?, 
wordy["4biii"] = None

# (iv) signals received - who may have sent these?, 
wordy["4biv"] = None

# (v) voluntary context switches, 
wordy["4bv"] = None

# (vi) involuntary context switches - what is the difference between (v) and (vi)?
wordy["4bvi"] = None


# Sanity Check
# DO NOT MODIFY ANYTHING BELOW HERE
if ID == "":
    print("Please fill out your student ID in the variable ID")
for key in numerical:
    if type(numerical[key]) is not int:
        print("Type error of answer %s (should be a numerical value)" % key)
for key in wordy:
    if type(wordy[key]) is not str:
        print("Type error or answer %s (should be a string)" % key)
