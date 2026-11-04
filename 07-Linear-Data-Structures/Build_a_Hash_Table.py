class HashTable:
    collection = {}

    def hash(self, stringa: str):
        return sum(ord(x) for x in stringa)

    def add(self, key: str , value: str):
        hash_key = self.hash(key)
        if not hash_key in self.collection:
            self.collection.update({hash_key: {key: value}})
        else:
            self.collection[hash_key].update({key: value})

    def remove(self, key: str):
        hash_key = self.hash(key)
        if not hash_key in self.collection or not key in self.collection[hash_key]:
            return 
        else:
            my_list = []
            for k, v in self.collection[hash_key].items():
                my_list.append(k)
                my_list.append(v)
            if len(my_list) > 2:
                del self.collection[hash_key][key]
            else:
                del self.collection[hash_key]

    def lookup(self, key: str):
        hash_key = self.hash(key)
        if not hash_key in self.collection: return None
        return self.collection.get(hash_key).get(key) 
        
        
        
