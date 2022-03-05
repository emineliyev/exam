from django.db import models


class StClass(models.Model):
    title = models.PositiveIntegerField(verbose_name='Sinif')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Sinif'
        verbose_name_plural = 'Sinifi'
        ordering = ['title']


class Group(models.Model):
    title = models.PositiveIntegerField(verbose_name='Qrup')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Qrup'
        verbose_name_plural = 'Qrup'
        ordering = ['title']


class Gender(models.Model):
    title = models.CharField(max_length=60, verbose_name='Cins')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Cins'
        verbose_name_plural = 'Cins'
        ordering = ['title']


class Section(models.Model):
    title = models.CharField(max_length=60, verbose_name='Bölmə')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Bölmə'
        verbose_name_plural = 'Bölmə'
        ordering = ['title']


class ForeignLanguage(models.Model):
    title = models.CharField(max_length=60, verbose_name='Xarici dil')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Xarici dil'
        verbose_name_plural = 'Xarici dil'
        ordering = ['-title']


class Exam(models.Model):
    name = models.CharField(max_length=150, verbose_name='İmtahan adı')
    exam_date = models.DateField(verbose_name='İmtahan tarixi')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'İmtahan'
        verbose_name_plural = 'İmtahan'
        ordering = ['-exam_date']


class Location(models.Model):
    name = models.CharField(max_length=250, verbose_name='Məntəqə adı')
    address = models.TextField(verbose_name='Ünvan')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='İmtahan')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'İmtahan məntəqəsi'
        verbose_name_plural = 'İmtahan məntəqəsi'
        ordering = ['name']


class Floor(models.Model):
    name = models.CharField(max_length=250, verbose_name='Mərtəbə adı')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Məntəqə')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Mərtəbə'
        verbose_name_plural = 'Mərtəbə'
        ordering = ['name']


class Room(models.Model):
    name = models.CharField(max_length=250, verbose_name='Otaq adı')
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name='Mərtəbə')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Otaq'
        verbose_name_plural = 'Otaq'
        ordering = ['name']


class Student(models.Model):
    name = models.CharField(max_length=60, verbose_name='Ad')
    last_name = models.CharField(max_length=60, verbose_name='Soyad')
    stclass = models.ForeignKey(StClass, on_delete=models.CASCADE, verbose_name='Sinif')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Qrup')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='Cins')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Bölmə')
    language = models.ForeignKey(ForeignLanguage, on_delete=models.CASCADE, verbose_name='Xarici dil')
    phone = models.IntegerField(verbose_name='Telefon nömrəsi')
    school = models.CharField(max_length=60, verbose_name='Məktəb')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Qeydiyyat tarixi')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='İmtahan')

    def __str__(self):
        return f"Şagirdin adı: {self.name}"

    class Meta:
        verbose_name = 'Şagird'
        verbose_name_plural = 'Şagird'
        ordering = ['-create_at']