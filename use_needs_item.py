def use_needs_item(current_need, max_need, item_number, increase_amount):
    
    

    '''
    message = None
    if item_number <= 0:
        message = "no items"
        return message


    find an effective way to handle zero or less items
    '''
    
    
    current_need += increase_amount
    if current_need > max_need:
        current_need = max_need

    item_number -= 1

    return current_need, item_number


