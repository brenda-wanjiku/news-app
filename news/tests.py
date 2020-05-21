from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.James = Editor(first_name = 'James', last_name = 'Muruiki', email = 'james@gmail.com')
        self.James.save()

    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.James, Editor))
    
    def test_save(self):
        self.Martha =  Editor(first_name = 'Martha', last_name = 'Wangari', email = 'martha@gmail.com')
        self.Martha.save_editor()
        editor = Editor.objects.all()
        self.assertTrue(len(editor) > 0)


    def test_delete(self):
        self.James.delete_editor()
        editor = Editor.objects.all()
        self.assertTrue(len(editor) == 0 )
        self.assertEqual(len(editor), 0 )


class ArticleTestClass(TestCase):
    def setUp(self):
        #Creating a new editor and saving it
        self.james = Editor(first_name = 'James', last_name = 'Mwangi', email = 'james@gmail.com')
        self.james.save_editor()

        
        #Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article', post = 'This is a random post', editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date)== 0)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
