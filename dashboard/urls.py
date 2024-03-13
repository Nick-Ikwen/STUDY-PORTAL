from django.urls import path
from . import views

urlpatterns = [
    # The following are urlpatterns for the NOTES section
    path("", views.home, name="home"),
    path("notes/", views.notes, name="notes"),
    path("delete_note/<int:pk>", views.delete_note, name="delete-note"),
    path("notes_detail/<int:pk>", views.NotesDetailView.as_view(), name="notes-detail"),

    # The following are urlpatterns for the HOMEWORK section
    path("homework", views.homework, name="homework"),
    path("update_homework/<int:pk>", views.update_homework, name="update-homework"),
    path("delete_homework/<int:pk>", views.delete_homework, name="delete-homework"),

    # The following are urlpatterns for the YOUTUBE section
    path("youtube", views.youtube, name="youtube"),

    # The following are urlpatterns for the TO-DO section
    path("todo", views.todo, name="todo"),
    path("update_todo/<int:pk>", views.update_todo, name="update-todo"),
    path("delete_todo/<int:pk>", views.delete_todo, name="delete-todo"),

    # The following are urlpatterns for the BOOKS section
    path("books", views.books, name="books"),

    # THe following are urlpatterns for the DICTIONARY section
    path("dictionary", views.dictionary, name="dictionary"),

    # The following are urlpatterns for the WIKIPEDIA section
    path("wiki", views.wiki, name="wiki"),

    # The following are urlpatterns for the CONVERSION section
    path("conversion", views.conversion, name="conversion"),
]