from django.shortcuts import render

def course_list(request):
    courses = [
        {"id": 1, "name": "Python негиздери", "teacher": "Айбек агай", "duration": "2 ай", "price": 5000},
        {"id": 2, "name": "Frontend Web", "teacher": "Нурзат эжей", "duration": "3 ай", "price": 8000},
        {"id": 3, "name": "UI/UX Дизайн", "teacher": "Санжар агай", "duration": "1.5 ай", "price": 7000},
    ]
    context = {"courses": courses}
    return render(request, "courses/course_list.html", context)
