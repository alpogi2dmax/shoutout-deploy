#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        print("Clearing db...")
        User.query.delete()
        
        db.session.commit()


        print("Seeding users...")
        users = []
        user1 = User(
            username='lightyagami',
            email='lightyagami@gmail.com',
            first_name='Light',
            last_name='Yagami',
            profile_pic='https://i.imgur.com/q4IgIRx.png'
        )
        user1.password_hash = 'password'
        users.append(user1)
        user2 = User(
            username='roronoazoro',
            email='roronoazoro@gmail.com',
            first_name='Roronoa',
            last_name='Zoro',
            profile_pic='https://i.imgur.com/XcxCRIW.png'
        )
        user2.password_hash = 'password'
        users.append(user2)
        user3 = User(
            username='leviackerman',
            email='leviackerman@gmail.com',
            first_name='Levi',
            last_name='Ackerman',
            profile_pic='https://i.imgur.com/Bfqji06.png'
        )
        user3.password_hash = 'password'
        users.append(user3)
        user4 = User(
            username='edwardelric',
            email='edwardelric@gmail.com',
            first_name='Edward',
            last_name='Elric',
            profile_pic='https://i.imgur.com/Tf2jQQV.png'
        )
        user4.password_hash = 'password'
        users.append(user4)
        user5 = User(
            username='gojosatoru',
            email='gojosatoru@gmail.com',
            first_name='Gojo',
            last_name='Satoru',
            profile_pic='https://i.imgur.com/qRfUCpd.png'
        )
        user5.password_hash = 'password'
        users.append(user5)
        user6 = User(
            username='josephjoestar',
            email='josephjoestar@gmail.com',
            first_name='Joseph',
            last_name='Joestar',
            profile_pic='https://i.imgur.com/U44ASCB.png'
        )
        user6.password_hash = 'password'
        users.append(user6)
        user7 = User(
            username='monkeydluffy',
            email='monkeydluffy@gmail.com',
            first_name='Monkey',
            last_name='Luffy',
            profile_pic='https://i.imgur.com/JrCXyOZ.png'
        )
        user7.password_hash = 'password'
        users.append(user7)
        user8 = User(
            username='arsenelupiniii',
            email='arsenelupiniii@gmail.com',
            first_name='Arsene',
            last_name='Lupin III',
            profile_pic='https://i.imgur.com/R6497xl.png'
        )
        user8.password_hash = 'password'
        users.append(user8)
        user9 = User(
            username='kenshinhimura',
            email='kenshinhimura@gmail.com',
            first_name='Kenshin',
            last_name='Himura',
            profile_pic='https://i.imgur.com/0Mq5J1u.png'
        )
        user9.password_hash = 'password'
        users.append(user9)
        user10 = User(
            username='spikespiegel',
            email='spikespiegel@gmail.com',
            first_name='Spike',
            last_name='Spiegel',
            profile_pic='https://i.imgur.com/DBYghZ8.png'
        )
        user10.password_hash = 'password'
        users.append(user10)
        db.session.add_all(users)
        db.session.commit()

        print("Seeding done!")
