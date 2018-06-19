import sys,os,importlib

# Use a shortcut to refer to the query source and the output files
#  to make it easier to manage multiple queries.
#query_src = 'HammondB3'
query_shortcut = sys.argv[1]

# The rest of the query filename follows a standard format.
filename =  'query_' + query_shortcut + '.py'
directory = '.'

# Perform a case insensitive search for the query file name.
# (The case sensitivity in Python with respect to filenames is a bit of beat down.
# This is the only way I could find to work around it.)
def find_sensitive_path(dir, insensitive_path):

    insensitive_path = insensitive_path.strip(os.path.sep)

    parts = insensitive_path.split(os.path.sep)
    next_name = parts[0]
    for name in os.listdir(dir):
        if next_name.lower() == name.lower():
            improved_path = os.path.join(dir, name)
            if len(parts) == 1:
                return improved_path
            else:
                return find_sensitive_path(improved_path, os.path.sep.join(parts[1:]))
    return None
    
improved_fullpath = find_sensitive_path(directory, filename)
#print ('Improved filename', improved_fullpath)
(head,tail) = os.path.split(improved_fullpath)
#print ('head', head)
#print ('tail', tail)
(root,ext) = os.path.splitext(tail)
#print ('root', root)
#print ('ext', ext)

# Import query from query source file
query_src = importlib.import_module(root)
