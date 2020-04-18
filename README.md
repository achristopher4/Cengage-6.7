# Cengage-6.7

Write a recursive function, displayFiles, that expects a pathname as an argument. The path name can be either the name of a file or the name of a directory. If the pathname refers to a file, its filepath is displayed, followed by its contents, like so:

File name: file_path
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit...

Otherwise, if the pathname refers to a directory, the function is applied to each name in the directory, like so:

Directory name: directory_path
File name: file_path1 Lorem ipsum dolor sit amet...
File name: file_path2 Lorem ipsum dolor sit amet...
...
