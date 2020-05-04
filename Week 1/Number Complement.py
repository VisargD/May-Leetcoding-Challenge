class Solution:
    def findComplement(self, num: int) -> int:

        # Initializing empty binary and complement string to store binary and complement form of number.
        binary_string = ''
        complement_string = ''

        # Initializing power to zero to calculate the value of complement form at last.
        # Initializing result to zero to add the value of each digit present in complement form.
        number = num
        power = 0
        result = 0

        # Converting to binary form without built-in function.
        while number >= 1:
            binary_string += str(number % 2)
            number = number // 2

            
        # Complementing each digit of binary form by checking if it is zero or one.
        for binary in binary_string:
            if binary == '1':
                complement_string += '0'
            elif binary == '0':
                complement_string += '1'

        # Looping through each digit in complement string and updating result everytime.
        # For example, in 01 :- result = result + (0 * (2 ^ power)) and then increment power and do the same for 1.
        for digit in complement_string:
            result += (int(digit) * pow(2, power))
            power += 1
        
        # Returning the result.
        return result
