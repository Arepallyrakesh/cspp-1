# def clean_given_text(text_input):
#     words = text_input.lower().strip().replace('\'', '')
#     regex = re.compile('[^a-z]')
#     words = regex.sub(" ", words).split(" ")
#     return words

no_of_lines = 5
lines = ""
for i in range(5):
    lines += input() + "\n"

print (lines)

	input1 = int(input())
	out_str = ""
	for i in range(input1):
		input_str = str(intput())
		out_str += input_str + "\n"
	return out_str
	

	lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)