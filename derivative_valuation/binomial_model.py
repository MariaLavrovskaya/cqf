import numpy as np
s0 = 100
mu = 0.1
sigma = 0.2

expiry = 12
number_of_steps = 5
int_rate = 0.1
dt = 1/12

strike = 100

discount_factor = np.exp(-int_rate * dt)

up = 1 + sigma * np.sqrt(dt)
down = 1 - sigma * np.sqrt(dt)

p = 0.5 + ((mu * np.sqrt(dt)) / (2* sigma))

stock_prices = np.zeros([number_of_steps, number_of_steps])
option_price = np.zeros([number_of_steps, number_of_steps])
stock_prices[0,0] = 100
for time_index in range(1,number_of_steps):
    stock_prices[:time_index, time_index] = np.dot(stock_prices[:time_index, time_index - 1],up)
    stock_prices[time_index, time_index] = np.dot(stock_prices[time_index -1, time_index - 1], down)

option_price = np.where(stock_prices - strike > 0, stock_prices - strike, 0)
# for time_back in range(number_of_steps-2, -1,  -1):
#     print(time_back)
#     for index_option in range(time_back):
#         print(index_option)
#         option_price[index_option, time_back] = ((p * option_price[index_option, time_back+1]) + ((1-p) * option_price[index_option +1, time_back+1])) * discount_factor

        
for time_back in range(number_of_steps-1, -1,  -1):
    print(time_back)
    for index_option in range(time_back):
        print(index_option)
        option_price[index_option, time_back-1] = ((p * option_price[index_option, time_back]) + ((1-p) * option_price[index_option +1, time_back])) * discount_factor