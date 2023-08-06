# -*- coding: utf-8 -*-

import inventree.base
import inventree.part
import inventree.company


class PurchaseOrder(
    inventree.base.MetadataMixin,
    inventree.base.InventreeObject,
    inventree.base.StatusMixin
):
    """ Class representing the PurchaseOrder database model """

    URL = 'order/po'

    def getLineItems(self, **kwargs):
        """ Return the line items associated with this order """
        return PurchaseOrderLineItem.list(self._api, order=self.pk, **kwargs)

    def getExtraLineItems(self, **kwargs):
        """ Return the line items associated with this order """
        return PurchaseOrderExtraLineItem.list(self._api, order=self.pk, **kwargs)

    def addLineItem(self, **kwargs):
        """
        Create (and return) new PurchaseOrderLineItem object against this PurchaseOrder
        """

        kwargs['order'] = self.pk

        return PurchaseOrderLineItem.create(self._api, data=kwargs)

    def addExtraLineItem(self, **kwargs):
        """
        Create (and return) new PurchaseOrderExtraLineItem object against this PurchaseOrder
        """

        kwargs['order'] = self.pk

        return PurchaseOrderExtraLineItem.create(self._api, data=kwargs)

    def getAttachments(self):
        return PurchaseOrderAttachment.list(self._api, order=self.pk)
    
    def uploadAttachment(self, attachment, comment=''):
        return PurchaseOrderAttachment.upload(
            self._api,
            attachment,
            comment=comment,
            order=self.pk,
        )

    def issue(self, **kwargs):
        """
        Issue the purchase order
        """

        # Return
        return self._statusupdate(status='issue', **kwargs)

    def receiveAll(self, location, status=10):
        """
        Receive all of the purchase order items, into the given location.

        Note that the location may be overwritten if a destination is saved in the PO for the line item.

        By default, the status is set to OK (Code 10).

        To modify the defaults, use the arguments:
            status: Status code
                    10 OK
                    50 ATTENTION
                    55 DAMAGED
                    60 DESTROYED
                    65 REJECTED
                    70 LOST
                    75 QUARANTINED
                    85 RETURNED
        """

        # Check if location is a model - or try to get an integer
        try:
            location_id = location.pk
        except:  # noqa:E722
            location_id = int(location)

        # Prepare request data
        items = list()
        for li in self.getLineItems():
            quantity_to_receive = li.quantity - li.received
            # Make sure quantity > 0
            if quantity_to_receive > 0:
                items.append(
                    {
                        'line_item': li.pk,
                        'supplier_part': li.part,
                        'quantity': quantity_to_receive,
                        'status': status,
                        'location': location_id,
                    }
                )

        # If nothing is left, quit here
        if len(items) < 1:
            return None

        data = {
            'items': items,
            'location': location_id
        }

        # Set the url
        URL = f"{self.URL}/{self.pk}/receive/"

        # Send data
        response = self._api.post(URL, data)

        # Reload
        self.reload()

        # Return
        return response


class PurchaseOrderLineItem(inventree.base.InventreeObject):
    """ Class representing the PurchaseOrderLineItem database model """

    URL = 'order/po-line'

    def getSupplierPart(self):
        """
        Return the SupplierPart associated with this PurchaseOrderLineItem
        """
        return inventree.company.SupplierPart(self._api, self.part)

    def getPart(self):
        """
        Return the Part referenced by the associated SupplierPart
        """
        return inventree.part.Part(self._api, self.getSupplierPart().part)

    def getOrder(self):
        """
        Return the PurchaseOrder to which this PurchaseOrderLineItem belongs
        """
        return PurchaseOrder(self._api, self.order)

    def receive(self, quantity=None, status=10, location=None, batch_code='', serial_numbers=''):
        """
        Mark this line item as received.

        By default, receives all remaining items in the order, and puts them in the destination defined in the PO.
        The status is set to OK (Code 10).

        To modify the defaults, use the arguments:
            quantity: Number of units to receive. If None, will calculate the quantity not yet received and receive these.
            status: Status code
                    10 OK
                    50 ATTENTION
                    55 DAMAGED
                    60 DESTROYED
                    65 REJECTED
                    70 LOST
                    75 QUARANTINED
                    85 RETURNED
            location: Location ID, or a StockLocation item

        If given, the following arguments are also sent as parameters:
            batch_code
            serial_numbers
        """

        if quantity is None:
            # Substract number of already received lines from the order quantity
            quantity = self.quantity - self.received

        if location is None:
            location_id = self.destination
        else:
            # Check if location is a model - or try to get an integer
            try:
                location_id = location.pk
            except:  # noqa:E722
                location_id = int(location)

        # Prepare request data
        data = {
            'items': [
                {
                    'line_item': self.pk,
                    'supplier_part': self.part,
                    'quantity': quantity,
                    'status': status,
                    'location': location_id,
                    'batch_code': batch_code,
                    'serial_numbers': serial_numbers
                }
            ],
            'location': location_id
        }

        # Set the url
        URL = f"{self.getOrder().URL}/{self.getOrder().pk}/receive/"

        # Send data
        response = self._api.post(URL, data)

        # Reload
        self.reload()

        # Return
        return response


class PurchaseOrderExtraLineItem(inventree.base.InventreeObject):
    """ Class representing the PurchaseOrderExtraLineItem database model """

    URL = 'order/po-extra-line'

    def getOrder(self):
        """
        Return the PurchaseOrder to which this PurchaseOrderLineItem belongs
        """
        return PurchaseOrder(self._api, self.order)


class PurchaseOrderAttachment(inventree.base.Attachment):
    """Class representing a file attachment for a PurchaseOrder"""

    URL = 'order/po/attachment'

    REQUIRED_KWARGS = ['order']


class SalesOrder(
    inventree.base.MetadataMixin,
    inventree.base.InventreeObject,
    inventree.base.StatusMixin
):
    """ Class respresenting the SalesOrder database model """

    URL = 'order/so'

    def getLineItems(self, **kwargs):
        """ Return the line items associated with this order """
        return SalesOrderLineItem.list(self._api, order=self.pk, **kwargs)

    def getExtraLineItems(self, **kwargs):
        """ Return the line items associated with this order """
        return SalesOrderExtraLineItem.list(self._api, order=self.pk, **kwargs)

    def addLineItem(self, **kwargs):
        """
        Create (and return) new SalesOrderLineItem object against this SalesOrder
        """

        kwargs['order'] = self.pk

        return SalesOrderLineItem.create(self._api, data=kwargs)

    def addExtraLineItem(self, **kwargs):
        """
        Create (and return) new SalesOrderExtraLineItem object against this SalesOrder
        """

        kwargs['order'] = self.pk

        return SalesOrderExtraLineItem.create(self._api, data=kwargs)

    def getAttachments(self):
        return SalesOrderAttachment.list(self._api, order=self.pk)
    
    def uploadAttachment(self, attachment, comment=''):
        return SalesOrderAttachment.upload(
            self._api,
            attachment,
            comment=comment,
            order=self.pk,
        )
    
    def getShipments(self, **kwargs):
        """ Return the shipments associated with this order """
        
        return SalesOrderShipment.list(self._api, order=self.pk, **kwargs)

    def addShipment(self, reference, **kwargs):
        """ Create (and return) new SalesOrderShipment
        against this SalesOrder """

        kwargs['order'] = self.pk
        kwargs['reference'] = reference

        return SalesOrderShipment.create(self._api, data=kwargs)


class SalesOrderLineItem(inventree.base.InventreeObject):
    """ Class representing the SalesOrderLineItem database model """

    URL = 'order/so-line'

    def getPart(self):
        """
        Return the Part object referenced by this SalesOrderLineItem
        """
        return inventree.part.Part(self._api, self.part)

    def getOrder(self):
        """
        Return the SalesOrder to which this SalesOrderLineItem belongs
        """
        return SalesOrder(self._api, self.order)

    def allocateToShipment(self, shipment, stockitems=None, quantity=None):
        """
        Assign the items of this line to the given shipment.
        
        By default, assign the total quantity using the first stock
        item(s) found. As many items as possible, up to the quantity in
        sales order, are assigned.
        
        To limit which stock items can be used, supply a list of stockitems
        to use in the argument stockitems.
        
        To limit how many items are assigned, supply a quantity to the
        argument quantity. This can also be used to over-assign the items,
        as no check for the amounts in the sales order is performed.

        This function returns a list of items assigned during this call.
        If nothing is returned, this means that nothing was assigned,
        possibly because no stock items are available.
        """

        # If stockitems are not defined, get the list of available stock items
        if stockitems is None:
            stockitems = self.getPart().getStockItems(include_variants=False, in_stock=True, available=True)

        # If no quantity is defined, calculate the number of required items
        # This is the number of sold items not yet allocated, but can not
        # be higher than the number of allocated items
        if quantity is None:
            required_amount = min(
                self.quantity - self.allocated, self.available_stock
            )

        else:
            try:
                required_amount = int(quantity)
            except ValueError:
                raise ValueError(
                    "Argument quantity must be convertible to an integer"
                )

        # Look through stock items, assign items until the required amount
        # is reached
        items = list()

        for SI in stockitems:
            
            # Check if we are done
            if required_amount <= 0:
                continue
            
            # Check that this item has available stock
            if SI.quantity - SI.allocated > 0:
                thisitem = {
                    "line_item": self.pk,
                    "quantity": min(
                        required_amount, SI.quantity - SI.allocated
                    ),
                    "stock_item": SI.pk
                }

                # Correct the required amount
                required_amount -= thisitem["quantity"]

                # Append
                items.append(thisitem)

        # Use SalesOrderShipment method to perform allocation
        if len(items) > 0:
            return shipment.allocateItems(items)


class SalesOrderExtraLineItem(inventree.base.InventreeObject):
    """ Class representing the SalesOrderExtraLineItem database model """

    URL = 'order/so-extra-line'

    def getOrder(self):
        """
        Return the SalesOrder to which this SalesOrderLineItem belongs
        """
        return SalesOrder(self._api, self.order)


class SalesOrderAttachment(inventree.base.Attachment):
    """Class representing a file attachment for a SalesOrder"""

    URL = 'order/so/attachment'

    REQUIRED_KWARGS = ['order']


class SalesOrderShipment(
    inventree.base.InventreeObject,
    inventree.base.StatusMixin
):
    """Class representing a shipment for a SalesOrder"""

    URL = 'order/so/shipment'

    def getOrder(self):
        """
        Return the SalesOrder to which this SalesOrderShipment belongs
        """
        return SalesOrder(self._api, self.order)

    def allocateItems(self, items=[]):
        """
        Function to allocate items to the current shipment
        
        items is expected to be a list containing dicts, one for each item
        to be assigned. Each dict should contain three parameters, as
        follows:
            items = [{
                "line_item": 25,
                "quantity": 150,
                "stock_item": 26
            }
        """

        # Customise URL
        url = f'order/so/{self.getOrder().pk}/allocate'

        # Create data from given inputs
        data = {
            'items': items,
            'shipment': self.pk
        }

        # Send data
        response = self._api.post(url, data)

        # Reload
        self.reload()

        # Return
        return response

    def complete(
        self,
        shipment_date=None,
        tracking_number='',
        invoice_number='',
        link='',
        **kwargs
    ):
        """
        Complete the shipment, with given shipment_date, or reasonable
        defaults.
        """

        # Create data from given inputs
        data = {
            'shipment_date': shipment_date,
            'tracking_number': tracking_number,
            'invoice_number': invoice_number,
            'link': link
        }

        # Return
        return self._statusupdate(status='ship', data=data, **kwargs)

    def ship(self, *args, **kwargs):
        """Alias for complete function"""
        self.complete(*args, **kwargs)
