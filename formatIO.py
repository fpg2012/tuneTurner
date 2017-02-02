
# 将输入输出格式化例如:(xxxx) -> (x)(x)(x)(x), ([x]) -> x, [xxxx] ->[x][x][x][x]
# 数字谱的注释放在尖括号'<'和'>'之间, 中间的内容连同尖括号本身都会被忽略

def formatting(old_tune):
    '''
    格式化谱子
    '''
    new_tune = ''
    others = sharped = False
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
        elif i == '<':
            new_tune = new_tune + i
            others = True
        elif i == '>':
            new_tune = new_tune + i
            others = False
        elif i == '#':
            sharped = True
            if low == high or others:
                new_tune = new_tune + i
            elif low > high:
                new_tune = new_tune + '(' * (low - high) + i
            elif low < high:
                new_tune = new_tune + '[' * (high - low) + i
            else:
                return 'error'
        else:
            if sharped:
                if low == high or others:
                    new_tune = new_tune + i
                elif low > high:
                    new_tune = new_tune + i + ')' * (low - high)
                elif low < high:
                    new_tune = new_tune + i + ']' * (high - low)
                else:
                    return 'error'
                sharped = False
            else:
                if low == high or others:
                    new_tune = new_tune + i
                elif low > high:
                    new_tune = new_tune + '(' * (low - high) + i + ')' * (low - high)
                elif low < high:
                    new_tune = new_tune + '[' * (high - low) + i + ']' * (high - low)
                else:
                    return 'error'
    print(new_tune)
    return new_tune
