# fmt: off
from paradox.lib.utils import memoized

ROUNDS = 14

xtimetbl = (
    0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e,
    0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e,
    0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e,
    0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e,
    0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e,
    0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e,
    0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e,
    0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e,
    0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e,
    0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e,
    0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae,
    0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe,
    0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce,
    0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde,
    0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee,
    0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe,
    0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15,
    0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05,
    0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35,
    0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25,
    0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55,
    0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45,
    0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75,
    0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65,
    0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95,
    0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85,
    0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5,
    0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5,
    0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5,
    0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5,
    0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5,
    0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5
)

Logtable = (0x00, 0x00, 0x19, 0x01, 0x32, 0x02, 0x1a, 0xc6,
            0x4b, 0xc7, 0x1b, 0x68, 0x33, 0xee, 0xdf, 0x03,
            0x64, 0x04, 0xe0, 0x0e, 0x34, 0x8d, 0x81, 0xef,
            0x4c, 0x71, 0x08, 0xc8, 0xf8, 0x69, 0x1c, 0xc1,
            0x7d, 0xc2, 0x1d, 0xb5, 0xf9, 0xb9, 0x27, 0x6a,
            0x4d, 0xe4, 0xa6, 0x72, 0x9a, 0xc9, 0x09, 0x78,
            0x65, 0x2f, 0x8a, 0x05, 0x21, 0x0f, 0xe1, 0x24,
            0x12, 0xf0, 0x82, 0x45, 0x35, 0x93, 0xda, 0x8e,
            0x96, 0x8f, 0xdb, 0xbd, 0x36, 0xd0, 0xce, 0x94,
            0x13, 0x5c, 0xd2, 0xf1, 0x40, 0x46, 0x83, 0x38,
            0x66, 0xdd, 0xfd, 0x30, 0xbf, 0x06, 0x8b, 0x62,
            0xb3, 0x25, 0xe2, 0x98, 0x22, 0x88, 0x91, 0x10,
            0x7e, 0x6e, 0x48, 0xc3, 0xa3, 0xb6, 0x1e, 0x42,
            0x3a, 0x6b, 0x28, 0x54, 0xfa, 0x85, 0x3d, 0xba,
            0x2b, 0x79, 0x0a, 0x15, 0x9b, 0x9f, 0x5e, 0xca,
            0x4e, 0xd4, 0xac, 0xe5, 0xf3, 0x73, 0xa7, 0x57,
            0xaf, 0x58, 0xa8, 0x50, 0xf4, 0xea, 0xd6, 0x74,
            0x4f, 0xae, 0xe9, 0xd5, 0xe7, 0xe6, 0xad, 0xe8,
            0x2c, 0xd7, 0x75, 0x7a, 0xeb, 0x16, 0x0b, 0xf5,
            0x59, 0xcb, 0x5f, 0xb0, 0x9c, 0xa9, 0x51, 0xa0,
            0x7f, 0x0c, 0xf6, 0x6f, 0x17, 0xc4, 0x49, 0xec,
            0xd8, 0x43, 0x1f, 0x2d, 0xa4, 0x76, 0x7b, 0xb7,
            0xcc, 0xbb, 0x3e, 0x5a, 0xfb, 0x60, 0xb1, 0x86,
            0x3b, 0x52, 0xa1, 0x6c, 0xaa, 0x55, 0x29, 0x9d,
            0x97, 0xb2, 0x87, 0x90, 0x61, 0xbe, 0xdc, 0xfc,
            0xbc, 0x95, 0xcf, 0xcd, 0x37, 0x3f, 0x5b, 0xd1,
            0x53, 0x39, 0x84, 0x3c, 0x41, 0xa2, 0x6d, 0x47,
            0x14, 0x2a, 0x9e, 0x5d, 0x56, 0xf2, 0xd3, 0xab,
            0x44, 0x11, 0x92, 0xd9, 0x23, 0x20, 0x2e, 0x89,
            0xb4, 0x7c, 0xb8, 0x26, 0x77, 0x99, 0xe3, 0xa5,
            0x67, 0x4a, 0xed, 0xde, 0xc5, 0x31, 0xfe, 0x18,
            0x0d, 0x63, 0x8c, 0x80, 0xc0, 0xf7, 0x70, 0x07)

Alogtable = (0x01, 0x03, 0x05, 0x0f, 0x11, 0x33, 0x55, 0xff,
             0x1a, 0x2e, 0x72, 0x96, 0xa1, 0xf8, 0x13, 0x35,
             0x5f, 0xe1, 0x38, 0x48, 0xd8, 0x73, 0x95, 0xa4,
             0xf7, 0x02, 0x06, 0x0a, 0x1e, 0x22, 0x66, 0xaa,
             0xe5, 0x34, 0x5c, 0xe4, 0x37, 0x59, 0xeb, 0x26,
             0x6a, 0xbe, 0xd9, 0x70, 0x90, 0xab, 0xe6, 0x31,
             0x53, 0xf5, 0x04, 0x0c, 0x14, 0x3c, 0x44, 0xcc,
             0x4f, 0xd1, 0x68, 0xb8, 0xd3, 0x6e, 0xb2, 0xcd,
             0x4c, 0xd4, 0x67, 0xa9, 0xe0, 0x3b, 0x4d, 0xd7,
             0x62, 0xa6, 0xf1, 0x08, 0x18, 0x28, 0x78, 0x88,
             0x83, 0x9e, 0xb9, 0xd0, 0x6b, 0xbd, 0xdc, 0x7f,
             0x81, 0x98, 0xb3, 0xce, 0x49, 0xdb, 0x76, 0x9a,
             0xb5, 0xc4, 0x57, 0xf9, 0x10, 0x30, 0x50, 0xf0,
             0x0b, 0x1d, 0x27, 0x69, 0xbb, 0xd6, 0x61, 0xa3,
             0xfe, 0x19, 0x2b, 0x7d, 0x87, 0x92, 0xad, 0xec,
             0x2f, 0x71, 0x93, 0xae, 0xe9, 0x20, 0x60, 0xa0,
             0xfb, 0x16, 0x3a, 0x4e, 0xd2, 0x6d, 0xb7, 0xc2,
             0x5d, 0xe7, 0x32, 0x56, 0xfa, 0x15, 0x3f, 0x41,
             0xc3, 0x5e, 0xe2, 0x3d, 0x47, 0xc9, 0x40, 0xc0,
             0x5b, 0xed, 0x2c, 0x74, 0x9c, 0xbf, 0xda, 0x75,
             0x9f, 0xba, 0xd5, 0x64, 0xac, 0xef, 0x2a, 0x7e,
             0x82, 0x9d, 0xbc, 0xdf, 0x7a, 0x8e, 0x89, 0x80,
             0x9b, 0xb6, 0xc1, 0x58, 0xe8, 0x23, 0x65, 0xaf,
             0xea, 0x25, 0x6f, 0xb1, 0xc8, 0x43, 0xc5, 0x54,
             0xfc, 0x1f, 0x21, 0x63, 0xa5, 0xf4, 0x07, 0x09,
             0x1b, 0x2d, 0x77, 0x99, 0xb0, 0xcb, 0x46, 0xca,
             0x45, 0xcf, 0x4a, 0xde, 0x79, 0x8b, 0x86, 0x91,
             0xa8, 0xe3, 0x3e, 0x42, 0xc6, 0x51, 0xf3, 0x0e,
             0x12, 0x36, 0x5a, 0xee, 0x29, 0x7b, 0x8d, 0x8c,
             0x8f, 0x8a, 0x85, 0x94, 0xa7, 0xf2, 0x0d, 0x17,
             0x39, 0x4b, 0xdd, 0x7c, 0x84, 0x97, 0xa2, 0xfd,
             0x1c, 0x24, 0x6c, 0xb4, 0xc7, 0x52, 0xf6, 0x01)

S = (0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
     0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
     0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
     0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
     0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
     0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
     0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
     0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
     0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
     0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
     0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
     0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
     0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
     0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
     0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
     0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
     0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
     0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
     0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
     0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
     0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
     0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
     0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
     0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
     0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
     0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
     0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
     0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
     0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
     0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
     0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
     0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16)

Si = (0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38,
      0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
      0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
      0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
      0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d,
      0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
      0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2,
      0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
      0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
      0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
      0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
      0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
      0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a,
      0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
      0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
      0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
      0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea,
      0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
      0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85,
      0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
      0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
      0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
      0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20,
      0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
      0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31,
      0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
      0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
      0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
      0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0,
      0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
      0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26,
      0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d)

iG = ((0x0E, 0x09, 0x0D, 0x0B),
      (0x0B, 0x0E, 0x09, 0x0D),
      (0x0D, 0x0B, 0x0E, 0x09),
      (0x09, 0x0D, 0x0B, 0x0E))

rcon = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 
        0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
        0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 
        0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4,
        0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91)

# Shifts
s0 = 0
s1 = 1
s2 = 2
s3 = 3

# Inv Shifts
is0 = 0
is1 = 3
is2 = 2
is3 = 1

# LT fixed lookups
lt_e = Logtable[0xE]
lt_b = Logtable[0xB]
lt_d = Logtable[0xD]
lt_9 = Logtable[0x9]

@memoized
def keygen(k):
    rk = [0] * 240
    
    if len(k) % 32:
        k += b'\xee' * (32 - (len(k) % 32))

    temp = [0, 0, 0, 0]

    i = 0
    while i < 4:
        j = 0
        while j < 4:
            rk[j * 4 + i] = k[i * 4 + j]
            j += 1
        j = 0
        while j < 4:
            rk[j * 4 + i + 16] = k[i * 4 + j + 16]
            j += 1
        i += 1

    i = 8
    while i < 60:
        j = 0
        while j < 4:
            temp[j] = rk[(((i - 1) & 0xFC) << 2) + ((i - 1) & 0x03) + j * 4]
            j += 1
        if i % 8 == 0:
            j = 0
            while j < 4:
                temp[j] = S[temp[j]]
                j += 1
            tmp = temp[0]

            j = 1
            while j < 4:
                temp[j - 1] = temp[j]
                j += 1

            temp[3] = tmp
            temp[0] ^= rcon[int(i / 8 - 1)]

        elif i % 8 == 4:
            j = 0
            while j < 4:
                temp[j] = S[temp[j]]
                j += 1

        j = 0
        while j < 4:
            rk[((i & 0xFC) << 2) + (i & 0x03) + j * 4] = (
                rk[(((i - 8) & 0xFC) << 2) + ((i - 8) & 0x03) + j * 4] ^ temp[j]
            )
            j += 1
        i += 1

    return rk
    
def encrypt(ctxt, key):
    dtxt = []

    ctxt = list(ctxt)

    if len(ctxt) % 16 != 0:
        ctxt.extend([0xee] * (16 - (len(ctxt) % 16)))
    
    rk = keygen(key)

    blocks = len(ctxt) // 16

    extend = dtxt.extend
    for i in range(blocks):
        a = ctxt[i * 16 : (i + 1) * 16]
        a = (a[0]  ^ rk[0],
             a[1]  ^ rk[1],
             a[2]  ^ rk[2],
             a[3]  ^ rk[3],
             a[4]  ^ rk[4],
             a[5]  ^ rk[5],
             a[6]  ^ rk[6],
             a[7]  ^ rk[7],
             a[8]  ^ rk[8],
             a[9]  ^ rk[9],
             a[10] ^ rk[10],
             a[11] ^ rk[11],
             a[12] ^ rk[12],
             a[13] ^ rk[13],
             a[14] ^ rk[14],
             a[15] ^ rk[15])

        for r in range(1, ROUNDS):
            r16 = r * 16

            # S BOX
            a = (S[a[0]],  S[a[1]],  S[a[2]],  S[a[3]], 
                 S[a[4]],  S[a[5]],  S[a[6]],  S[a[7]],
                 S[a[8]],  S[a[9]],  S[a[10]], S[a[11]],
                 S[a[12]], S[a[13]], S[a[14]], S[a[15]])

            # Shift Row
            a = (a[0],  a[1],  a[2],  a[3],
                 a[5],  a[6],  a[7],  a[4],
                 a[10], a[11], a[8],  a[9],
                 a[15], a[12], a[13], a[14])

            # Mix Column
            tmp0 = a[0] ^ a[4] ^ a[8]  ^ a[12]
            tmp1 = a[1] ^ a[5] ^ a[9]  ^ a[13]
            tmp2 = a[2] ^ a[6] ^ a[10] ^ a[14]
            tmp3 = a[3] ^ a[7] ^ a[11] ^ a[15]

            a = (a[0]  ^ (xtimetbl[a[0]  ^ a[4]]  ^ tmp0),
                 a[1]  ^ (xtimetbl[a[1]  ^ a[5]]  ^ tmp1),
                 a[2]  ^ (xtimetbl[a[2]  ^ a[6]]  ^ tmp2),
                 a[3]  ^ (xtimetbl[a[3]  ^ a[7]]  ^ tmp3),
                 a[4]  ^ (xtimetbl[a[4]  ^ a[8]]  ^ tmp0),
                 a[5]  ^ (xtimetbl[a[5]  ^ a[9]]  ^ tmp1),
                 a[6]  ^ (xtimetbl[a[6]  ^ a[10]] ^ tmp2),
                 a[7]  ^ (xtimetbl[a[7]  ^ a[11]] ^ tmp3),
                 a[8]  ^ (xtimetbl[a[8]  ^ a[12]] ^ tmp0),
                 a[9]  ^ (xtimetbl[a[9]  ^ a[13]] ^ tmp1),
                 a[10] ^ (xtimetbl[a[10] ^ a[14]] ^ tmp2),
                 a[11] ^ (xtimetbl[a[11] ^ a[15]] ^ tmp3),
                 a[12] ^ (xtimetbl[a[12] ^ a[0]]  ^ tmp0),
                 a[13] ^ (xtimetbl[a[13] ^ a[1]]  ^ tmp1),
                 a[14] ^ (xtimetbl[a[14] ^ a[2]]  ^ tmp2),
                 a[15] ^ (xtimetbl[a[15] ^ a[3]]  ^ tmp3))

            # Key Addition
            a = (a[0]  ^ rk[r16],
                 a[1]  ^ rk[1  + r16],
                 a[2]  ^ rk[2  + r16],
                 a[3]  ^ rk[3  + r16],
                 a[4]  ^ rk[4  + r16],
                 a[5]  ^ rk[5  + r16],
                 a[6]  ^ rk[6  + r16],
                 a[7]  ^ rk[7  + r16],
                 a[8]  ^ rk[8  + r16],
                 a[9]  ^ rk[9  + r16],
                 a[10] ^ rk[10 + r16],
                 a[11] ^ rk[11 + r16],
                 a[12] ^ rk[12 + r16],
                 a[13] ^ rk[13 + r16],
                 a[14] ^ rk[14 + r16],
                 a[15] ^ rk[15 + r16])

            r += 1

        # S BOX
        a = (S[a[0]],  S[a[1]],  S[a[2]],  S[a[3]], 
             S[a[4]],  S[a[5]],  S[a[6]],  S[a[7]],
             S[a[8]],  S[a[9]],  S[a[10]], S[a[11]],
             S[a[12]], S[a[13]], S[a[14]], S[a[15]])

        # Shift Row
        a = (a[0],  a[1],  a[2],  a[3],
             a[5],  a[6],  a[7],  a[4],
             a[10], a[11], a[8],  a[9],
             a[15], a[12], a[13], a[14])
        
        # Key addition
        a = (a[0]  ^ rk[224],
             a[1]  ^ rk[225],
             a[2]  ^ rk[226],
             a[3]  ^ rk[227],
             a[4]  ^ rk[228],
             a[5]  ^ rk[229],
             a[6]  ^ rk[230],
             a[7]  ^ rk[231],
             a[8]  ^ rk[232],
             a[9]  ^ rk[233],
             a[10] ^ rk[234],
             a[11] ^ rk[235],
             a[12] ^ rk[236],
             a[13] ^ rk[237],
             a[14] ^ rk[238],
             a[15] ^ rk[239])

        extend(a)

    return bytes(dtxt)

def decrypt(ctxt, key):
    dtxt = []

    rk = keygen(key)

    ctxt = list(ctxt)
    
    blocks = len(ctxt) // 16

    extend = dtxt.extend

    for i in range(blocks):
        a = ctxt[i * 16 : (i + 1) * 16]

        # Key Addition
        a = (a[0] ^ rk[224],
            a[1]  ^ rk[225],
            a[2]  ^ rk[226],
            a[3]  ^ rk[227],
            a[4]  ^ rk[228],
            a[5]  ^ rk[229],
            a[6]  ^ rk[230],
            a[7]  ^ rk[231],
            a[8]  ^ rk[232],
            a[9]  ^ rk[233],
            a[10] ^ rk[234],
            a[11] ^ rk[235],
            a[12] ^ rk[236],
            a[13] ^ rk[237],
            a[14] ^ rk[238],
            a[15] ^ rk[239])
      
        # Si Box
        a = (Si[a[0]],  Si[a[1]],  Si[a[2]],  Si[a[3]], 
             Si[a[4]],  Si[a[5]],  Si[a[6]],  Si[a[7]],
             Si[a[8]],  Si[a[9]],  Si[a[10]], Si[a[11]],
             Si[a[12]], Si[a[13]], Si[a[14]], Si[a[15]])

        # Shift Row Invert
        a = (a[0],  a[1],  a[2],  a[3], 
             a[7],  a[4],  a[5],  a[6], 
             a[10], a[11], a[8],  a[9], 
             a[13], a[14], a[15], a[12])

        for r in range(13, 0, -1):
            r16 = r * 16
            
            # Key Addition
            a = (a[0] ^ rk[r16],
                    a[1]  ^ rk[1  + r16],
                    a[2]  ^ rk[2  + r16],
                    a[3]  ^ rk[3  + r16],
                    a[4]  ^ rk[4  + r16],
                    a[5]  ^ rk[5  + r16],
                    a[6]  ^ rk[6  + r16],
                    a[7]  ^ rk[7  + r16],
                    a[8]  ^ rk[8  + r16],
                    a[9]  ^ rk[9  + r16],
                    a[10] ^ rk[10 + r16],
                    a[11] ^ rk[11 + r16],
                    a[12] ^ rk[12 + r16],
                    a[13] ^ rk[13 + r16],
                    a[14] ^ rk[14 + r16],
                    a[15] ^ rk[15 + r16])

            # Inv Mix Column
            a = (
                (Alogtable[(lt_e + Logtable[a[0]])  % 255] if a[0]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[4]])  % 255] if a[4]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[8]])  % 255] if a[8]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[12]]) % 255] if a[12] else 0),
                (Alogtable[(lt_e + Logtable[a[1]])  % 255] if a[1]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[5]])  % 255] if a[5]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[9]])  % 255] if a[9]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[13]]) % 255] if a[13] else 0),
                (Alogtable[(lt_e + Logtable[a[2]])  % 255] if a[2]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[6]])  % 255] if a[6]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[10]]) % 255] if a[10] else 0) ^
                (Alogtable[(lt_9 + Logtable[a[14]]) % 255] if a[14] else 0),
                (Alogtable[(lt_e + Logtable[a[3]])  % 255] if a[3]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[7]])  % 255] if a[7]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[11]]) % 255] if a[11] else 0) ^
                (Alogtable[(lt_9 + Logtable[a[15]]) % 255] if a[15] else 0),
                (Alogtable[(lt_e + Logtable[a[4]])  % 255] if a[4]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[8]])  % 255] if a[8]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[12]]) % 255] if a[12] else 0) ^
                (Alogtable[(lt_9 + Logtable[a[0]])  % 255] if a[0]  else 0),
                (Alogtable[(lt_e + Logtable[a[5]])  % 255] if a[5]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[9]])  % 255] if a[9]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[13]]) % 255] if a[13] else 0) ^
                (Alogtable[(lt_9 + Logtable[a[1]])  % 255] if a[1]  else 0),
                (Alogtable[(lt_e + Logtable[a[6]])  % 255] if a[6]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[10]]) % 255] if a[10] else 0) ^
                (Alogtable[(lt_d + Logtable[a[14]]) % 255] if a[14] else 0) ^
                (Alogtable[(lt_9 + Logtable[a[2]])  % 255] if a[2]  else 0),
                (Alogtable[(lt_e + Logtable[a[7]])  % 255] if a[7]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[11]]) % 255] if a[11] else 0) ^
                (Alogtable[(lt_d + Logtable[a[15]]) % 255] if a[15] else 0) ^
                (Alogtable[(lt_9 + Logtable[a[3]])  % 255] if a[3]  else 0),
                (Alogtable[(lt_e + Logtable[a[8]])  % 255] if a[8]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[12]]) % 255] if a[12] else 0) ^
                (Alogtable[(lt_d + Logtable[a[0]])  % 255] if a[0]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[4]])  % 255] if a[4]  else 0),
                (Alogtable[(lt_e + Logtable[a[9]])  % 255] if a[9]  else 0) ^
                (Alogtable[(lt_b + Logtable[a[13]]) % 255] if a[13] else 0) ^
                (Alogtable[(lt_d + Logtable[a[1]])  % 255] if a[1]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[5]])  % 255] if a[5]  else 0),
                (Alogtable[(lt_e + Logtable[a[10]]) % 255] if a[10] else 0) ^
                (Alogtable[(lt_b + Logtable[a[14]]) % 255] if a[14] else 0) ^
                (Alogtable[(lt_d + Logtable[a[2]])  % 255] if a[2]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[6]])  % 255] if a[6]  else 0),
                (Alogtable[(lt_e + Logtable[a[11]]) % 255] if a[11] else 0) ^
                (Alogtable[(lt_b + Logtable[a[15]]) % 255] if a[15] else 0) ^
                (Alogtable[(lt_d + Logtable[a[3]])  % 255] if a[3]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[7]])  % 255] if a[7]  else 0),
                (Alogtable[(lt_e + Logtable[a[12]]) % 255] if a[12] else 0) ^
                (Alogtable[(lt_b + Logtable[a[0]])  % 255] if a[0]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[4]])  % 255] if a[4]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[8]])  % 255] if a[8]  else 0),
                (Alogtable[(lt_e + Logtable[a[13]]) % 255] if a[13] else 0) ^
                (Alogtable[(lt_b + Logtable[a[1]])  % 255] if a[1]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[5]])  % 255] if a[5]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[9]])  % 255] if a[9]  else 0),
                (Alogtable[(lt_e + Logtable[a[14]]) % 255] if a[14] else 0) ^
                (Alogtable[(lt_b + Logtable[a[2]])  % 255] if a[2]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[6]])  % 255] if a[6]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[10]]) % 255] if a[10] else 0),
                (Alogtable[(lt_e + Logtable[a[15]]) % 255] if a[15] else 0) ^
                (Alogtable[(lt_b + Logtable[a[3]])  % 255] if a[3]  else 0) ^
                (Alogtable[(lt_d + Logtable[a[7]])  % 255] if a[7]  else 0) ^
                (Alogtable[(lt_9 + Logtable[a[11]]) % 255] if a[11] else 0))

            # Si Box
            a = (Si[a[0]],  Si[a[1]],  Si[a[2]],  Si[a[3]], 
                 Si[a[4]],  Si[a[5]],  Si[a[6]],  Si[a[7]],
                 Si[a[8]],  Si[a[9]],  Si[a[10]], Si[a[11]],
                 Si[a[12]], Si[a[13]], Si[a[14]], Si[a[15]])

            # Shift Row Invert
            a = (a[0],  a[1],  a[2],  a[3], 
                 a[7],  a[4],  a[5],  a[6], 
                 a[10], a[11], a[8],  a[9], 
                 a[13], a[14], a[15], a[12])


        # Key addition
        a = (a[0]  ^ rk[0],  a[1]  ^ rk[1],  a[2]  ^ rk[2],
             a[3]  ^ rk[3],  a[4]  ^ rk[4],  a[5]  ^ rk[5],
             a[6]  ^ rk[6],  a[7]  ^ rk[7],  a[8]  ^ rk[8],
             a[9]  ^ rk[9],  a[10] ^ rk[10], a[11] ^ rk[11],
             a[12] ^ rk[12], a[13] ^ rk[13], a[14] ^ rk[14],
             a[15] ^ rk[15])

        extend(a)

    return bytes(dtxt)
