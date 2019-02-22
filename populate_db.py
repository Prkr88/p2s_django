import os
from faker import Faker
import django

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p2s_django.settings')

# Import settings
django.setup()

import random
from main_app.models import Fleet, SiteUser, Ship, Section, Item, Ship_Type

fakegen = Faker()


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''
    fleet_F = Fleet.objects.get_or_create(company="Spanish Armada", manager="Rodrigo Diaz Vivar")
    ship_type_one = Ship_Type.objects.get_or_create(type_name='Columbus',
                                                    type_pic="static\main_app\site_media\images\columbus.png")
    ship_type_two = Ship_Type.objects.get_or_create(type_name='Crazy_Pirate',
                                                    type_pic="static\main_app\site_media\images\crazy_pirate.png")
    types = [ship_type_one, ship_type_two]
    status = ['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'service', 'out of order']
    sections = ['engine', 'crane', 'gears', 'oil', 'water_elec']
    ships = Ship.objects.all()
    piclist = [
        'static\main_app\items_pics\engine.png',
        'static\main_app\items_pics\crane.png',
        'static\main_app\items_pics\gears.png',
        'static\main_app\items_pics\oil.png',
        'static\main_app\items_pics\water_elec.png',
    ]

    # **************** POPULATE SECTIONS ***********************
    # #Careful Crashing
    # for ship in Ship.objects.all():
    #     for section in sections:
    #         sec = Section.objects.get_or_create(section_name=section, parent=ship)
    # **************** POPULATE SECTIONS ***********************

    for entry in range(N):
        # # Create Fake Data for SHIP
        sn = str(fakegen.ein()).replace('-', '')
        sn = sn[:5]
        fake_sn = "S-" + sn
        fake_n_m = str(fakegen.date_this_year(before_today=True, after_today=False)).split('-')
        fake_n_m.reverse()
        fake_n_m = '-'.join(fake_n_m)
        fake_type = random.choice(types)[0]
        fake_status = random.choice(status)
        # print(fake_sn, fake_status, fake_n_m, fake_type, fleet_F[0])

        # #Create Fake Data for Item
        sections = Section.objects.all()
        fake_item_id = str(fakegen.ean8())
        fake_item_name = (fakegen.street_name().split(' '))[0]
        fake_item_quantity = random.randint(1, 100)
        fake_item_picture = random.choice(piclist)
        fake_section = random.choice(sections)
        fake_onboard = random.choice(ships)

        print(fake_item_id, fake_item_name, fake_item_quantity, fake_item_picture,fake_section,fake_onboard)
        item = Item.objects.get_or_create(item_id=fake_item_id,
                                          item_name=fake_item_name,
                                          item_quantity=fake_item_quantity,
                                          item_picture=fake_item_picture,
                                          section=fake_section,
                                          ship=fake_onboard
                                          )
        # **************** POPULATE SHIPS ***********************
        # ship = Ship.objects.get_or_create(ship_id=fake_sn, n_m=fake_n_m, status=fake_status,
        #                                   fleet=fleet_F[0], type=fake_type)[0]
        # **************** POPULATE SHIPS ***********************




if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(100)
    print('Populating Complete')