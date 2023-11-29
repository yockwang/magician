import pymongo
import random

test = [3, 3, 5, 7, 8]

test_delete = 5

# 刪除元素 5
if test_delete in test:
    test.remove(test_delete)

print(test)

