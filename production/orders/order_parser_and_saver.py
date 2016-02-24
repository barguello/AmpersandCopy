import csv
import pdb
import sys
from datetime import datetime
from production.models import Item, OrderItem, Customer, Order


#Slaves
#---------------------------------------------------------------------------
def check_for_correct_columns(line):
    if line[1] != "ID#" or line[2] != "Date" or line[3] != "Quantity" or line[4] != "Item/Acct" or line[5] != "Description" or line[6] != "Amount" or line[7] != "Status" or line[8] != "Customer PO #" or line[9] != "Promised Date" or line[10] != "Referral Source":
        return "Wrong Columns"

    else:
        return "ok"

def parse_order_report(file_path):
    """Parse an order in file_path into a list of lists

    Description
    -----------
    This specialized parser is for use in parsing orders output from
    AccountEdge.  The reader_status is used both to aid the parsing and
    to aid the code reader in understanding how the parsing is done.  If the
    format of file_name changes, this parser may also need to change.
    However, this parser does not care about what columns are in the form.

    Parameters
    ----------
    :param file_path: path of tab-delimitted csv AccountEdge order file

    :type file_path: string

    :return: the table containing the order
    :rtype: list of lists
    """

    order = []
    with open(file_path, 'rU') as file:
        csvreader = csv.reader(file, delimiter = '\t')
        reader_status = "initial skipping"

        for i in range(10):
            csvreader.next()

        for line in csvreader:
            if reader_status == "initial skipping":
                reader_status = "ready to validate columns"

            if reader_status == "ready to validate columns":
                status = check_for_correct_columns(line)
                if status != "ok":
                    print sys.stderr, "incorrect columns"
                    return status
                reader_status = "ready for new customer"
                csvreader.next()
                continue

            if reader_status == "ready for new customer":
                order.append([line[0]])
                reader_status = "ready for first new item"
                continue

            if reader_status == "ready for first new item":
                order[-1] = order[-1] + line[1:]
                if len(order[-1]) == 10:
                    order[-1] = order[-1] + ['none']
                reader_status = "ready for new item"
                continue

            if reader_status  == "ready for new item":
                if line:
                    order.append([order[-1][0]] + line[1:])
                    if len(order[-1]) == 10:
                        order[-1] = order[-1] + ['none']
                else:
                    for i in range(2):
                        csvreader.next()
                    reader_status = "ready for new customer"

    #turn on to see the actual flattened csv
    #with open('flattened_order.csv', 'w') as f:
        #writer = csv.writer(f)
        #writer.writerows(order)

    return order

#add_or_dont functions add an object only if the object does not exist
#add_or_update functions add the object if it does not exist.  If the item
#   does already exist, the function updates
def add_or_dont_add_customer(order):
    try:
        customer = Customer.objects.get(name = order[0])
    except Customer.DoesNotExist:
        customer = []

    if not customer:
        new_customer = Customer(name=order[0])
        new_customer.save()

def add_or_update_order(order):
    customer = Customer.objects.get(name=order[0])
    try:
        order_temp = Order.objects.get(invoice_number=order[1])
    except Order.DoesNotExist:
        order_temp = []

    if not order_temp:
        new_order = Order(invoice_number=order[1],
                          customer=customer,
                          order_date=datetime.strptime(order[2], '%m/%d/%y'),
                          status=order[7], po_number=order[8],
                          promised_date=datetime.strptime(order[9], '%m/%d/%y'), 
                          referral=order[10])
        Order.save(new_order)

    else:
        current_order = Order(id=order_temp.id, invoice_number=order[1],
                      customer=customer,
                      order_date=datetime.strptime(order[2], '%m/%d/%y'),
                      status=order[7], po_number=order[8],
                      promised_date=datetime.strptime(order[9], '%m/%d/%y'),
                      referral=order[10])
        Order.save(current_order)

#the item is actually needed for add_or_update_order_item_and_item
def add_or_update_item(order):
    try:
        item = Item.objects.get(ampersand_sku = order[4])
    except Item.DoesNotExist:
        item = []

    if not item:
        new_item = Item(ampersand_sku=order[4], description=order[5])
        Item.save(new_item)
        item = Item.objects.get(ampersand_sku = order[4])
    return item

def add_or_update_order_item_and_item(order):
    new_item = add_or_update_item(order)
    current_order = Order.objects.get(invoice_number=order[1])

    try:
        order_item_temp = OrderItem.objects.get(order=current_order, item=new_item)
    except OrderItem.DoesNotExist:
        order_item_temp = []

    if not order_item_temp:
        new_order_item = OrderItem(quantity=order[3].replace(",",""),
                                    retail_amount=order[6],
                                    order=current_order,
                                    item=new_item)
        OrderItem.save(new_order_item)
    else:
        current_order_item = OrderItem(id=order_item_temp.id,
                                        quantity=order[3].replace(",",""),
                                        retail_amount=order[6],
                                        order=current_order,
                                        item=new_item)
        OrderItem.save(current_order_item)

def validate(orders):
    if orders != "ok":
        return orders

    return "saved"
#--------------------------------------------------------------------------


#Master
#--------------------------------------------------------------------------
def save_orders(file_path):
    '''
    1. parse the flattened order and save it to orders
    2. if orders takes on a string, then the parsing was invalid and the
       status is returned
    3. initialize the saving by getting and saving the first customer and order
    4. for each line item:
        a. save the customer if the customer is new
        b. save the order if the order is new
        c. save the new item
    '''
    orders = parse_order_report(file_path)
    status = validate(orders)
    if type(orders) == str:
        return status

    current_customer = orders[0][0]
    current_invoice_number = orders[0][1]
    add_or_dont_add_customer(orders[0])
    add_or_update_order(orders[0])
    for order in orders[:-1]:
        customer_name = order[0]

        if customer_name != current_customer:
            current_customer = customer_name
            add_or_dont_add_customer(order)

        invoice_number = order[1]

        if invoice_number != current_invoice_number:
            current_invoice_number = invoice_number
            add_or_update_order(order)

        add_or_update_order_item_and_item(order)
    return "saved"
#---------------------------------------------------------------------------
