'''
Created on 22 Jan 2012

@author: george
'''
from mongoengine import *
from database.model.tweets import EgyptTweet

class WarehouseServer(object):
    '''
    This is a class containing methods related to the warehouse and 
    provides getters for clients to retrieve data.
    '''
    
    def __init__(self):
        '''
        Constructs a Warehouse server object and initiates connection with the database.
        '''
        self.connection = connect("pythia_db")
        
    
    def get_documents_by_date(self, from_date, to_date, limit = 10000, type=EgyptTweet):
        '''
        This is a getter which returns all the documents which were retrieved during
        the period from_date <--> to_date. 
        '''
        t = type.objects(Q(date__gte=from_date) & Q(date__lte=to_date)).limit(limit)
        return t
    
    def get_top_documents_by_date(self, from_date, to_date, limit = 10000, threshold=5, type=EgyptTweet):
        '''
        This is a getter which returns the top documents (in terms of retweets which were retrieved during
        the period from_date <--> to_date. 
        '''
        t = type.objects(Q(date__gte=from_date) & Q(date__lte=to_date) & Q(retweet_count__gte=threshold)).limit(limit)
        return t
    
    def get_all_documents(self, type=EgyptTweet):
        '''
        This is a getter which returns all the documents in the collection.
        '''
        t = type.objects
        return t
    
    def get_n_documents(self, n=0, type=EgyptTweet):
        '''
        This is a getter which returns the n first the documents in the collection.
        '''
        t = type.objects[:n]
        return t
    
    def get_document_by_id(self, id, type=EgyptTweet):
        '''
        Returns the document which corresponds to this id
        '''
        return type.objects(id=id).get()