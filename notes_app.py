import os

# Step 2: Create a note file
def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            file.write(note_text)
        print("Заметка успешно создана.")
    except Exception as e:
        print(f"Ошибка при создании заметки: {e}")

# Step 3: Request user input and create note
def create_note():
    try:
        note_name = input("Введите название заметки: ")
        note_text = input("Введите текст заметки: ")
        build_note(note_text, note_name)
    except Exception as e:
        print(f"Ошибка при создании заметки: {e}")

# Step 4: Read a note
def read_note():
    try:
        note_name = input("Введите название заметки для чтения: ")
        filename = f"{note_name}.txt"
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as file:
                print("\nСодержимое заметки:")
                print(file.read())
        else:
            print("Заметка не найдена.")
    except Exception as e:
        print(f"Ошибка при чтении заметки: {e}")

# Step 5: Edit a note
def edit_note():
    try:
        note_name = input("Введите название заметки для редактирования: ")
        filename = f"{note_name}.txt"
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as file:
                print("Текущий текст заметки:")
                print(file.read())
            new_text = input("Введите новый текст заметки: ")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(new_text)
            print("Заметка обновлена.")
        else:
            print("Заметка не найдена.")
    except Exception as e:
        print(f"Ошибка при редактировании заметки: {e}")

# Step 6: Delete a note
def delete_note():
    try:
        note_name = input("Введите название заметки для удаления: ")
        filename = f"{note_name}.txt"
        if os.path.isfile(filename):
            os.remove(filename)
            print("Заметка удалена.")
        else:
            print("Заметка не найдена.")
    except Exception as e:
        print(f"Ошибка при удалении заметки: {e}")

# Step 8: Display notes sorted from shortest to longest
def display_notes():
    try:
        notes = [f for f in os.listdir() if f.endswith('.txt')]
        sorted_notes = sorted(notes, key=lambda name: os.path.getsize(name))

        if not sorted_notes:
            print("Нет заметок.")
            return

        print("Заметки (от самой короткой к самой длинной):")
        for note in sorted_notes:
            print(note)
    except Exception as e:
        print(f"Ошибка при выводе заметок: {e}")

# Step 9: Display notes sorted from longest to shortest
def display_sorted_notes():
    try:
        notes = [f for f in os.listdir() if f.endswith('.txt')]
        sorted_notes = sorted(notes, key=lambda name: os.path.getsize(name), reverse=True)

        if not sorted_notes:
            print("Нет заметок.")
            return

        print("Заметки (от самой длинной к самой короткой):")
        for note in sorted_notes:
            print(note)
    except Exception as e:
        print(f"Ошибка при сортировке заметок: {e}")

# Step 7: Main loop
def main():
    try:
        while True:
            print("\nМеню:")
            print("1 — Создать заметку")
            print("2 — Прочитать заметку")
            print("3 — Редактировать заметку")
            print("4 — Удалить заметку")
            print("5 — Показать все заметки (короткие → длинные)")
            print("6 — Показать заметки (длинные → короткие)")
            print("0 — Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                create_note()
            elif choice == "2":
                read_note()
            elif choice == "3":
                edit_note()
            elif choice == "4":
                delete_note()
            elif choice == "5":
                display_notes()
            elif choice == "6":
                display_sorted_notes()
            elif choice == "0":
                print("Выход из программы...")
                break
            else:
                print("Неверный ввод, попробуйте снова.")
    except Exception as e:
        print(f"Ошибка в работе приложения: {e}")


if __name__ == "__main__":
    main()

