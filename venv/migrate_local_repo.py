import os
import shutil

# 缓存目录
gradle_cache_path = os.environ['HOME'] + "/Downloads/files-2.1/"
# maven_path = os.environ['HOME'] + "/.gradle/caches/modules-2/files-2.1/"
# 格式化输出目录
m2_path = os.environ['HOME'] + "/Downloads/temp/release/"

# 需要格式化的包路径
group_ids = [
    "com.mb.gradle.plugin",
    "com.ymm.lib",
    "com.amh.lib",
    "com.mb.lib",
    "com.wlqq.android",
    "com.ymm.lib.widget",
    "com.ymm.biz",
    "com.ymm.common-plugins",
    "com.manbang.android",
    "com.manbang.biz",
    "io.manbang.frontend",
    "io.manbang",
    "io.socket",
    "com.ymm.plugin.aar",
    "com.ymm.biz.module.aar",
    "com.amh.biz",
    "com.github.zyyoona7",
]


# 3.开始拷贝
def start_copy(group_id, source):
    # 1.获取groupId对应的目录
    print(f"源文件路径：{source}")
    split_group_id = group_id.split(".")
    relate_prefix_path = ''
    for split in split_group_id:
        relate_prefix_path += split + "/"

    prefix_path = m2_path + relate_prefix_path
    # print(f"拷贝目录前缀{prefix_path}")

    # 2.获取要拷贝路径后缀
    suffix_path = source.split(group_id)[1]
    length = len(suffix_path.split("/"))
    rm_str = suffix_path.split("/")[length - 2] + "/"
    file_name = suffix_path.split("/")[length - 1]
    real_str = suffix_path.replace(rm_str, "").replace(file_name, "")
    # print(f"原始目录后缀{suffix_path}")
    # print(f"需要移除的目录:{rm_str}")
    # print(f"最终目录后缀:{real_str}")
    # print(f"文件名称:{file_name}")

    # 3.最终目录处理结果
    copy_path = prefix_path + real_str
    exists = os.path.exists(copy_path)
    file_path = copy_path + file_name
    # print(f"需要拷贝最终目录：{copy_path}")
    print(f"拷贝文件路径：{file_path}")
    print(f"目录是否存在{exists}")
    if not exists:
        os.makedirs(copy_path)
    shutil.copy(source, file_path)
    print("")


# 2.找到需要拷贝的文件
def find_copy_files(group_id, root):
    g = os.walk(root)
    for child_path, dir_list, file_list in g:
        for file in file_list:
            start_copy(group_id, os.path.join(child_path, file))
    print("拷贝完成---------")


# 1.遍历指定目录
for path in group_ids:
    real_path = gradle_cache_path + path
    print(f"要遍历的目录:\n{real_path}")
    print("")
    find_copy_files(path, real_path)
