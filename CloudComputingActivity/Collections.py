from DatabaseConnect import get_database
dbname = get_database()

#collections are based off of production studio

item_1 = {
"_id" : "GB01",
"Name" : "Kiki's Delivery Service",
"Runtime" : "103 Mins",
"Producer" : "Hayao Miyazaki",
"Poster" : "https://bit.ly/3Bb1eyO",
"IMDb Rating" : "7.9/10"
}

item_2 = {
"_id" : "GB02",
"Name" : "Princess Mononoke",
"Runtime" : "133 Mins",
"Producer" : "Toshio Suzuki",
"Poster" : "https://bit.ly/3oCY1ED",
"IMDb Rating" : "8.4/10"
}

dbname["Ghibli"].insert_many([item_1,item_2])

item_3 = {
"_id" : "DS01",
"Name" : "Big Hero 6",
"Runtime" : "102 Mins",
"Producer" : "Roy Conli",
"Poster" : "https://bit.ly/3uKgwbu",
"IMDb Rating" : "7.8/10"
}

item_4 = {
"_id" : "DS02",
"Name" : "Moana",
"Runtime" : "107 Mins",
"Producer" : "Osnat Shurer",
"Poster" : "https://bit.ly/3uPFoyI",
"IMDb Rating" : "7.6/10"
}

dbname["Disney"].insert_many([item_3,item_4])

item_5 = {
"_id" : "MV01",
"Name" : "Guardians of the Galaxy",
"Runtime" : "122 Mins",
"Producer" : "Kevin Feige",
"Poster" : "https://bit.ly/3FmLsn4",
"IMDb Rating" : "8/10"
}

item_6 = {
"_id" : "MV02",
"Name" : "Spider-Man: Homecoming",
"Runtime" : "133 Mins",
"Producer" : "Kevin Feige",
"Poster" : "https://bit.ly/3mxQXXg",
"IMDb Rating" : "7.4/10"
}

dbname["Marvel"].insert_many([item_5,item_6])

#extra collection of some personal comments I have about each movie

item_1 = {
"_id" : "CM01",
"Movie" : "Kiki's Delivery Service",
"Comment": "I like watching this movie when it's raining."
}

item_2 = {
"_id" : "CM02",
"Movie" : "Princess Mononoke",
"Comment": "The opening scene is really cool."
}

item_3 = {
"_id" : "CM03",
"Movie" : "Big Hero 6",
"Comment": "Baymax is super cute!"
}

item_4 = {
"_id" : "CM04",
"Movie" : "Moana",
"Comment": "How Far I'll Go was stuck in my head for days."
}

item_5 = {
"_id" : "CM05",
"Movie" : "Guardians of the Galaxy",
"Comment": "Rocket Racoon is my favourite member."
}

item_6 = {
"_id" : "CM06",
"Movie" : "Spider-Man: Homecoming",
"Comment": "I loved the fight scenes in this movie."
}

dbname["Comments"].insert_many([item_1,item_2,item_3,item_4,item_5,item_6])
