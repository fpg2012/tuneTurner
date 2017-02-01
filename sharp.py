
# 升半音

def sharp_note(mynote, sharped):
    '''
    给一个音符升半音
    '''
    if sharped:
        if mynote == '1':
            return '2'
        elif mynote == '2':
            return '3'
        elif mynote == '4':
            return '5'
        elif mynote == '5':
            return '6'
        elif mynote == '6':
            return '7'
        else:
            return '(!)'
    else:
        if mynote == '3':
            return '4'
        elif mynote == '7':
            return '[1]'
        elif mynote == '1' or mynote == '2' or mynote == '4' or mynote == '5' or mynote == '6':
            return '#' + mynote
        else:
            return mynote

def sharp_tune(old_tune):
    '''
    升半音
    '''
    str(old_tune)
    sharping = False
    new_tune = ''
    for i in old_tune:
        if i == '#':
            sharping = True
        else:
            new_tune = new_tune + sharp_note(i, sharping)
            sharping = False
    return new_tune


def sharp_tune_more(old_tune, times):
    '''
    多次升半音
    '''
    for _ in range(times):
        old_tune = sharp_tune(old_tune)
    return old_tune

# print(sharp_tune(input('input:')))
