import argparse
from TaskView import *

def main():
    parser = argparse.ArgumentParser(description="Gestor de tareas CLI")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

  
    parser_list = subparsers.add_parser("list", help="Listar tareas")
    parser_list.add_argument("--status", choices=["pendientes", "en progreso", "realizado"], help="Filtrar tareas por estado")


    parser_add = subparsers.add_parser("add", help="Agregar una nueva tarea")
    parser_add.add_argument("title", help="Título de la tarea")

   
    parser_update = subparsers.add_parser("update", help="Actualizar una tarea")
    parser_update.add_argument("id", type=int, help="ID de la tarea a actualizar")
    parser_update.add_argument("--title", help="Nuevo título de la tarea")
    parser_update.add_argument("--status", choices=["pendientes", "en progreso", "realizado"], help="Nuevo estado de la tarea")

    parser_delete = subparsers.add_parser("delete", help="Eliminar una tarea")
    parser_delete.add_argument("id", type=int, help="ID de la tarea a eliminar")

    
    args = parser.parse_args()

    
    if args.command == "list":
        listTask(filter_status=args.status)
    elif args.command == "add":
        addTask(args.title)
    elif args.command == "update":
        update_task(args.id, new_title=args.title, new_status=args.status)
    elif args.command == "delete":
        deleteTask(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    initial_json()
    main()
