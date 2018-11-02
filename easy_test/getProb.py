import addressbook_pb2
import sys

# 指定 Protocol Buffer 資料檔
my_pb_file = "my_addr_book.pb"

# 建立 AddressBook
address_book = addressbook_pb2.AddressBook()

# 寫入 AddressBook
with open(my_pb_file, "rb") as f:
  address_book.ParseFromString(f.read())

# 顯示資料
for person in address_book.people:
  print("Person ID:", person.id)
  print("  Name:", person.name)
  if person.HasField('email'):
    print("  E-mail address:", person.email)

  for phone_number in person.phones:
    if phone_number.type == addressbook_pb2.Person.MOBILE:
      print("  Mobile phone #:", phone_number.number)
    elif phone_number.type == addressbook_pb2.Person.HOME:
      print("  Home phone #:", phone_number.number)
    elif phone_number.type == addressbook_pb2.Person.WORK:
      print("  Work phone #:", phone_number.number)
