from django.db import models
class PatentGroup(models.Model):
    pass

class Patent(models.Model):
    number = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 
    description = models.TextField()
    label = models.ForeignKey(
        PatentGroup,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return(self.number)
    
    @property
    def path(self):
        import os
        return os.path.join("/static/eoi/patents/", self.link)


class InstrumentClass(models.Model):
    pass

class Case(models.Model):
    case_name = models.CharField(max_length = 100)
    jurisdiction = models.CharField(max_length = 100)
    counsel = models.CharField(max_length = 300)
    start = models.DateField() 
    end = models.DateField() 
    work_product = models.TextField()
    notes = models.TextField()
    status = models.TextField()
