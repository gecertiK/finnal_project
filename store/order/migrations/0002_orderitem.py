# Generated by Django 4.1.1 on 2022-10-6 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_bookitem_options_rename_custom_id_book_id_and_more'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='book_item',
            field=models.ManyToManyField(help_text='Select a book_item for the order', to='books.bookitem'),
        ),
        migrations.DeleteModel(
            name='OrderItemBookItem',
        ),
    ]
