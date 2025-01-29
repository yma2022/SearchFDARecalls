import os
import glob
import xml.etree.ElementTree as ET

def parse_xml_files(data_path):
    """
    Parse each XML file in the given directory
    and extract recall data into a list of dictionaries.
    """
    recall_data = []
    
    xml_files = glob.glob(os.path.join(data_path, "*.xml"))
    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Iterate through each <recall> element
        for recall in root.findall("recall"):
            brand = recall.find("Brand").text if recall.find("Brand") is not None else ""
            company = recall.find("Company").text if recall.find("Company") is not None else ""
            date = recall.find("Date").text if recall.find("Date") is not None else ""
            product_description = recall.find("ProductDescription").text if recall.find("ProductDescription") is not None else ""
            reason = recall.find("Reason").text if recall.find("Reason") is not None else ""
            url = recall.find("Url").text if recall.find("Url") is not None else ""
            
            recall_data.append({
                "brand": brand,
                "company": company,
                "date": date,
                "product_description": product_description,
                "reason": reason,
                "url": url
            })
    
    return recall_data

if __name__ == "__main__":
    data_path = "./data"
    recall_data = parse_xml_files(data_path)
    print(f"Parsed {len(recall_data)} recall entries.")