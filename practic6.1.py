# Робота зі словниками
# Третій студент: пошук та редагування даних
# Автор: Тарасенко С.В.

students = {
    "КН-44": [
        {
            "ПІБ": "Обух Володимир Валентинович",
            "курс": 2,
            "оцінки": {
                "Математика": 90,
                "Програмування": 95,
                "Фізика": 88
            }
        },
        {
            "ПІБ": "Грибоєдова Марина Олегівна",
            "курс": 2,
            "оцінки": {
                "Математика": 55,
                "Програмування": 79,
                "Фізика": 87
            }
        },
        {
            "ПІБ": "Могильний Дмитро Валерійович",
            "курс": 2,
            "оцінки": {
                "Математика": 85,
                "Програмування": 92,
                "Фізика": 80
            }
        }
    ]
}

def find_student(full_name):
    """Пошук студента за ПІБ"""
    for group, group_students in students.items():
        for student in group_students:
            if student["ПІБ"] == full_name:
                return group, student
    return None, None

def update_grade(full_name, subject, new_grade):
    """Оновлення оцінки студента"""
    group, student = find_student(full_name)
    if student:
        student["оцінки"][subject] = new_grade
        print("Оцінку оновлено")
    else:
        print("Студента не знайдено")

# Приклад використання
update_grade("Грибоєдова Марина Олегівна", "Програмування", 79)

# Виведення оновлених даних
print("\nОновлені дані:")
for group, group_students in students.items():
    print(f"\nГрупа: {group}")
    for s in group_students:
        print(s)
