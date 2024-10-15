Products_list = {
    "Name": "Microsoft Surface Laptop", 
    "Processor": "Qualcomm Snapdragon X Elite",
    "Screensize": "14-inch / 15-inch",
    "Ram": 64,
    "Storage": "1TB",
}, {
    "Name": "Lenovo IdeaPad Duet 5 OLED Chromebook",
    "Processor": "Qualcomm Snapdragon 7c Gen2",
    "Screensize": "13.3-inch",
    "Ram": 8,
    "Storage": "128GB", 
}, {
    "Name":"Apple MacBook Air M3",
    "Processor": "Apple M3",
    "Screensize": "13.6-inch",
    "Ram": 24,
    "Storage": "2TB",
}, {
    "Name": "Dell XPS 13 2024",
    "Processor": "Qualcomm Snapdragon X Elite",
    "Screensize": "13.4-inch",
    "Ram": 16,
    "Storage": "512GB",
}, {
    "Name": "Acer Aspire 5",
    "Processor": "Intel Core i5",
    "Screensize": "14-inch",
    "Ram": 8,
    "Storage": "512GB", 
}

for Laptop in Products_list:
   print(f"Name: {Laptop['Name']}, Processor: {Laptop['Processor']}, Screensize: {Laptop['Screensize']}, Ram: {Laptop['Ram']}, Storage: {Laptop['Storage']}")
