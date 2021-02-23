from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Category(models.Model):
    # 本棚のモデル
    class Meta:
        db_table = 'category'

    name = models.CharField('カテゴリー名', max_length=50)

    def __str__(self):
        return self.name[:50]

# 本のモデル


class Book(models.Model):
    # テーブル名をbookにする
    class Meta:
        db_table = 'book'

    category = models.ForeignKey(Category, verbose_name='カテゴリー',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField('本のタイトル', max_length=100)
    author = models.CharField('著者', max_length=100)
    recommend_level = models.IntegerField('おすすめレベル', default=1, validators=[
        MaxValueValidator(10), MinValueValidator(1)])
    recommend_context = models.TextField('おすすめポイント')
    date_posted = models.DateTimeField('投稿時間', auto_now=True)
    like = models.IntegerField(default=0)

    # 管理画面で、タイトルが表示されるようにする。
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:book_list')
