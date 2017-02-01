
# 降半音

def flat_note(mynote, sharped):
    '''
    给一个音符降半音
    '''
    if not sharped:
        if mynote == '1':
            return '(7)'
        elif mynote == '2':
            return '#1'
        elif mynote == '3':
            return '#2'
        elif mynote == '4':
            return '3'
        elif mynote == '5':
            return '#4'
        elif mynote == '6':
            return '#5'
        elif mynote == '7':
            return '#6'
        else:
            return mynote
    else:
        return mynote


def flat_tune(old_tune):
    '''
    降半音
    '''
    str(old_tune)
    flatting = False
    new_tune = ''
    for i in old_tune:
        if i == '#':
            flatting = True
        else:
            new_tune = new_tune + flat_note(i, flatting)
            flatting = False
    return new_tune


def flat_tune_more(old_tune, times):
    '''
    多次降半音
    '''
    for _ in range(times):
        old_tune = flat_tune(old_tune)
    return old_tune

# print(flat_tune(input('input:')))
