
# 程序主体

from flat import flat_tune_more
from sharp import sharp_tune_more
from formatIO import formatting

def dotunes():
    '''
    程序主体
    '''
    oldpath = input('输入需要转调的谱子的地址,例如\"F:\\谱子.txt\":')
    newpath = input('输入转调后谱子的路径,默认与原谱位于同一路径:')
    if newpath == '':
        for i in oldpath:
            if i == '.':
                break
            else:
                newpath = newpath + i
        newpath = newpath + '(new).txt'
    mode = input('你想做什么?\n1.升半音\t2.降半音\t3.格式化谱子\n:')
    oldfile = open(oldpath, 'r')
    newfile = open(newpath, 'r+')
    oldtune = oldfile.read()
    if mode == '3':
        newfile.write(formatting(oldtune))
    elif mode == '1':
        times = int(input('升/降几次?:'))
        newfile.write(formatting(sharp_tune_more(oldtune, times)))
    elif mode == '2':
        times = int(input('升/降几次?:'))
        newfile.write(formatting(flat_tune_more(oldtune, times)))
    else:
        return 'error'
    oldfile.close()
    newfile.close()
    return 'done'
print(dotunes())
