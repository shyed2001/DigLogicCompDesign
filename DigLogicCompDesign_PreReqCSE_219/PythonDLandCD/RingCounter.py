# import matplotlib.pyplot as plt

# def ring_counter():
#     states = ['000', '001', '010', '100', '101', '110']
#     outputs = ['000', '001', '010', '100', '101', '110']
    
#     # Plotting the counter
#     fig, ax = plt.subplots()
#     ax.set_title('3-Bit Ring Counter')
#     ax.axis('off')
#     ax.table(cellText=[list(state) for state in states],
#              colLabels=['Q2', 'Q1', 'Q0'],
#              cellLoc='center',
#              loc='center')
#     plt.show()
    
#     # Displaying the truth table
#     print("3-Bit Ring Counter Truth Table")
#     print("==============================")
#     print("State  |  Q2  |  Q1  |  Q0")
#     print("---------------------------")
    
#     for i in range(len(states)):
#         state = states[i]
#         output = outputs[i]
#         q2, q1, q0 = state[0], state[1], state[2]
#         print(f" {state}   |   {q2}   |   {q1}   |   {q0}")
    
#     print("==============================")

# ring_counter()

import matplotlib.pyplot as plt

def draw_ring_counter(num_bits):
    states = [format(i, '0{}b'.format(num_bits)) for i in range(2**num_bits)]
    outputs = states.copy()

    # Plotting the counter circuit diagram
    fig, ax = plt.subplots()
    ax.set_title(f'{num_bits}-Bit Ring Counter')
    ax.axis('off')
    ax.table(cellText=[list(state) for state in states],
             colLabels=[f'Q{i}' for i in range(num_bits)],
             cellLoc='center',
             loc='center')
    plt.show()

    # Displaying the truth table
    print(f'{num_bits}-Bit Ring Counter Truth Table')
    print('=' * (5 + num_bits * 7))
    print('State  |', end=' ')
    for i in range(num_bits):
        print(f' Q{i}  |', end=' ')
    print('\n' + '-' * (7 * (num_bits + 1)))
    
    for i in range(len(states)):
        state = states[i]
        output = outputs[i]
        state_values = '  |  '.join(list(state))
        print(f' {state}   |  {state_values}  ')
    
    print('=' * (5 + num_bits * 7))

# Getting user input for the number of bits
num_bits = int(input('Enter the number of bits (1,2, 3, 4,5, or 6): '))
draw_ring_counter(num_bits)


