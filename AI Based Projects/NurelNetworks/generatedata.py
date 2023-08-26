def logical_system(input1, input2, input3, input4, input5, input6, input7, input8):
    result1 = input1 and input2
    result2 = input3 or input4
    combined = result1 or result2
    result3 = input5 ^ input6
    combined2 = combined and result3
    result4 = not (input7 and input8)
    combined3 = not (combined2 or result4)
    final = not combined3
    return final

with open("data.csv", "w") as f:
    f.write("input1,input2,input3,input4,input5,input6,input7,input8,target\n")
    for input1 in [0, 1]:
        for input2 in [0, 1]:
            for input3 in [0, 1]:
                for input4 in [0, 1]:
                    for input5 in [0, 1]:
                        for input6 in [0, 1]:
                            for input7 in [0, 1]:
                                for input8 in [0, 1]:
                                    target = logical_system(input1, input2, input3, input4, input5, input6, input7, input8)
                                    if target:
                                        target = 1
                                    else:
                                        target = 0
                                    f.write(f"{input1},{input2},{input3},{input4},{input5},{input6},{input7},{input8},{target}\n")

print("Truth table saved to 'data.csv'.")
