from django.db import models
# from django.db.models.enums import choices

#model of districts
class district(models.Model):
    Name = models.CharField(max_length=10)
    def __str__(self):
        return self.Name

#model of sectors
class sector(models.Model):
    Name  = models.CharField(max_length=10)
    District = models.ForeignKey(district,on_delete=models.SET_NULL,null=True,blank= True,related_name='sectors')

    def __str__(self):
        return self.Name

# model of the restaurant 
class Restaurant(models.Model):
    Rating = (
        ('*', 'StarI'),
        ('**', 'StarII'),
        ('***', 'StarIII'),
        ('****', 'StarIV'),
        ('*****','StarV'),
    )

    Restaurant_name = models.CharField(max_length= 20)
    Ouner_name = models.CharField(max_length= 50)
    # Location = models.CharField(max_length= 40)
    Rating = models.CharField(max_length=50,choices=Rating,null=True)
    Sector = models.ForeignKey(sector,on_delete=models.SET_NULL,null=True,blank= True,related_name='restaurant')
    District = models.ForeignKey(district,on_delete=models.SET_NULL,null=True,blank= True,related_name='restaurant')
    def __str__(self):
        return self.Restaurant_name
    

#model of the dishes
class Dish(models.Model):
    Dish_name = models.CharField(max_length= 40)
    Cooking_Time = models.CharField(max_length= 40)
    date = models.DateField(null=True)
    Ingredient  = models.TextField(max_length=500)
    price = models.CharField(max_length=20)
    picture = models.ImageField(upload_to = 'images')
    restaurant =  models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True,blank= True,related_name='dish')

    def __str__(self):
        return self.Dish_name
        
    
    

