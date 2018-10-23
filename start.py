import pytablewriter
import encrypt
import time
import generateFiles

filesSizes = [1, 10, 100]

print('Setting up Test')
generateFiles.gen(filesSizes)

times = encrypt.testEncrypt("test", filesSizes)


f = open("test.md", "w")
writer = pytablewriter.MarkdownTableWriter()
writer.table_name = "example_table"
writer.header_list = ["int", "float", "str", "bool", "mix", "time"]
writer.value_matrix = [
    [0,   0.1,      "hoge", True,   0,      "2017-01-01 03:04:05+0900"],
    [2,   "-2.23",  "foo",  False,  None,   "2017-12-23 45:01:23+0900"],
    [3,   0,        "bar",  "true",  "inf", "2017-03-03 33:44:55+0900"],
    [-10, -9.9,     "",     "FALSE", "nan", "2017-01-01 00:00:00+0900"],
]

f.write(writer.write_table())
f.close()

print(f'{times[1]-times[0]:.5f} seconds')
