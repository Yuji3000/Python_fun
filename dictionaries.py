# convert Jan => January

months = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December",
}

# will return value of given key
print(months["Nov"])
print(months.get("Nov"))
print(months.get("Luv", "Not a value key")) #(months.get(key, default value))

