def read_q(file_name):
    file = open(file_name, "r")
    lines=file.readlines()
    my_questions = []
    current_questions = None
    for line in lines:
        sign=line[0]
        if sign==">":
            if current_questions is not None:
                my_questions.append(current_questions)
            current_questions = {
                'answers': [],
                'question': '',
                'ok': ''
            }
            current_questions['question']=line[1:-1]
            # current_questions['question']=current_questions['question'][:-1]
        elif sign in ("-", '*'):
            current_questions['answers'].append(line[1:-1])
            if sign=="*":
                current_questions['ok'] = line[1]
    file.close()
    return my_questions

def display_text(questions):
    text_questions = "Answer the question: "
    for row in questions:
        print(row.get('question'))
        for answer in row.get('answers'):
            print(answer)
        answer_ = input(text_questions)
        while answer_ != row.get('ok'):
            print('zla')
            answer_ = input(text_questions)
        else:
            print('prawidlowa')

questions_ = read_q("questions.txt")
display=display_text(questions_)





