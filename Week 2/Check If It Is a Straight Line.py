class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        # By default answer will be True. So if during the execution any condition is not satisfied, answer is changed to false.    
        answer = True
        
        # If only 2 or 1 coordinates are given then the answer will always be True (on the same line).
        # So we only need to check if there are 3 or more coordinates.
        if len(coordinates) > 2:
            
            # The condition is : for [x1, y1] [x2, y2] value of y2 - y1 / x2 - x1 will be same for all pair.
            
            # Here, denominator will contain x2 - x1 for 1st and 2nd coordinate. We also need to check if its zero for divison by zero exception.
            # If it is equal to 0 then we make it 1 (any random number).
            denominator = (coordinates[1][0] - coordinates[0][0])
            if denominator == 0:
                denominator = 1

            # Numerator contains y2 - y1 for 1st and 2nd coordinate.
            numerator = (coordinates[1][1] - coordinates[0][1])
            
            # check_value is the condition to satisfy. The value for 1st pair should be the value for all the pairs.
            # So we need to compare y2 - y1 / x2 - x1 for all the pairs with check_value.
            check_value = (numerator / denominator)
            
            # Looping through index of coordinates. We need to loop len(coordinates) - 1 because we are considering pairs so we cant take last element.
            for i in range(len(coordinates) - 1):
                
                # Checking the denominator ,i.e., x2 - x1 for cuurent pair for division by zero condition.
                # If it is zero then make it 1 (any random number).
                denom = (coordinates[i+1][0] - coordinates[i][0])
                if denom == 0:
                    denom = 1
                
                # Now check if current pair satisfies the condition. If it does not, then change answer to False.
                if check_value != ((coordinates[i+1][1] - coordinates[i][1]) / denom):
                    
                    answer = False

            # Return the answer.        
            return answer

        # If len(coordinates) <= 2 then return True answer by default.         
        else:
            return answer
                    
                    
                

# The logic used here is : for 3 pairs of coordinates (1st pair - [x1, y1]) (2nd pair [x2, y2]) (3rd pair [x3, y3])
# The value of y2 - y1 / x2 - x1 should be equal to y3 - y2 / x3 - x2.
# So we took initial value of 1st and 2nd pair y2 - y1 / x2 - x1 as check_value.
# For (2nd 3rd) (3rd 4th) (4th 5th) the value should be same as check_value.
