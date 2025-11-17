import pprint

class Dictionary:

    def __init__(self, capacity = 8):
        self.table = [None] * capacity
        self.length = 0
        self.capacity = capacity

    def __setitem__(self, key, value):
        hash_value = hash(key)
        self.check_need_resize()
        index = self.count_position(hash_value)

        if self.table[index] is not None:
            found = False
            for el in self.table[index]:
                if el["key"] == key and el["hash"] == hash_value:
                    el["value"] = value
                    found = True
                    break
            if not found:
                self.length += 1
                self.table[index].append({"key": key,
                                      "value": value,
                                      "hash": hash_value})

        else:
            self.length += 1
            self.table[index] = list()
            self.table[index].append({"key": key,
                                      "value": value,
                                      "hash": hash_value})


    def __getitem__(self, key):
        search_hash = hash(key)
        index = self.count_position(search_hash)
        if self.table[index] is not None:
            for el in self.table[index]:
                if el["hash"] == search_hash and el["key"] == key:
                    return el["value"]
        raise KeyError("Key not found")

    def check_need_resize(self):
        load_factor = 2/3

        if (self.length + 1) / self.capacity >= load_factor:
            self._resize()


    def _resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for el in self.table:

            if el is not None:
                for chain_element in el:
                    index = self.count_position(chain_element["hash"],
                                                new_capacity)
                    if new_table[index] is not None:
                        new_table[index].append(chain_element)

                    else:
                        new_table[index] = list()
                        new_table[index].append(chain_element)

        self.table = new_table
        self.capacity = new_capacity

    def __len__(self):
        return self.length

    def count_position(self, hash_value: int, capacity = None):
        if capacity is None:
            capacity = self.capacity
        return hash_value % capacity






custom_dict = Dictionary()

custom_dict.__setitem__("forelka", 124)
custom_dict.__setitem__("jokdf", 845)
custom_dict.__setitem__("for34lka", 194)
# custom_dict.__setitem__("jo23ff", 8695)
custom_dict.__setitem__("jilkkjla", 124)
custom_dict.__setitem__("orgrgrgo", 8444)
custom_dict.__setitem__("fllllllllll", 19633)
custom_dict.__setitem__("uoibrrrr", 5)
custom_dict.__setitem__("bobre", 88)
custom_dict.__setitem__("lupka", 14)
custom_dict.__setitem__("кеа", 124)
custom_dict.__setitem__("йц", 8444)
# custom_dict.__setitem__("412431", 19633)
# custom_dict.__setitem__("sdfa", 124)
# custom_dict.__setitem__("jjy", 8444)
# custom_dict.__setitem__("412431", 19633)
# custom_dict.__setitem__("bobre", 84)
#
pprint.pprint(custom_dict.table)


# inside of node - tuple, dict, or little class?

# node - key, hash, value

# i should save hash in node

# if i do set - search node in cell with same key, then equal hash and equal
# key then add item and increase length
# then - check load-factor

# get - search cell - hash and then key if no -- ValueError
#

# cell = [{key: 1, value: 2, hash: 123123}, {key: 2, value: 55, hash: 098776}]
