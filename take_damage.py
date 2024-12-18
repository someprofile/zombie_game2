def take_damage(current_health, damage, reduction):

    damage -= reduction
    current_health -= damage
    return current_health