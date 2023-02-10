import shutil, os, sys
repo_path = os.path.abspath('./repo')
print(f"-----repo_path:{repo_path}")
prefixs = []
for arg in sys.argv:
    args = arg.split('=')
    if len(args) == 2:
        if args[0] == 'repo':
            repo_path = os.path.abspath(args[1])
        if args[0] == 'prefix':
            prefixs = args[1].split(',')

def isNeedCopy(dir_name):
    for prefix in prefixs:
        if dir_name.startswith(prefix):
            return True
    return False
temp_path = os.path.join(os.path.abspath(os.path.dirname(repo_path)),'temp')
if os.path.exists(temp_path):
    shutil.rmtree(temp_path)
os.mkdir(temp_path)
arch_paths = []
for dir_name in os.listdir(repo_path):
    if(isNeedCopy(dir_name)):
        path = os.path.join(repo_path, dir_name)
        arch_paths.append(path)
for arch_path in arch_paths:
    g = os.walk(arch_path)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            if file_name != '.DS_Store':
                paths = path.removeprefix(repo_path+'/').split('/')
                paths.pop()
                paths[:1] = paths[0].split('.')
                copy_path = os.path.join(temp_path,'/'.join(paths))
                if not os.path.exists(copy_path):
                    os.makedirs(copy_path)
                shutil.copy(os.path.join(path, file_name),copy_path)