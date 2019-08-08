dict01 = {'经理':{'曹操','刘备','孙权'},
          '技术':{'曹操','刘备','关羽','张飞'}}

# jingli={'曹操','刘备','孙权'}
# jishu={'曹操','刘备','关羽','张飞'}

is_jingli_and_jishu = dict01['经理']&dict01['技术']
is_jingli_not_jishu = dict01['经理']-dict01['技术']
not_jingli_is_jishu = dict01['技术']-dict01['经理']
zhangfei_is_or_jingli = {'张飞'} < dict01['经理']
num_people = len(dict01['经理']|dict01['技术'])
only_1 = len(dict01['经理']^dict01['技术'])
print(is_jingli_and_jishu,
      is_jingli_not_jishu,
      not_jingli_is_jishu,
      zhangfei_is_or_jingli,
      num_people,only_1)