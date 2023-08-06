import collections
import os
import shutil
import uuid


class PropertyException(Exception):
    pass


class PropertyLine:

    def __init__(self, line):
        self.raw_line = str(line)
        self.key = None
        self.value = None
        self.comment = None
        self.modified = False
        line = self.raw_line.strip()
        if line.find('=') > 0 and not line.startswith('#'):
            # 存放解析的键值对
            strs = line.split('=')
            self.key = strs[0].strip()
            if len(strs) == 2:
                self.value = strs[1].strip()
            else:
                # 存在多个=的情况
                self.value = "=".join(strs[1:]).strip()
        else:
            # 存放注释
            self.key = uuid.uuid4()
            self.comment = line

    def get_value(self):
        return self.value

    def set_value(self, v):
        if self.key and self.value:
            self.value = v
            self.modified = True
        else:
            raise PropertyException("cannot set value to a comment")

    def __str__(self):
        if not self.modified:
            return self.raw_line
        if self.key:
            if self.comment:
                return "{}={} {}".format(self.key, self.value, self.comment)
            else:
                return "{}={}".format(self.key, self.value)
        return ""

    def __repr__(self):
        return self.__str__()


class Properties:
    def __init__(self):
        self.data = collections.OrderedDict()
        self.file_path = None

    def __load(self, iterable):
        for line in iterable:
            pro = PropertyLine(str(line))
            self.data[pro.key] = pro

    def loads(self, text):
        """

        :param text: 加载文本内容:字符串
        :return:
        """
        self.__load(text.split("\n"))

    def dumps(self):
        """

        :return: 读取到的properties文本内容:字符串
        """
        return str(self)

    def read(self, path, encoding="utf-8"):
        """
        读取properties文件
        :param encoding:
        :param path: 文件路径
        :return:
        """
        f = open(path, "r", encoding=encoding)
        self.file_path = path
        r = f.read()
        f.close()
        self.loads(r)
        return self

    def write(self, path=None, encoding="utf-8", bak='.pr_bak'):
        """
        #慎重使用写功能#,先备份源文件(若已存在预期备份文件则不备份),然后将更改的内容写入properties文件
        注意:此操作若人为中断会导致文件变成空文件
        :param bak: 备份后缀名称,通过修改此名称可以多次备份
        :param encoding:
        :param path: 文件路径,默认为 read() 读取的文件
        :return: 将修改后的数据重新写入到文件
        """
        path = self.file_path if path is None else path
        # 首次使用备份文件
        bak_file = path + bak
        if not os.path.exists(bak_file):
            shutil.copyfile(path, bak_file)
        f = open(path, "w", encoding=encoding)
        f.write(self.dumps())
        f.close()

    def __str__(self):
        return "\n".join([str(kk) for kk in self.data.values()])

    # 以下方法，为Properties提供了类似dict的访问方式
    def __delitem__(self, key):
        self.data.__delitem__(key)

    def __getitem__(self, item):
        return self.data[item].value

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].set_value(value)
        else:
            # new property to add
            self.data[key] = PropertyLine("{}={}".format(key, value))

    def __iter__(self):
        for kc in self.data.keys():
            if self.data[kc].value:  # 不是键值对的行不遍历
                yield kc
