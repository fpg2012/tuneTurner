
# 将输入输出格式化例如:(xxxx) -> (x)(x)(x)(x), ([x]) -> x, [xxxx] ->[x][x][x][x]

def formatting(old_tune):
    '''
    格式化
    '''
    new_tune = ''
    sharped = False
    low = high = 0
    for i in old_tune:
        if i == '(':
            low = low + 1
        elif i == '[':
            high = high + 1
        elif i == ']':
            high = high - 1
        elif i == ')':
            low = low - 1
        elif i == '#':
            sharped = True
            if low == high:
                new_tune = new_tune + i
            elif low > high:
                new_tune = new_tune + '(' * (low - high) + i
            elif low < high:
                new_tune = new_tune + '[' * (high - low) + i
            else:
                return 'error'
        else:
            if sharped:
                if low == high:
                    new_tune = new_tune + i
                elif low > high:
                    new_tune = new_tune + i + ')' * (low - high)
                elif low < high:
                    new_tune = new_tune + i + ']' * (low - high)
                else:
                    return 'error'
                sharped = False
            else:
                if low == high:
                    new_tune = new_tune + i
                elif low > high:
                    new_tune = new_tune + '(' * (low - high) + i + ')' * (low - high)
                elif low < high:
                    new_tune = new_tune + '[' * (high - low) + i + ']' * (low - high)
                else:
                    return 'error'
    print(new_tune)
    return new_tune
