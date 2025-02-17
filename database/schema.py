def individual_data(Todo):
    return{
        "id":str(Todo["_id"]),
        "title":Todo["title"],
        "description":Todo["description"],
        "status":Todo["is_completed"]
    }

def all_data(Todos):
    return [individual_data(Todo) for Todo in Todos]