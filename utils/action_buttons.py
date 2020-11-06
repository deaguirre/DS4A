def get_button_pressed(buttons):
    buttons = [int(button) for button in buttons]
    if(max(buttons) > 0):
        idx = buttons.index(max(buttons))
        
        return idx
    else:
        return False
    