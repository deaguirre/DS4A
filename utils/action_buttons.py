def get_button_pressed(buttons):
    """
    Return the id of the button pressed among a list of buttons.

    Args:

        buttons (list)

    Return:

        index
    """
    buttons = [int(button) for button in buttons]
    if(max(buttons) > 0):
        idx = buttons.index(max(buttons))
        
        return idx
    else:
        return False
    