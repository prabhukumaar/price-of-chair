import os

import pymongo

__author__ = 'jslvtr'


class Database(object):
    URI = 'mongodb+srv://greatnages:greatnages@pricing-cluster-pbamx.mongodb.net/pricingdb'
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)
