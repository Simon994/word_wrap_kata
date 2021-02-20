class Wrapper:
    @staticmethod
    def wrap(string, column_length):
        # if length of string is <= column_length, simply return string
        if len(string) <= column_length:
            return string
        
        #Between indexes of 0 and column_length+1, find the highest index where there is a space
        #i.e., the breakPoint. If no space found, rfind will return -1
        breakPoint = string.rfind(" ", 0, column_length+1)
        
        # find the length of the next word in the string, after breakPoint
        afterBreak = breakPoint+1
        if " " in string[afterBreak:]:
            next_word_length = string[afterBreak:].find(" ")
        else:
            next_word_length = len(string[afterBreak:])

        if breakPoint == -1 or next_word_length > column_length:
            breakPoint = column_length
        
        # store the line then recursively call wrap,
        # with string sliced from breakPoint to end of string
        line = string[:breakPoint] + "\n"
        remaining_text = string[breakPoint:].strip()
        return line + Wrapper.wrap(remaining_text, column_length)
