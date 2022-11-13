count_c = 0
count_n = 0
count_o = 0
c_true = False
n_true = False
o_true = False
secret_command = False
char = input()
word = ""
completed_words = ""

while char != "End":

    # caps 65 to 90, lower 97 to 122
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        if char == "c" or char == "o" or char == "n":
            if char == "c":
                count_c += 1
                if count_c == 1:
                    pass
                elif count_c == 2:
                    word += char
                else:
                    word += char

            elif char == "o":
                count_o += 1
                if count_o == 1:
                    pass
                elif count_o == 2:
                    word += char
                else:
                    word += char

            elif char == "n":
                count_n += 1
                if count_n == 1:
                    pass
                elif count_n == 2:
                    word += char
                else:
                    word += char

        else:  # if char != "c" and char != "o" and char != "n":
            word += char

        if count_c > 0 and count_n > 0 and count_o > 0:
            word += " "
            completed_words += word
            word = ""
            count_o = 0
            count_c = 0
            count_n = 0


    else:
        pass

    char = input()

if char == "End":
    print(completed_words)
