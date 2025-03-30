from src.gilded_rose.main import Item, GildedRose

class TestGildedRose():
    def test_foo(self):
        items = get_starting_inventory()
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert "fixme" == items[0].name


def get_starting_inventory():
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Ticket to Lucas The Bard concert", sell_in=15, quality=20),
        Item(name="Ticket to Lucas The Bard concert", sell_in=10, quality=49),
        Item(name="Ticket to Lucas The Bard concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
