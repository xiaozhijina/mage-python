import argparse
import stat
from pathlib import Path
from datetime import datetime


parser = argparse.ArgumentParser(prog='ls',add_help=False,description='list directory contents')
parser.add_argument('path',nargs='?',default='.',help='path help')
parser.add_argument('-l',dest='long',action='store_true',help='use a long listing format')
parser.add_argument('-a','--all',action='store_true',help='show all files,do not ignore entires starting with .')
parser.add_argument('-h','--human-readable',action='store_true',help='with -l,print sizes in \
                    human readable format ')

def listdir(path,all=False,detail=False,human=False):
    def _getfiletype(f:Path):
        if f.is_dir():
            return 'd'
        elif f.is_block_device():
            return 'b'
        elif f.is_char_device():
            return 'c'
        elif f.is_socket():
            return 's'
        elif f.is_symlink():
            return 'l'
        elif f.is_fifo():
            return  'p'
        else:
            return '-'

# def convert_mode(mode:int):
#     modelist = ['r','w','x','r','w','x','r','w','x']
#     modestr = bin(mode)[-9:]  #'110110100'
#     ret = ""
#     for i,c in enumerate(modestr):
#         if c == '1':
#             ret += modelist[i]
#         else:
#             ret += '-'
#     return ret

    modelist = dict(zip(range(9),['r','w','x','r','w','x','r','w','x']))
    def _getmodestr(mode:int):
        m = mode & 0o777
        mstr = ''
        for i in range(8,-1,-1):
            if m >> i & 1:
                mstr += modelist[8-i]
            else:
                mstr += '-'
        return mstr

# def bytes2human(n):
#     symbols = ['K','M','G','T','P']
#     prefix = {}
#     for i,s in enumerate(symbols):
#         prefix[s] = 1 << (i + 1) * 10
#     for s in reversed(symbols):
#         if n >= prefix[s]:
#             value = float(n) / prefix[s]
#             return '{.1f}{}'.format(value,s)
#         return "{}B".format(n)
# print(bytes2human(100000))

    def _gethuman(size:int):
        units = ['','K','M','G','T','P']
        depth = 0
        while size >=1000:
            size = size // 1000
            depth += 1
        return '{}{}'.format(size,units[depth])

    def _listdir(path,all=False,detail=False,human=False):
        """详细列出本目录"""
        p = Path(path)
        for i in p.iterdir():
            if not all and i.name.startswith('.'):   #不显示隐藏文件
                continue
            if not detail:
                yield (i.name,)
            else:
                st = i.stat()
    #            t = _getfiletype(p)
    #            mode = oct(stat.st_mode)[-3:]
    #            mode = _getfiletype(p) + _getmodestr(stat.st_mode)  ##采用自己编写的判断文件类型与mode
                mode = stat.filemode(st.st_mode)     #采用stat模块实现
                actime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                size = str(st.st_size) if  not human else _gethuman(st.st_size)
                yield (mode,st.st_nlink,st.st_gid,st.st_uid,actime,size,i.name)

    #排序
    yield from sorted(_listdir(path,all,detail,human),key=lambda x:x[len(x) - 1])

if __name__ == '__main__':
    args = parser.parse_args(('-l','-a','-h'))    #分析参数，同时传入可迭代的参数
    print(args)
#    parser.print_help()
#    print(args.all)
#    print(args.human_readable)
    files = listdir(args.path,args.all,args.long,args.human_readable)
    for i in files:
        print(i)

