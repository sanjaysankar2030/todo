#!/usr/bin/env python3

import json

# from termcolor import colored
with open("todo.json", "r") as file:
    todo = json.load(file)


def show():
    print("\n")
    print("      ____________________________________________________")
    print("      |  ID     |  Tasks             |  D.O.A         ==>    Status  ")
    for num, todos in todo.items():

        print("      _________________________________________________________")
        print(
            f"      |   {num}     |  {todos[0]}  |  {todos[1]}          ===>{todos[2]} "
        )
    print("\n")
    manipulate()


def errshow():
    print("\n")
    print("           ______________________________________________")
    print("          |  ID     |  Tasks       |  D.O.A          ==>  Status  ")
    for num, todos in todo.items():
        print("           ______________________________________________")
        print(
            f"          |   {num}     |  {todos[0]}  |  {todos[1]}        ==> {todos[2]}"
        )
    print("\n")


def manipulate():
    global completed
    no = len(todo)
    manip = input("\n   > Add/Mark Complete/Quit (A/C/Q):")
    if manip == "A":
        append_no = int(input("   > How many tasks you want to add:"))
        for j in range(1, append_no + 1):
            j = j + no
            app_task = input("Tasks:").title()
            app_doa = input("D.O.A:").title()
            app_status = "Pending"
            todo[j] = [app_task, app_doa, app_status]
            json_save()
        errshow()
        print("\n Quit and come back to complete or delete tasks")
    elif manip == "C":
        comp_id = str(input(" \n   > Which task did you complete:"))
        for comp_no, comp_text in todo.items():
            if comp_id == comp_no:
                comp_text[2] = "Completed"
        json_save()
        show()
    else:
        del_ans = input(
            "\n   > Have you completed all of your tasks, Do you want to delete all of  your tasks (yes/no):"
        )
        if del_ans == "yes":
            todo.clear()
            print("\n   <All the tasks are deleted....>")
            json_save()
        else:
            print("\nCarry on with your work !!! :> ")


def json_save():
    with open("todo.json", "w") as f:
        json.dump(todo, f, indent=4)
        print("Saving the tasks.... ")


if __name__ == "__main__":
    show()
