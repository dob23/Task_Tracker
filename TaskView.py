import json
import os
import uuid
from datetime import datetime
#LISTAR TAREAS

def listTask(filter_status = None):
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No hay tareas registradas")
        
        task = data["task"]
        
        if filter_status:
            tasks = [task for task in tasks if  task["status"] == filter_status]
            
        if not  tasks:
            print("No hay tareas para mostrar")
            return
        
        for task in tasks:
            print(f'{task["id"]}. {task["title"]}')



#AÑADIR TAREA
def addTask(title):
    try:
        with open("task.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"task": []}
        
        
    new_task = {
        "id" : len(data["task"]) + 1,
        "title" : title,
        "status": "pendiente",
        "created_at": datetime.now().isoformat(),
        "update_at": datetime.now().isoformat(),
    }
    data["task"].append(new_task)
    
    with open("task.json", "w") as file:
        json.dump(data,file,indent=4)
        
    print(f"Tarea {title} Agregada con exito.")

#ACTUALZIAR TAREA
def update_task(task_id, new_title = None,new_status = None):
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: no hay tareas registradas")
    
    task_found = False
    for task in data["task"]:
        if task ["id"] == task_id:
            if new_title:
                task["title"] = new_title
            if new_status:
                valid_statuses = ["pendiente", "en progreso","realizado"]
                if new_status  not in valid_statuses:
                        print(f"Error: estado '{new_status}' no es valido")
                        return
                task["status"] = new_status
                task["update_at"] = datetime.now().isoformat()
                task_found = True
                break
    if task_found:
        with open ("task.json", "w")as file:
            json.dump(data,file, indent =4)
        print(f"Tarea {task_id} actualizada con exito")
    else:
        print(f"Error: no se encontro una tarea con el id: {task_id}.")


def deleteTask(task_id):
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: no hay tareas registradas")
        return 
    

    initial_count = len(data["task"])
    data["task"] =  [task  for task in data["task"]if task["id"] != task_id]
    
    if len(data["task"]) < initial_count:
        with open("task.json", "w") as file:
            json.dump(data,file, indent=4)
            print(f"Tarea {task_id} eliminada con exito")
    else:
        print(f"Error: No se encuentra una tarea con el id {task_id}")
        

#Funcion para crear json 
def initial_json():
    if not os.path.exists("task.json"):
        with open("task.json", "w") as file:
            json.dump({"task": []}, file, indent=4)
        print("Archivo task.json creado")
        

#CREACION DE ID UNICOS
def id_unique():
    return str(uuid.uuid4())