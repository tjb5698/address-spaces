# -*- coding: utf-8 -*-

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
    "2ai32": None,
    "2aii32": None,
    "2aiii32": None,
    "2ai64": None,
    "2aii64": None,
    "2aiii64": None,
    "3ai32": None,
    "3aii32": None,
    "3aiii32": None,
    "3ai64": None,
    "3aii64": None,
    "3aiii64": None,
}

# Comment

###########################################################
# Answer Section
# You may edit the values of variables below
###########################################################

# FILL OUT YOUR ID AND ANSWERS BELOW
# PSU ID (e.g. xyz1234)
ID = "tjb5698"

###########################################################
# (1) Stack, heap, and system calls
###########################################################

# (1.a) What is the size of the proces stack when it is
#   waiting for user input?
#   Enter your answer in bytes.
numerical["1a"] = 86016

# (1.b) Which addresses are for the local variables and
#   which ones are for the dynamically allocated variables?
#   What are the directions in which the stack and the heap
#   grow on your system?
wordy["1b"] = "Address 1 refers to local variables saved in stack while address 2 refers to dynamically allocated variables in heap. STack grows downwards from high to low address while the heap grows upwards from low to high address."

# (1.c.heap) What is the size of the process heap when it
#   is waiting for user input?
#   Enter your answer in bytes.
numerical["1c"] = 135168

# (1.c.stack) What is the size of the process stack when it
#   is waiting for user input?
#   Enter your answer in bytes.
numerical["1cbis"] = 270336

# (1.d) What are the address limits of the stack and the heap?
wordy["1d"] = "heap- 00c1b000 to 00c5d000 ; stack- 7fff39d03000 to 7fff39d18000"

# (1.e) For each unique system call, write in your own words
#   (just one sentence should do) what purpose this system
#   call serves for this program.
wordy["1e"] = "execve, brk, mmap, access, open, fstat, close, read, mprotect, arch.pctrl, munmap, write"

###########################################################
# (2) Debugging Refresher
###########################################################

# (2.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables

# (2.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["2ai32"] = 1691

# (2.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["2aii32"] = 8192

# (2.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["2aiii32"] = 1642496

# (2.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["2ai64"] = 2183

# (2.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["2aii64"] = 8192

# (2.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["2aiii64"] = 3117056

# (2.b) Use gdb to find the program statement that
#   caused the error
wordy["2b"] = "allocate(count-1)"

# (2.c) Explain the cause of this error.
wordy["2c"] = "count variable is outside the stack limits provided by /proc"

# (2.d) Examine individual frames in the stack to find each
#   frame's size. Estimate the number of invocations of the
#   recursive function that should be possible. How many
#   invocations occur when you actually execute the program?
wordy["2d"] = "frame size – 1200048b , stack size limit – 10240kb, should be 10240kb/1200048b invocations, in reality 10"

# (2.e) What are the contents of a frame in general?
#   Which of these are present in a frame corresponding
#   to an invocation of the recursive function and
#   what are their sizes?
wordy["2e"] = "arguments - 0b, return address - 8b, old base pointer - 8b, saved registers - 0b, local variables - 1200012b"

###########################################################
# (3) More debugging
###########################################################

# (3.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables:

# (3.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["3ai32"] = 1984

# (3.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["3aii32"] = 8192

# (3.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["3aiii32"] = 1642496

# (3.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["3ai64"] = 2556

# (3.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["3aii64"] = 8192

# (3.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["3aiii64"] = 6189056

# (3.b) Use valgrind to find the cause of the error
#   including the program statement causing it
wordy["3b"] = "Error occurs during call to memset due to heap overflow."

# (3.c) How is this error different than the one for prog2?
wordy["3c"] = "Error in the last prog was due to stack overflow whereas this is due to heap overflow."

###########################################################
# (4) And some more
###########################################################

# (4.a) Describe the cause and nature of these errors.
#   How would you fix them?
wordy["4a"] = "Valgring shows that the error is due to memory leak. This can be fixed by freeing the malloced memory"

# (4.b) Modify the program to use getrusage for measuring the following:

# (4.b.i) user CPU time used
wordy["4bi"] = "0.889864 s"

# (4.b.ii) system CPU time used
#   What is the difference between (i) and (ii)?
wordy["4bii"] = "0.470928 s" 

# (4.b.iii) maximum resident set size
#   what is this?
wordy["4biii"] = "1814672 kb"

# (4.b.iv) signals received
#   Who may have sent these?
wordy["4biv"] = "0"

# (4.b.v) voluntary context switches
wordy["4bv"] = "3"

# (4.b.vi) involuntary context switches
#   what is the difference between (v) and (vi)?
wordy["4bvi"] = "139"

###########################################################
# Sanity Check
# DO NOT MODIFY ANYTHING BELOW HERE
###########################################################
if ID == "":
    print("Please fill out your student ID in the variable ID")
for key in numerical:
    if type(numerical[key]) is not int:
        print("Type error of answer %s (should be a numerical value)" % key)
for key in wordy:
    if type(wordy[key]) is not str:
        print("Type error of answer %s (should be a string)" % key)
