foo = "A B C D"
bar = "E-F-G-H"

# the split() function will return a list
foo_list = foo.split()
# if you give no arguments, it will separate by whitespaces by default
# ["A", "B", "C", "D"]

bar_list = bar.split("-", 3)
# you can specify the maximum amount of elements the split() function will output
# ["E", "F", "G"]