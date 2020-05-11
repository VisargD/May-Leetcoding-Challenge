class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        # Initializing start color to the color or image[sr][sc]
        start_color = image[sr][sc]

        # NOTE: This is a very important step.
        # If the start color and new color are equal then return the image list as it is.
        if newColor == start_color:
            return image
        
        # Recursive DFS function.
        def dfs(image_list, row, col, start_col, new_col):
            
            # Checking if the current color is equal to the start color. If no, then return.
            if image_list[row][col] != start_col:
                return
            
            # If the start and current color are equal then change the color to new color.
            image_list[row][col] = new_col
            
            # If the current row is last one then dont increment the row as it will result in index out of bound.
            if row != len(image_list) - 1:
                dfs(image_list, row + 1, col, start_col, new_col)

            # If the current is the first one then dont decrement the row as it will result in index out of bound.
            if row != 0:
                dfs(image_list, row - 1, col, start_col, new_col)

            # If the column is the last one then dont increment it as it will result in index out of bound. 
            if col != len(image_list[0]) - 1:
                dfs(image_list, row, col + 1, start_col, new_col)
            
            # If the column is the first one then dont decrement it as it will result in index out of bound.
            if col != 0:
                dfs(image_list, row, col - 1, start_col, new_col)
            
            
        # Call the recursive function.    
        dfs(image, sr, sc, start_color, newColor)
        
        # Return the final image.
        return image


