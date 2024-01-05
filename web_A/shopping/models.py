from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from phonenumber_field import modelfields
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete

user = get_user_model()
class Type_job(models.Model):
    choice = [('',''),('عميل أخر','عميل اخر')]
    type_job = models.CharField(max_length=40,choices=choice,blank=True)
    def insert(self,job):
        self.choice.insert(0,(str(job),str(job)))
    def __str__(self):
        return f"type_job : { self.type_job }"

# Create your models here.

class Profile(models.Model):
    user_profile            = models.OneToOneField(user,on_delete=models.CASCADE)
    profile_mobile_number   = modelfields.PhoneNumberField(region="DZ")
    profile_image           = models.ImageField(upload_to="profile/image/",blank=True)
    #random nember client and random number worker defulh_client==null 
    jobs = models.OneToOneField(Type_job,on_delete=models.CASCADE)
    def __str__(self):
        return f"profile: { self.user_profile }"
    
class On_Off(models.Model):
    user = models.OneToOneField(Profile,on_delete=models.CASCADE)
    choice = (('on','on'),('off','off'))
    on_or_off = models.CharField(max_length=40,choices=choice)
    def __str__(self):
        return f"on/off : { self.on_or_off }"

class Type_catigory(models.Model):
    type_catigory = models.CharField(max_length=50,unique=True)

    code = models.CharField(max_length=50)
    def __str__(self):
        return f"type_catigory : { self.type_catigory } "

class Catigory(models.Model):

    catigory = models.OneToOneField(Type_catigory,on_delete=models.CASCADE)
    choice = [(f'{x.type_catigory}',f'{x.type_catigory}') for x in Type_catigory.objects.all()  or ""]
    cat = models.CharField(max_length=40,choices=choice,blank=True)


    
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"catigory : { self.catigory } "
    
class Type_prodect(models.Model):
    cality = (
        ("ممتاز","ممتاز"),
        ("جيد","جيد"),
        ("متوسط","متوسط")
    )
    type_prodect = models.CharField(max_length=50,choices=cality)

    def __str__(self):
        return f"wazn {self.type_prodect}"

class Prodect(models.Model):
    catigory = models.OneToOneField(Catigory,on_delete=models.CASCADE,related_name="pro_dect")
    c = models.ForeignKey(Type_prodect,on_delete=models.CASCADE) 
    img =models.ImageField(blank=True,upload_to="%y/%m/%d")
    name = models.CharField(max_length=50)
    contity = models.PositiveIntegerField()
    price = models.IntegerField(blank=False)
    
    def __str__(self):
        return f" name : { self.name }"


class Chop_prodect(models.Model):

    choice1 = (        
        ("g","g"),
        ("x*g","x*g"),
        ("kg","kg"),
        ("x*kg","x*kg"),
    )
    choice2 = (        
        ("ml","ml"),
        ("x*ml","x*ml"),
        ("L","L"),
        ("x*L","x*L"),
    )
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)  
    type_shop_prodect = models.ForeignKey(Type_prodect,on_delete=models.CASCADE,related_name="prodect_shopping")          
    ticket = models.ForeignKey(Prodect,on_delete=models.CASCADE)
    contity = models.FloatField()
    wazn_kg = models.CharField(max_length=10,choices=choice1,default="kg")
    wazn_L = models.CharField(max_length=10,choices=choice2,default="L")
    def __str__(self):
        return f"wazn {self.wazn_kg or self.wazn_L}"

class VitVit(models.Model):
    u_add  = models.ForeignKey(Chop_prodect,on_delete=models.CASCADE)
    track_with_user_packet = models.ForeignKey(User,on_delete=models.CASCADE)
    get_lat  = models.FloatField(max_length=30) 
    get_long = models.FloatField(max_length=30)
    vitass = (
        ("بدون وقت","بدون وقت"),
        ("يوم كامل (24) ساعة","يوم كامل (24) ساعة"),
        ("نصف يوم","نصف يوم"),
        ("ساعات 3 ","3 ساعات "),
        ("ساعة","ساعة"),
    )

    vit = models.CharField(max_length=50,choices=vitass,default=vitass[0][0])
    def __str__(self):
        return f"{self.u_add.user} :cat: ({self.u_add.ticket.name}) :contity: ({self.u_add.contity} :wazn: ({self.u_add.wazn}))"

@receiver(post_save,sender=User)
def save(sender,instance,created,**kwrgs):
    if created:
        user = instance
        obj = Profile.objects.create(
            user_profile = user,
            profile_mobile_number= "0791045394",
            jobs=Type_job.objects.get(id=1),

        )
        obj.save()
        print("yes created By "+str(sender)+str(instance))
"""@receiver(post_save,sender=Profile)
def save(sender,instance,created,**kwrgs): 
    if created:
        user = instance
        obj = Process_with_Profile.objects.create(
            user = user,
            pro = user.pro
        )
        obj.save()
        print("yes proooooooooo By "+str(sender)+str(instance))

"""




@receiver(post_delete,sender=Profile)
def delete(sender,instance,**kargs):
    user = instance.user_profile
    user.delete()
    print(f"delete user {user}")
#post_save.connect(save,sender=User)