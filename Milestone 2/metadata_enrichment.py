nato_countries = [
    "United States","Canada","United Kingdom","France","Germany","Italy",
    "Spain","Portugal","Netherlands","Belgium","Luxembourg","Denmark",
    "Norway","Poland","Czech Republic","Slovakia","Hungary","Romania",
    "Bulgaria","Greece","Turkey","Estonia","Latvia","Lithuania",
    "Croatia","Slovenia","Albania","Montenegro","North Macedonia",
    "Finland","Sweden"
]

region_map = {
    "United States":"North America",
    "Canada":"North America",

    "Germany":"Europe","France":"Europe","United Kingdom":"Europe",
    "Italy":"Europe","Spain":"Europe","Poland":"Europe",

    "Russia":"Europe",

    "China":"Asia","India":"Asia","Japan":"Asia","South Korea":"Asia",
    "North Korea":"Asia","Pakistan":"Asia",

    "Saudi Arabia":"Middle East","Iran":"Middle East","Israel":"Middle East",
    "Turkey":"Middle East",

    "Brazil":"South America","Argentina":"South America","Chile":"South America",

    "South Africa":"Africa","Egypt":"Africa","Nigeria":"Africa",

    "Australia":"Oceania","New Zealand":"Oceania"
}

df["is_nato"] = df["Country"].apply(lambda x: 1 if x in nato_countries else 0)

df["region"] = df["Country"].map(region_map)
