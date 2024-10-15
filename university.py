University_list = {
 "Name": "University of the Philippines Diliman", 
 "President": "Angelo Jimenez",
 "Location": "Quezon City",
 "Status": "Public",
 "Date": 1908,
}, {
 "Name": "Ateneo de Manila University", 
 "President": "Roberto Yap",
 "Location": "Quezon City",
 "Status": "Private",
 "Date": 1859,
}, {
 "Name": "Philippine Normal University", 
 "President": "Bert J. Tuga",
 "Location": "Manila",
 "Status": "Public",
 "Date": 1901,
}, {
 "Name": "De La Salle University Manila", 
 "President": "Br. Bernard S. Oca FSC",
 "Location": "Manila",
 "Status": "Private",
 "Date": 1911,
}, {
 "Name": "Polytechnic University of the Philippines",
 "President": "Manuel Muhi",
 "Location": "Manila",
 "Status": "Public",
 "Date": 1904,
}

for University in University_list:
   print(f"Name: {University['Name']}, President: {University['President']}, Location: {University['Location']}, Status: {University['Status']}, Date: {University['Date']}")
