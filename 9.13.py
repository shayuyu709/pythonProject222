# class TaskManager:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#         else:
#             print("任务不存在")
#
#     def display_tasks(self):
#         if not self.tasks:
#             print("任务列表为空")
#         else:
#             print("任务列表:")
#             for index, task in enumerate(self.tasks, start=1):
#                 print(f"{index}. {task}")
#
# def main():
#     task_manager = TaskManager()
#
#     while True:
#         print("\n选择一个操作:")
#         print("1. 添加任务")
#         print("2. 删除任务")
#         print("3. 显示任务")
#         print("4. 退出")
#
#         choice = input("输入操作数字: ")
#
#         if choice == "1":
#             task = input("输入要添加的任务: ")
#             task_manager.add_task(task)
#             print("任务已添加")
#         elif choice == "2":
#             task = input("输入要删除的任务: ")
#             task_manager.remove_task(task)
#             print("任务已删除")
#         elif choice == "3":
#             task_manager.display_tasks()
#         elif choice == "4":
#             print("退出程序")
#             break
#         else:
#             print("无效的选择，请重新输入")
#
# if __name__ == "__main__":
#     main()

to_list=[]
def add_task(task):