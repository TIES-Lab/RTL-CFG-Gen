import os
import re

# tst_strng = "3'b011, 3'b101:"
# pattern0 = re.compile(r"([A-Za-z0-9_.', ]+)\s?(:)\s?([A-Za-z0-9_.', ]+)\s?(\[[A-Za-z0-9_.:', ]+\])?\s?(<?=)\s?([A-Za-z0-9_.', ]+)\s?(\[[A-Za-z0-9_.:', ]+\])?;")
# pattern1 = re.compile(r"([A-Za-z0-9_.', ]+)\s?(:)")
#
# a = re.search(pattern0, tst_strng)
# a_groups = [x for x in list(re.findall(pattern0, tst_strng)[0]) if x != '']
#
# b = re.search(pattern1, tst_strng)
# b_groups = [x for x in list(re.findall(pattern1, tst_strng)[0]) if x != '']
# print(b)
# print(_groups)

# with open('memory_control.sv', 'r') as fl:
#     txt_fl = fl.read()
#
# # print([txt_fl])
# pattern_block = re.compile(r"/\*(\*(?!/)|[^*]+)*\*/")
# findall_lst = re.findall(pattern_block, txt_fl)
# # lst = [txt_fl]
# # print('Full Text: \n', lst)
#
# # print(findall_lst)
#
# for all in findall_lst:
#     print('\n yo: ====================================================================================================================\n')
#     print(all)

root_loc: str = 'D:/DAC_ext'
RTL_loc: str = 'SoC_1/All_RTL/'
property_fl_name: str = "spec.txt"
property_fl_loc: str = os.path.join(root_loc, property_fl_name)
srch_rtl: str = os.path.join(root_loc, RTL_loc)
CFG_loc: str = 'Extracted_CFG'
Dest_loc: str = os.path.join(root_loc, CFG_loc)


accpt_frmts = ['.v', '.sv']
file_lst = [x for x in os.listdir(srch_rtl) if os.path.splitext(x)[-1] in accpt_frmts]
curr_lvl: int = 1
tree = {}
curr_lvl_str: str = str(curr_lvl)
tree[curr_lvl_str] = []

for iter_file in file_lst:
    # if iter_file == "memory_control.sv":
    #     continue
    file_path: str = os.path.join(srch_rtl, iter_file)
    with open(file_path, "r") as fl:
        lines = fl.readlines()
        fl.close()
    for iter_line in lines:
        if "multicore" in re.split(r"[() ]", re.sub(r"[\n\t]+", "", iter_line)):
            tree[curr_lvl_str].append(iter_file)
            break
#
# tree["second"] = []
# for iter_name in tree[curr_lvl_str]:
#     iter_name = os.path.splitext(iter_name)[0]
#     for iter_file in file_lst:
#         if os.path.splitext(iter_file)[0] == iter_name:
#             continue
#         file_name = os.path.splitext(iter_file)[0]
#         # print(file_name)
#         file_path: str = os.path.join(srch_rtl, iter_file)
#         with open(file_path, "r") as fl:
#             lines = fl.readlines()
#             fl.close()
#         for iter_line in lines:
#             if file_name in re.split(r"[() ]", re.sub(r"[\n\t]+", "", iter_line)):
#                 tree["second"].append(iter_file)
#                 break
print(tree)