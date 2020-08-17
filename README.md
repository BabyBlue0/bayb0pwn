# bayb0pwn
babyblue0's pwn library.  
This script is used with pwntools.  
If it gets huge, it may be packaged.  

# function list
## createFmt(32|64)( dest, src, offset, start=0 )  
Automatic making the format of FSA.   
|args|description|
|--|--|
|dest|destination address you want to overwrite|
|src|source address you want to overwrite|
|offset|offset of printf's args |
|start=0|length of string already output( deafult is 0 )|
  
e.g.) `createFmt32( elf.got["atoi"], elf.plt["system"], 7 )`  

