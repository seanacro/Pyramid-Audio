from pathlib import Path
import re
import dbf
import csv
import json
import os
import shutil
# import webbrowser
from datetime import date
from colorama import Fore, Style

# Primary path
PATH = Path("C:/dbase/pyScripts/eBay")

# sample eBay report csv
# input_file = Path('/'.join([str(PATH),"4424eBayReport.csv"]))
# dBase AD Table
dBase_file = Path("C:/dbase/AD.DBF")
ad = dbf.Table(filename=str(dBase_file))
ad.open(dbf.READ_WRITE)

# If there's not an existing record in the ad file,
# there will be no way to find field lengths and avoid
# overflow scenarios. So this Table has one record to act
# as a template for the AD Table. 
template_file = Path("C:/dbase/AD_TEMP.DBF")
ad_template = dbf.Table(filename=str(template_file))
ad_template.open(dbf.READ_WRITE)

# Paths for eBay report 
downloads_path = Path("C:/Users/Shipping/Downloads")
downloads = os.listdir(downloads_path)
report = [file for file in downloads if file.startswith("eBay-OrdersReport-") and file.endswith(".csv")]
# At the end of the script, the report will be moved from
# the path location to the archive location
report_path = Path("/".join([str(downloads_path), report[0]]))
report_archive = Path("C:/Users/Shipping/Documents/eBay sale reports")

# URL to eBay sales page
# eBay_url = "https://www.ebay.com/sh/ord"

# dBase fieldnames that need to be populated
# and modules that we sell. Populated fields will
# be returned as function values
with open(Path('/'.join([str(PATH), 'fields.json']))) as fields_file:
    fields = json.load(fields_file)
modules = [
    'S-100+',
    'SP-40W+',
    'STK0050+',
    'STK0059+',
    'STK0080+',
    'STK1060+',
    'STK1070+',
    'TA-100W+',
    'TA-100WA+',
    'TA-200W+'
]
# Price breakdown (Parts/Labor/Shipping) 
# and packing lists
# of all modules that we sell
with open(Path("/".join([str(PATH), "Module_Price_List.json"]))) as price_file:
    price_list = json.load(price_file)
with open(Path("/".join([str(PATH), "Module_Pack_List.json"]))) as pack_file:
    pack_list = json.load(pack_file)
    
def find_report():
    while True:
        if len(report) > 1:
            print(Fore.RED + "Multiple Reports Found in Downloads directory\nArchive old eBay reports to C:\dbase\pyScripts\eBay\Reports")
            print(Style.RESET_ALL)
        elif len(report) < 1:
            print(Fore.RED + "No eBay report found in Downloads directory\nDownload report from https://www.ebay.com/sh/ord")
            print(Style.RESET_ALL)
        else:
            return report_path

# Ingest csv reports from eBay and 
# return dBase record formatted data
def order_parser(row):

    def name_sort(order):
        # Split buyer name into "first" and "last" names
        return {
            'first': order['Buyer Name'].split(' ')[0].upper(),
            'last': order['Buyer Name'].split(' ')[0-1].upper()
        }
    
    def address(order):
        # Define address according to dBase record format
        return {
            'street': ' '.join([order['Ship To Address 1'], order['Ship To Address 2']]).upper(),
            'city' : order['Ship To City'].upper(),
            'state': order['Ship To State'].upper(),
            'zip': order['Ship To Zip'].split('-')[0]
        }

    def item_name(order):
        # If the item is one of our TA/STK Modules,
        # return the module name
        # Return tech/warr fields as appropriate
        if order['Item Title'].split(' ')[0] in modules:
            return {
                'make': 'MINE',
                'model': order['Item Title'].split(' ')[0],
                'tech': 'C',
                'warranty': ''
            }
        # If the item is an ODR Outer, the naming
        # format is a bit different
        elif order['Item Title'].split(' ')[0:2] == ['Pioneer', 'ODR']:
            return {
                'make': 'MINE',
                'model': 'ODR Outer',
                'tech': 'C',
                'warranty': ''
            }
        # If we sold something else entirely,
        # "MINE" will not be the "MAKE" value
        else:
            return {
                'make': order['Item Title'].split(' ')[0].upper(),
                'model': order['Item Title'].split(' ')[1],
                'tech': '',
                'warranty': 'PARTS'
            }

    def complaint(order):
        # Simple string that shows qty of items
        # for dBase records
        if order['Item Title'].split(' ')[0] in modules:
            if int(order['Quantity']) == 1:
                module = 'MODULE'
            elif int(order['Quantity']) > 1:
                module = 'MODULES'
            return '  '.join([' ', order['Quantity'], item_name(order)['model'], module])
        else:
            return " ".join(["eBay sale", item_name(order)['model']])
    
    def parts(order):
        # Populate "PARTS" dialog with packing list
        # for module sold
        if order['Item Title'].split(' ')[0] in modules:
            parts_list = []
            for part in pack_list[item_name(order)]:
                qty = str(pack_list[item_name(order)][part] * order['Quantity'])
                parts_list.append("\t".join([qty, part]))
            
            # Head's up, dBase treats TABs as three spaces
            # so this may render funny if you're testing 
            # outside of dBase.
            return "\n".join(["\t" + line for line in parts_list])
        else:
            return ""
        
    def model_pricing(item_name):
        # Price breakdowns (Parts/Labor/Shipping) 

        # Breakdown for non-module sales
        # eg used receivers, amps, etc...
        non_module = {
            "labor": 0,
            "parts": float(row["Sold For"][1:]),
            "ship": 0,
            "total": float(row["Sold For"][1:])
        }

        if item_name in price_list:
            # Reference Module_Price_List.json for 
            # price breakdowns
            return price_list[item_name]
        else:
            return non_module

    def field_trim(field, item):
        # Trim inputs to field length if necessary
        field_length = len(getattr(ad_template[0], field))
        if len(item) > field_length:
            return item[:field_length]
        else:
            return item

    # Return a copy of a record's fields with all
    # relevant fields populated
    fields['FIRST'] = field_trim('FIRST', name_sort(row)['first'])
    fields['LAST'] = field_trim('LAST', name_sort(row)['last'])
    fields['STREET'] = field_trim('STREET', address(row)['street'])
    fields['CITY'] = field_trim('CITY', address(row)['city'])
    fields['STATE'] = field_trim('STATE', address(row)['state'])
    fields['ZIP'] = address(row)['zip']
    fields['MAKE'] = field_trim('MAKE', item_name(row)['make'])
    model = item_name(row)['model']
    fields['MODEL'] = field_trim('MODEL', model)
    fields['COMP'] = complaint(row)
    fields['PARTS'] = parts(row)
    fields['TECH'] = item_name(row)['tech']
    today = dbf.Date(date.today())
    fields['DATE_IN'] = today
    fields['DATE_OUT'] = today
    fields['WARR'] = item_name(row)['warranty']
    fields['PAID_LABOR'] = model_pricing(model)['labor'] * float(row['Quantity'])
    fields['PAID_PARTS'] = model_pricing(model)['parts'] * float(row['Quantity'])
    fields['NOTAX'] = model_pricing(model)['ship'] * float(row['Quantity'])
    fields['AMT_DEP'] = model_pricing(model)['total'] * float(row['Quantity'])
    fields['DATE_DEP'] = today
    return fields

# Write eBay report data to dBase AD Table
def dBase():

    # Ticket numbers will always be a 6 digit integer
    # If someone fat fingers too many or too few digits
    # or somehow enters a non-numeric character...
    # this will correct them
    def tik_num():
        while True:
            try:
                ticket = int(input("Enter Ticket Number \n"))
                if 100000 <= ticket <= 999999:
                    return ticket
                else:
                    print(Fore.RED + "Ticket Number must be 6 digits")
                    print(Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Ticket Number must be a number")
                print(Style.RESET_ALL)

    # open eBay report and append records to AD
    order_format = re.compile(r'^\d{2}-\d{5}-\d{5}$')    
    with open(find_report(),'r') as csvread:
        next(csvread)
        orders = csv.DictReader(csvread)
        for line in orders:
            if line['Order Number'] is not None \
            and order_format.match(line['Order Number']):
                fields['TICKET'] = tik_num()
                ad.append(order_parser(line))
    
    # We can close up our Tables
    ad.close()
    ad_template.close()

# The dbf library creates DBF files that dBase
# doesn't recognize. Turns out there's a byte in 
# the header that needs to get changed. 
def dbf_hex_repair():
    with open(dBase_file, mode='rb') as f:
        data = bytearray(f.read())
        data[1] = 24
    with open(dBase_file, mode='wb') as f:
        f.write(data) 

dBase()
dbf_hex_repair()

# Move the eBay report to the archive directory
shutil.move(src=report_path, dst=report_archive)
# webbrowser.open(eBay_url, new=0, autoraise=True)