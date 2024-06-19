---
layout: page
title: Building Arcade Games with Littlebits
---


### Introduction


### Goals

By the end of this tutorial, you will be able to:
* 
* 
* 

### Materials Required

* 
* 

### Prerequisite lessons
None

### Table of Contents


- [Additional Resources](#additional-resources)
- [Lead Author](#lead-author)
- [Acknowledgements](#acknowledgements)
- [License](#license)

### Integrity
- How do we know that data has not been changed?
- Data could be changed on accident.
- Data could be changed on purpose.
- Integrity is the assurance that the data we have is the same as the data that was sent.


### Integrity of Images
- Imagine we have a 4x4 Black & White Image
  ![]()
- How can we verify this image is displayed as intended?
- We can add a bit in a 5th row/column.
- The 5th row/column should make the number of black bits even.
  ![]()
-Images are not sent as pictures.
- Images are sent as a series of zeros and ones
- Everything is sent as zeros and ones.

  
### Integrity of ISBN
- Before 2007, ISBNs were 10-digit long.
- After that year ISBNs extended to 13 digits. 
- In both ISBN-10 and ISBN-13 standards, the last digit is the check digit, for error detection.
- ISBN-10 check digit is calculated by Modulus 11 with decreasing weights on the first 9 digits.

#### ISBN-10 
1. Example: 0-38549-422-X
- 0×10 + 3×9 + 8×8 + 5×7 + 4×6 + 9×5 + 4×4 + 2×3 + 2×2 + 10×1 = 231
- 231 / 11 = 21 remainder 0.
- This is a valid ISBN

2. Example: 0-060-53348-X
- 0×10 + 0×9 + 6×8 + 0×7 + 5×6 + 3×5 + 3×4 + 4×3 + 8×2 + 10×1 = 48 + 35 + 15 + 12 + 12 + 16 + 10 = 148
- 148 / 11 = 13 remainder 5.
- This is a invalid ISBN

#### ISBN-13
ISBN-13 check digit is calculated by Modulus 10 with alternate weights of 1 and 3 on the first 12 digits.

1. Example: 978-1549304002
- 9×1 + 7×3 + 8×1 + 1×3 + 5×1 + 4×3 + 9×1 + 3×3 + 0×1 + 4×3 + 0×1 + 0×3 + 2×1 =90
- 90 / 10 = 9 remainder 0.
- This is a valid ISB

2. Example: 978-0-80-374107-2
- 9×1 + 7×3 + 8×1 + 0×3 + 8×1 + 0×3 + 3×1 + 7×3 + 4×1 + 1×3 + 0×1 + 7×3 + 2×1 = 9 + 21 + 8 + 0 + 8 + 0 + 3 + 21 + 4 + 3 + 0 + 21 + 2 
- 100 / 10 = 10 remainder 0.
- This is a valid ISBN


### Error Detection
- Some techniques can tell there was a mistake.
- They cannot identify the specific problem.
- What is an example of error detection we saw today?


### Error Correction
- Some techniques can tell there was a mistake AND find the mistake.
- If possible, an algorithm can correct the mistake to re-create the data.
- What is an example of error correction we saw today?


### Binary Numbers
To send information (like images, text, numbers, videos, etc.) we must store all data as Binary numbers

### Image Protocol
- How would you convert an image to binary for the purpose of saving or transmitting?
- A Protocol is a set of rules to define how to expect information.
- What is all the information you would need for a black & white image?
- Would you include error detection/correction?

#### Example Protocol
4-bits for width
4-bits for height
Image data (1 = White, 0 = Black)
Column Parity Bits for Error Checking
0101 (5)
0101 (5)
1010111011111111101110001 (Image Data)
00100 (Column Parity Bits)


### Additional Resources
- [Binary Game](https://tinyurl.com/CyberBinary)

### Lead Author

- Derek Babb

### Acknowledgements

Special thanks to Gul e Fatima Kiani for reviewing and editing this lesson.

### License
[Nebraska GenCyber](https://www.nebraskagencyber.com) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2024  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), [Dr. Deanna House](#),[Derek Babb](https://derekbabb.com/), [Kristeen Shabram](#), [Dr. Lynn Spady](#), and [Gul e Fatima Kiani](#)
