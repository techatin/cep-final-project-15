from rest_framework import serializers
from .models import Bill, Item

class ItemSerializer(serializers.ModelSerializer):
    
    #bill =  serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Item
        fields = ('name', 'cost', 'bill')
        
    def create(self, validated_data):
        
        print validated_data
        
        temp_bill = validated_data.pop("bill")
        print temp_bill
        
        item = Item(**validated_data)
        
        item.bill = temp_bill
        item.save()
        return item
        
class BillSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True, allow_null=True)
    
    class Meta:
        model = Bill
        fields = ('name', 'description', 'items', 'pk')
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        
        bill = Bill(**validated_data)
        bill.save()
        
        for i in items_data:
            
            if not i:
                item = Item.objects.create(bill=bill, **i)
            
        return bill
        
    def update(self, instance, validated_data):
        
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.save()
        
            
        return instance
            
        
