import os.path

task_types = {
    "Д": "homework",
    "П": "lesson",
    "Э": "extra"
}

def create_new_files(name, until):
    for i in range(1, until+1):
        if not os.path.exists(f"{task_types[name]}_{i}.py"):
            with open(f"{task_types[name]}_{i}.py", "w") as file:
                file.write(f"# Задание №{name}{i}")


create_new_files("Э", 10)
create_new_files("П", 10)
create_new_files("Д", 20)
