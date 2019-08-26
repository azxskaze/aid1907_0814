from stage2.day01.model import LinkList


class NodeList:
    node_num=0
    def __init__(self):
        self.node_list=[]
    def add_node(self,obj):
        self.node_list.append(LinkList(obj.data,obj.next,NodeList.node_num))
        NodeList.node_num+=1

    def insert_node(self,num,obj):



