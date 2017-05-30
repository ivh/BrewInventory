from django.db.models.signals import pre_save
from django.dispatch import receiver
from keepstuff.models import Entry

@receiver(pre_save, sender=Entry)
def update_stock(sender, instance, update_fields, **kwargs):
    if instance.isabs:
        instance.stuff.quant = instance.quant
        instance.stuff.save()
        return

    try:
        before = sender.objects.get(pk=instance.pk)
    except:
        before = None
    created = False if before else True
    if not created:
        instance.stuff.quant -= before.quant
    instance.stuff.quant += instance.quant
    instance.stuff.save()
	
