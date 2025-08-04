import os 
import json 
from datetime import datetime

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")


def check_file_premission():
    try:
        with open(NOTES_FILE, "a", encoding="utf-8"):
            pass
        return True
    except PermissionError:
        print("Ошибка, система не может получить доступ к файлу")



def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
           data = f.read()

           if not data.strip():
               return []
           return json.loads(data)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка {e} ")
        return []



def save_notes(notes):
    try:
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
           json.dump(notes, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранение файлов! {e} ")




def add_note():
    title = input("Введите Заголовок: ")
    content = input("Введите заметку: ")
    timespawn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes = load_notes()
    notes.append({
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "datatime_create_at": timespawn,
        "datatime_update_at": timespawn
    })

    save_notes(notes)
    print("Заметка успешна добавлена!")




def list_notes():
    notes = load_notes()

    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"\nЗаголовок: {note['title']}")
        print(f"\nЗаметка: {note['content']}")
        print(f"\nДата Создание: {note['datatime_create_at']}")
        print(f"\nВремя обновлена: {note['datatime_update_at']}")
        print("-" * 30)
    

    if not notes:
        print("📝 Список заметок пуст.")
        return




def search_notes():
    query = input("Введите слово для поиска: ")
    notes = load_notes()
    found = []

    for note in notes:
        if (query in note['title'].lower()) or (query in note['content'].lower()):
            found.append(note)
    if not found:
        print("Ничего не найдена")
        return
    else:
        print(f"Найдено {len(found)} заметок")
        for note in notes:
            print(f"/ID: {note['id']} | {note('titile')}")



def delite_notes():
    list_notes()
    try:
        note_id = int(input("Введите ID для удаление заметки: "))
        notes = load_notes()
        notes = [note for note in notes if note['id'] != note_id]
        save_notes(notes)
        print("Заметка Удалена")
    except ValueError:
        print("Ошибка введите число!")



def edit_notes():
    list_notes()

    try:
        notes_id = int(input("ВВедите ID для редоктирование заметок: "))
        notes = load_notes()

        for note in notes:
            if note["id"] == notes_id:
                new_title = input(f"Новый заголовок ({note['title']})") or note["title"]
                new_content = input(f"Новая заметка ({note['content']})") or note["content"]

                note["title"] = new_title
                note["content"] = new_content
                note["datatime_update_at"] = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

                save_notes(notes)
                print("Заметка Обновлена!")
                return
        print("Заметка с таким ID не найдена")
        return
    except ValueError:
        print("Упс вы ввели неправильное значение должно быть число!")



def main():
    print(f"Текущая директория: {os.getcwd()}")


    if not check_file_premission():
        return
    
    while True:
        print("\n NoteClI - менеджер заметок!")
        print("\n 1: Добавить заметку")
        print("\n 2: Список Заметок")
        print("\n 3: Поиск заметок")
        print("\n 4: Удалить заметку")
        print("\n 5: Редактировать заметку заметку")
        print("\n 6: Выход")


        choise = int(input("\nВведите число "))

        if choise == 1:
            add_note()
        elif choise == 2:
            list_notes()
        elif choise == 3:
            search_notes()
        elif choise == 4:
            delite_notes()
        elif choise == 5:
            edit_notes()
        elif choise == 6:
            break
        else:
            print("Ошибка вы ввели не то число что доступно в доступных")


if __name__ == "__main__":
    main()