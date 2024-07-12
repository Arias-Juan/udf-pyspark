def calculate_profit_margin(revenue,profit):
    
    if revenue < profit:
        return '0.00%'
    
    profit_margin_value = (profit / revenue) * 100

    profit_margin = format(profit_margin_value, '.2f') + '%'

    return profit_margin