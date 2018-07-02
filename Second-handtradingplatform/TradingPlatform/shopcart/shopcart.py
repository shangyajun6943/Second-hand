class ShopCart(object):
    def __init__(self):
        self.order = None
        self.order_item_list = None
        self.shop_user=None


class OrderItems(object):
    def __init__(self):
        self.order_item = None
        self.product = None