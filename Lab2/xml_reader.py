
import xml.dom.minidom as minidom
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
CURRENCY_FILE = FOLDER / "currency.xml"
OUTPUT_FILE = FOLDER / "currency_results.txt"

def read_currencies():
    with open(CURRENCY_FILE, encoding="utf-8") as file:
        xml_data = file.read()

    dom = minidom.parseString(xml_data)
    dom.normalize()

    currencies = {}

    for node in dom.getElementsByTagName("Valute"):
        name = node.getElementsByTagName("Name")[0].firstChild.data
        value = node.getElementsByTagName("Value")[0].firstChild.data

        currencies[name] = float(value.replace(",", "."))
        
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write('Currency dictionary ("Name - Value")\n')
        file.write("=" * 40 + "\n")

        for name, value in currencies.items():
            file.write(f"{name} - {value}\n")


    print('Currency dictionary ("Name - Value"):')
    for name, value in currencies.items():
        print(f"{name} - {value}")

    return currencies
