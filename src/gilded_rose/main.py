from dataclasses import dataclass

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Ticket to Lucas The Bard concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        # Handle standard item quality
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    # Handle quality increasing item
                    item.quality = item.quality + 1
                    if item.name == "Ticket to Lucas The Bard concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                # Handle standard item sell_in
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                # Handle expired items
                if item.name != "Aged Brie":
                    if item.name != "Ticket to Lucas The Bard concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                # Standard item extra quality loss
                                item.quality = item.quality - 1
                    else:
                        # Ticket goes to 0 if expired
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        # Aged Brie extra quality gain
                        item.quality = item.quality + 1


@dataclass
class Item:
    name: str
    sell_in: int
    quality: int
