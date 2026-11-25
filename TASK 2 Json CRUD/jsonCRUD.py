import json
with open("data.json") as f:
    content=json.load(f)

json_data = {}
while True:
    print("1. Read data")
    print("2. Create data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        read_choice = input("Enter 'id' to read data in JSON format or 'all' to read all data: ")
        if read_choice == "all":
            print(json.dumps(content, indent=4))
        else:
            for item in content:
                if item['id'] == int(read_choice):
                    print(json.dumps(item, indent=4))
                    break
            else:
                print("Data not found.")
    elif choice == "2":
        last_id = max(item['id'] for item in content) if content else 0
        id = last_id + 1
        name = input("Enter name for the new data: ")
        email = input("Enter email for the new data: ")
        new_data = json.dumps({"id": int(id), "name": name, "email": email})
        content.append(json.loads(new_data))
        with open("data.json", "w") as f:
            json.dump(content, f)
        print("Data added successfully.")
    elif choice == "3":
        update_id = input("Enter id to update record:")
        for i, item in enumerate(content):
            if item['id'] == int(update_id):
                update_record = input("Enter n to update name, e to update email, or b to update both: ")
                if update_record == "n":
                    name = input("Enter updated name: ")
                    content[i]['name'] = name
                    with open("data.json", "w") as f:
                        json.dump(content, f)
                    print("Data updated successfully.")
                elif update_record == "e":
                    email = input("Enter updated email: ")
                    content[i]['email'] = email
                    with open("data.json", "w") as f:
                        json.dump(content, f)
                    print("Data updated successfully.")
                elif update_record == "b":
                    name = input("Enter updated name: ")
                    email = input("Enter updated email: ")
                    content[i]['name'] = name
                    content[i]['email'] = email
                    with open("data.json", "w") as f:
                        json.dump(content, f)
                    print("Data updated successfully.")
                break
        else:
            print("Data not found.")
            with open("data.json", "w") as f:
                json.dump(content, f)
    elif choice == "4":
        delete_id = input("Enter id to delete record:")
        for i, item in enumerate(content):  
            if item['id'] == int(delete_id):
                del content[i]
                print("Data deleted successfully.")
                break
        else:
            print("Data not found.")
        with open("data.json", "w") as f:
            json.dump(content, f)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")      