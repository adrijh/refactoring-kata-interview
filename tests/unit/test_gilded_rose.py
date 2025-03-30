from src.gilded_rose.main import Item, GildedRose

def test_standard_item():
    got = perform_items_upgrade([
        Item(name="+5 Dexterity Vest", sell_in=10, quality=9),
        Item(name="Elixir of the Mongoose", sell_in=1, quality=12),
        Item(name="Enigmatic Staff", sell_in=0, quality=16),
        Item(name="Necklace of Ice", sell_in=-12, quality=0),
    ])

    want = [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=8),
        Item(name="Elixir of the Mongoose", sell_in=0, quality=11),
        Item(name="Enigmatic Staff", sell_in=-1, quality=14),
        Item(name="Necklace of Ice", sell_in=-13, quality=0),
    ]

    assert got == want


def test_aged_brie():
    got = perform_items_upgrade([
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Aged Brie", sell_in=-3, quality=5),
        Item(name="Aged Brie", sell_in=0, quality=50),
    ])

    want = [
        Item(name="Aged Brie", sell_in=1, quality=1),
        Item(name="Aged Brie", sell_in=-4, quality=7),
        Item(name="Aged Brie", sell_in=-1, quality=50),
    ]

    assert got == want


def test_sulfuras():
    got = perform_items_upgrade([
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-20, quality=80),
    ])

    want = [
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-20, quality=80),
    ]

    assert got == want


def test_bard_ticket():
    got = perform_items_upgrade([
        Item(name="Ticket to Lucas The Bard concert", sell_in=20, quality=10),
        Item(name="Ticket to Lucas The Bard concert", sell_in=10, quality=10),
        Item(name="Ticket to Lucas The Bard concert", sell_in=5, quality=10),
        Item(name="Ticket to Lucas The Bard concert", sell_in=0, quality=0),
        Item(name="Ticket to Lucas The Bard concert", sell_in=-1, quality=10),
    ])

    want = [
        Item(name="Ticket to Lucas The Bard concert", sell_in=19, quality=11),
        Item(name="Ticket to Lucas The Bard concert", sell_in=9, quality=12),
        Item(name="Ticket to Lucas The Bard concert", sell_in=4, quality=13),
        Item(name="Ticket to Lucas The Bard concert", sell_in=-1, quality=0),
        Item(name="Ticket to Lucas The Bard concert", sell_in=-2, quality=0),
    ]

    assert got == want


def perform_items_upgrade(items: list[Item]) -> list[Item]:
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return gilded_rose.items
