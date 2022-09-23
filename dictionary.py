a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'} ①
print(a_dict)
# kq: {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict['server']) ②
 # kq :'db.diveintopython3.org'
print(a_dict['database']) ③
 # kq :'mysql'
print(a_dict['db.diveintopython3.org'])
# error vì ko lấy dc value để tìm key
 # replace value of key
    a_dict['database'] = 'blog'
# add key-value
  a_dict['user'] = 'dora'
  # python có phân biêth hoa thường ở key
  # nó vẫn thêm 1 cặp key-value
  a_dict['User'] = 'mark'

 print(a_dict)
 # nó là giá trị mới 
  # None là giá trị null, và nó tạo ra false
