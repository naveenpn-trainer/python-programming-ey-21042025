shares = [
    {"name":"GOOG","price":140},
    {"name":"YAHOO","price":100},
    {"name":"ALIBABA","price":120}
]
max_share = max(shares, key=lambda s : s["price"])
print(max_share)