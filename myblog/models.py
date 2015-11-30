from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
    username = models.CharField(max_length=50)
    blog = models.ForeignKey('myblog.Blog', related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text