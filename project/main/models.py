from django.db import models

class MenuGroups(models.Model):
    title = models.CharField("Title", max_length=50) 
    sub_title = models.CharField("Sub_Title", max_length=50)
    title_desc = models.TextField("Title_Desc")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

class Menu(models.Model):
    title = models.CharField("Title", max_length=50)
    item = models.CharField("Item", max_length=50)
    alergian = models.CharField("Alergian", max_length=50)
    price = models.CharField("Price", max_length=50)
    description = models.TextField("Description")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"
