import xlrd
import xlsxwriter


def get_webinfo(path):
    web_info = {}
    config = open(path)
    for line in config:
        result = [ele.strip() for ele in line.split('=')]
        web_info.update(dict([result]))
    return web_info


def get_userinfo(path):
    account_info = []
    config = open(path)
    for r in config:
        account_dict = {}
        result = [ele.strip() for ele in r.split(' ')]
        for info in result:
            account = [ele.strip() for ele in info.split('=')]
            account_dict.update(dict([account]))
        account_info.append(account_dict)

    # print(account_info)
    return account_info


class xlUserinfo(object):
    def __init__(self, path=''):
        self.xl = xlrd.open_workbook(path)

    def floattostr(self, val):
        if isinstance(val, float):
            val = str(int(val))
        return val

    def get_sheet_info(self):
        listkey = ['uname', 'pwd']
        infolist = []
        for row in range(1, self.sheet.nrows):
            info = [self.floattostr(val) for val in self.sheet.row_values(row)]
            tmp = zip(listkey, info)
            infolist.append(dict(tmp))
        return infolist

    def get_sheetinfo_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()


if __name__ == '__main__':
    # ele_dict = get_webinfo(r'webinfo.txt')
    # for key  in info:
    #     print(key,info[key])

    # user_list = get_userinfo(r'usrinfo.txt')
    # for l in userinfo:
    #     print(l)
    # print(userinfo)

    xinfo = xlUserinfo(r'userinfo.xls')
    info = xinfo.get_sheetinfo_by_index(0)
    print(info)
    # info = xinfo.get_sheetinfo_by_name('Sheet1')
    # print(info)
