import re

def validate_pattern(word, text):
    """
    Return True if the word is in text.

    Args:
    
        word (string)
        text (string)
    
    Returns:

        bool
    """
    search = re.findall(r'{}*'.format(word), text)
    
    if(len(search) > 0):
        return True
    else:
        return False


