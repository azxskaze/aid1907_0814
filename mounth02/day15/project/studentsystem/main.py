# from view import *
# import sys.view as u
'''第二种'''
# from  sys import view
# manager=view.StudentManagerView()
# manager.main()
# from sys.view import StudentManagerView
# from project.studentsystem import StudentManagerView
from project.studentsystem.view import StudentManagerView
if __name__=='__main__':
    manager=StudentManagerView()
    manager.main()