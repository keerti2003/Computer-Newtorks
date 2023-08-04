
def go_back_n_arq(n, m, Sf, Sn, E1, E2, E3):
    window_size = (2 ** m) - 1

    for _ in range(n):
        if E1 == 1:  
            Sf = Sn
        elif E2 > 0:  
            num_frames_to_send = min(E2, window_size - (Sn - Sf))
            Sn += num_frames_to_send
            E2 -= num_frames_to_send
        elif E3 > 0:  
            Sf = E3
    print("Sf:", Sf, " Sn:", Sn)


n = int(input("Enter number of test cases:"))
inputs = []
for i in range(n):
    inputs.append([n])
    inputs[i].extend(list(map(int, input().split())))
print()

for test_case in inputs:
    go_back_n_arq(*test_case)
