# Probtobuf example with python

Protobuf範例 與 Json檔轉換



## Install

-  step 1
```
pip install protobuf
brew install protobuf
```
-  step 2
定義protobuf 資料格式
```
vim APHDC.proto
```

-  step 3
編譯成python檔：APHDC_pb2.py, 或是可以直接複製此檔 跳過step1
```
sh compile.sh
```

## Quick test
```
python pdData.py
```


Reference:
https://blog.gtwang.org/programming/python-protocol-buffers-tutorial/
實作可以參考 easy_test file