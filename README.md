# bayb0pwn
own's pwn library.
Use pwntools with this script.
If it gets huge, it may be packaged.

# addtion list
- for format string attack, automake format function  
  - createFmt32( dest, src, offset, start=0 )  
    |args|description|
    |--|--|
    |dest|overwrite destination address|
    |src|overwrite source address|
    |offset|offset of printf's args |
    |start=0|length of string already output( deafult is 0 )|
    for example:  
      createFmt32( elf.got["atoi"], elf.plt["system"], 7 )

