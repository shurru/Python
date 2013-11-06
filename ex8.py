formatter = "%r,%r,%r,%r" #%r is raw data and can be used to describe any variable whatsoever

print formatter % (1,2,3,4)
print formatter %("one", "two", "three", "four")
print formatter %(True, False, False, True)
print formatter % (formatter, formatter,formatter,formatter)
print formatter%(
" I had this thing", 
"that could type up right",
"but it didn't sing", 
"so i said gnite"
)