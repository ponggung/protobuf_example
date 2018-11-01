import addressbook_pb2
import sys

# 指定 Protocol Buffer 資料檔
my_pb_file = "my_addr_book.pb"

# 建立 AddressBook
address_book = addressbook_pb2.AddressBook()

# 增加一筆 Person 資料
person = address_book.people.add()

# 設定 Person 基本資料
person.id = 666
person.name = "P. K. Wang"
person.email = "ponggung1986@gmail.com"

# 新增第一筆電話
phone_number = person.phones.add()
phone_number.number = "0912-345678"
phone_number.type = addressbook_pb2.Person.MOBILE

# 新增第二筆電話
phone_number = person.phones.add()
phone_number.number = "02-1234567"
phone_number.type = addressbook_pb2.Person.WORK

# 寫入 AddressBook
with open(my_pb_file, "wb") as f:
  f.write(address_book.SerializeToString())
