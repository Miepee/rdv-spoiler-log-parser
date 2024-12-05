import json
from world import World

class SpoilerFile:
    def __init__(self):
        self.json = None
        self.objects = None
        self.world_names = None
        
    def read(self, filename):
        with open(filename, "r") as file:
            self.json = json.load(file)
            file.close()
        
    def get_seed_details(self):
        details = dict()
        details['permalink']    = self.json['info']['permalink']
        details['hash']         = self.json['info']['hash']
        details['word_hash']    = self.json['info']['word_hash']
        details['has_spoiler']  = self.json['info']['has_spoiler']
        return details
    
    def set_world_names(self, names = None):
        if names is None:
            self.world_names = list()
            for i in range(len(self.json['info']['presets'])):
                self.world_names.append(f"Player {i}")
            return
        self.world_names = names
    
    def get_worlds(self):
        if (self.world_names is None):
            self.set_world_names()
        
        worlds = list()
        for world in self.json['game_modifications']:
            worlds.append(World(world))
        return worlds
