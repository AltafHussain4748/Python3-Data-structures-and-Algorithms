from hash.hash_table import HashTable
from hash.hash_tables_chaining import HashTableChain


def test_hash_table():
    table = HashTable()
    table["march 6"] = 310
    table["march 7"] = 420
    assert table["march 7"] == 420


def test_hash_table_chaining():
    table = HashTableChain()
    # march 6 and march 17 will generate 9 as index so we will save [(march 6, 310), (march 17, 420)]
    table["march 6"] = 310
    table["march 9"] = 3198
    table["march 17"] = 420
    assert table["march 6"] == 310
