travel_log = {
    "France": {"Paris", "Lille", "Dijon"},
    "Germnay": ["Stuttgart", "Berlin"],
}
# for n in travel_log["France"]:
#     if n == "Lille":
#         print(n)
print(travel_log["France"][1])

travel_log = {
    "France": {"Paris": "A", "Lille": "B", "Dijon": "C"},
    "Germnay": ["Stuttgart", "Berlin"],
}
# for n in travel_log["France"]:
#     if n == "Lille":
#         print(n)
print(travel_log["France"]["Paris"])