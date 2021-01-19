from django.db import models
# from django.urls import reverse



class RadioPoll(models.Model):
    radio_id = models.AutoField(primary_key=True)
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')

    # def get_obsalute_url(self):
    #     return reverse('vote', kwarg={"pk":self.pk})

    def radio_total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count
 
 
class CheckboxPoll(models.Model):
    checkbox_id = models.AutoField(primary_key=True)
    quest = models.TextField()
    opt_one = models.CharField(max_length=30)
    opt_two = models.CharField(max_length=30)
    opt_three = models.CharField(max_length=30)
    opt_four = models.CharField(max_length=30)
    opt_one_count = models.IntegerField(default=0)
    opt_two_count = models.IntegerField(default=0)
    opt_three_count = models.IntegerField(default=0)
    opt_four_count = models.IntegerField(default=0)
    head_image = models.ImageField(null=True, blank=True, upload_to='images/')

    # def get_obsalute_url(self):
    #     return reverse('vote', kwarg={"pk":self.pk})

    def checkbox_total(self):
        return self.opt_one_count + self.opt_two_count + self.opt_three_count + self.opt_four_count