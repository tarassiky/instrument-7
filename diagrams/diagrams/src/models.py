
from django.conf import settings
from django.db import models


class Page(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    slug = models.SlugField("Адрес страницы", unique=True)
    content = models.TextField("Содержание")
    is_published = models.BooleanField(
        "Опубликована", default=False
    )
    created_at = models.DateTimeField(
        "Дата создания", auto_now_add=True
    )

    def __str__(self):
        return self.title


class News(models.Model):
    STATUS_CHOICES = [
        ("draft", "Черновик"),
        ("review", "На проверке"),
        ("published", "Опубликована"),
        ("archived", "В архиве"),
    ]

    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст новости")
    publication_date = models.DateTimeField(
        "Дата публикации", null=True, blank=True
    )
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Автор",
    )

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    event_date = models.DateTimeField("Дата мероприятия")
    location = models.CharField(
        "Место проведения", max_length=200
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    position = models.CharField("Должность", max_length=200)
    biography = models.TextField("Биография", blank=True)
    email = models.EmailField("Электронная почта", blank=True)

    def __str__(self):
        return self.full_name


class EducationalProgram(models.Model):
    name = models.CharField("Название программы", max_length=250)
    description = models.TextField("Описание")
    degree = models.CharField("Уровень образования", max_length=100)
    study_direction = models.CharField(
        "Направление подготовки", max_length=150
    )
    teachers = models.ManyToManyField(
        Teacher,
        blank=True,
        related_name="programs",
        verbose_name="Преподаватели",
    )

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField("Название документа", max_length=200)
    file = models.FileField(
        "Файл", upload_to="department_documents/"
    )
    category = models.CharField("Категория", max_length=100)
    uploaded_at = models.DateTimeField(
        "Дата загрузки", auto_now_add=True
    )

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.CharField("Адрес", max_length=250)
    phone = models.CharField("Телефон", max_length=30, blank=True)
    email = models.EmailField("Электронная почта")
    office_hours = models.CharField(
        "Время работы", max_length=200, blank=True
    )

    def __str__(self):
        return self.email
