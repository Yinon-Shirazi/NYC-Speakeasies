from copy import deepcopy
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 10
data = {
     "1":{
        "id":"1",
        "name": "Please Dont Tell",
        "image": "https://s3-media0.fl.yelpcdn.com/bphoto/QXu-wzODRUKQomRdzldJUw/o.jpg",
        "address": "113 St Marks Pl, New York, NY 10009",
        "about": "This hidden gen is located in the heart of the East Village in NYC.  It combines the New York cocktails scene with late-night street food. To enter the bar, patrons have to step into a hot dog shop, and enter into the phone both on their left. It is one of the most famous (ironically) speakeasies in NYC.",
        "rating" : "4.0",
        "popular_drinks": ["Jin & Tonic", "Margarita", "Cosmopolitan" ],
        "drink_price": "14",
        "neighborhood": "East Village", 
        "seating_config": ["Standing","Bar-seating", "Table-service"]
        },
    "2":{
        "id":"2",
        "name": "Dear Irving",
        "image": "https://media.timeout.com/images/105761704/1024/768/image.jpg",
        "address": "55 Irving Place, New York, NY 10003",
        "about": "This hidden gen is located in the heart of the Gramercy. It combines the New York cocktails scene a la carte finger food. It has been fetures on many movies and TV shows. It has the best Old-Fashioned cocktail in the city.",
        "rating" : "4.6",
        "popular_drinks": ["Old-Fashioned", "Wine", "Rose-Wine" ],
        "drink_price": "16",
        "neighborhood": "Gramercy", 
        "seating_config": ["Booths","Bar-seating", "Table-service"]
        },
    "3":{
        "id":"3",
        "name": "Coby Club",
        "image":"https://images.squarespace-cdn.com/content/v1/5a7bc20f6f4ca3e636938b3d/1617903532966-7B8YEEIWSNAS4E6T01W7/cody+bigger.jpg?format=2500w",
        "address": "156 1/2 7th Ave, New York, NY 10011",
        "about": "Every name has story.  San Francisco Chinatown 1959. Drawing inspiration from the most provocative and exciting period of San Francisco nightlife, Coby Club pays homage to the iconic artistry of its most celebrated performer, Miss Coby Yee. Revisit a long lost time when sultry music slipped past plush curtains into fog shrouded streets, the night kept your secrets and the breaking dawn held limitless possibilities.",
        "rating" : "4.1",
        "popular_drinks": ["Old-Fashioned", "Dirty Martini", "Wine" ],
        "drink_price": "14",
        "neighborhood": "Chelsea", 
        "seating_config": ["Low-tables", "Table-service"]
        },
    "4":{
        "id":"4",
        "name": "Attaboy",
        "image":"https://media.timeout.com/images/101223777/1024/768/image.jpg",
        "address": "134 Eldridge St, New York 10010",
        "about": "Occupying the former Milk and Honey space (the bar said to have kick started this whole genre revival on New Years Eve, 1999), there’s now a whole generation of drinkers who could be forgiven for thinking Attaboy has been here forever. Its narrow interior, anchored by a brushed steel bar, is chicly worn, and plenty of old-timey tipples are available. Some still say it’s a little hard to find, so here’s a tip: The address is 134 Eldridge Street, and it reads “AB” on the door. ",
        "rating" : "3.6",
        "popular_drinks": ["Beer", "Whiskey", "Wine" ],
        "drink_price": "11",
        "neighborhood": "Lower East Side", 
        "seating_config": ["Bar-seating", "Table-service"]
        },
    "5":{
        "id":"5",
        "name": "Angel's Share",
        "image":"https://media.timeout.com/images/100419913/1024/768/image.jpg",
        "address": "8 Stuyvesant St New York. 10003",
        "about": "This was one of a few speakeasy-inspired bars to add outdoor seating in 2020, sunshine dehydrating any last lingering molecules of anonymity. But now that the indoors are open once more, it’s fun to climb Angel Share’s staircase, stride through adjacent Japanese restaurant Village Yokocho, and see if you can squeeze in past the bar’s big wooden door. Arrive alone or in pairs for a better chance of nabbing a spot. ",
        "rating" : "4.6",
        "popular_drinks": ["Sake", "Whiskey", "Japanise-Whiskey" ],
        "drink_price": "15",
        "neighborhood": "East Village", 
        "seating_config": ["Low-tables", "Outdoor tables"]
        },
    "6":{
        "id":"6",
        "name": "The Back-Room",
        "image":"https://media.timeout.com/images/100497827/1024/768/image.jpg",
        "address": "102 Norfolk St. New York. 10002",
        "about": "In theory, you and a companion–yet to be determined friend or foe–will turn up Norfolk street just as a cloud of steam rises from a subway grate, and your eyes will land on a sign: THE LOWER EAST SIDE TOY COMPANY. This must be the place, you’ll say, pulling your trench coat tighter, no longer sure whether you’re nervous or excited, or if this is really the place at all. In practice, there will probably already be people milling around outside The Back Room, and you may have to wait for your cocktail-in-a-teacup, but the environs are just transportive enough to make it seem, for a minute, like you’re back in the original roaring 20s.",
        "rating" : "3.8",
        "popular_drinks": ["Beer", "Whiskey", "Rose" ], 
        "drink_price": "14",
        "neighborhood": "East Village", 
        "seating_config": ["Low-tables", "Bar-seating"]
        },
    "7":{
        "id":"7",
        "name": "Bathtub Gin",
        "image":"https://media.timeout.com/images/100459453/1024/768/image.jpg",
        "address": "132 Ninth Ave, New York. 10011",
        "about": "If you’re really thirsty for the whole hide-and-seek conceit, or simply tolerating someone who is, this is the place to be. Up front, it’s a functional coffee shop. In the back after dark, it’s Jazz Age cosplay, baby. Not that most people come wearing costumes, but they certainly could and blend right in with the copper bathtub in the center of the room. Go ahead: Take a little social media dip.",
        "rating" : "4.0",
        "popular_drinks": ["Gin", "Whiskey", "Wine" ],
        "drink_price": "13",
        "neighborhood": "Chelsea", 
        "seating_config": ["High-seating", "Table service"]
        },
    "8":{
        "id":"8",
        "name": "The Garret",
        "image":"https://media.timeout.com/images/105230282/1024/768/image.jpg",
        "address": "296 Bleecker St, New York, 10012",
        "about": "This one ranks high on the calculated seclusion spectrum, too. Situated above a Five Guys, the path up a back staircase leading to tin ceilings, banquet hall-esque chandeliers and cozy tufted booths is pretty neat if you just sort of happen upon it, so grab a pal prone to whimsy and try to orchestrate that very experience without mentioning the place is already all over Yelp, Instagram, and TikTok.",
        "rating" : "4.0",
        "popular_drinks": ["Beer", "Wine", "Rose" ],
        "drink_price": "14",
        "neighborhood": "West Village", 
        "seating_config": ["Bar-seating", "Booths"]
        },
    "9":{
        "id":"9",
        "name": "Employees Only",
        "image":"https://media.timeout.com/images/103377942/1024/768/image.jpg",
        "address": "510 Hudson St, New York. 10014",
        "about": "Originally opened by industry pros on the earlier side of the 2000s speakeasy resurgence, Employees Only has real NYC bar bonafides. The comfortably-worn reproduction of a prohibition-era bar is also among the city’s most populist, with enough nerd-baiting sips on the menu to please aficionados without alienating everyone else. ",
        "rating" : "4.2",
        "popular_drinks": ["Cosmopolitan", "Wine", "Martini", "Manhatten" ], 
        "drink_price": "16",
        "neighborhood": "West Village", 
        "seating_config": ["High-seating", "Bar-service"]
        },
    "10":{
        "id":"10",
        "name": "UES",
        "image":"https://media.timeout.com/images/105230290/1024/768/image.jpg",
        "address": "1707 Second Ave, New York, 10128",
        "about": "Similar to Bathtub Gin, UES. has an ice cream shop front, but when you ask whether they have this or that in the back, you get an intoxicating surprise. And it’s alcohol! Make like a soda jerk and pass the frozen treats for Upper East Side-themed cocktails like the 1040 Fifth Avenue and Here’s Looking at You, Bradshaw, in what is colloquially known as UES.’s 'storage room'." ,
        "rating" : "4.9",
        "popular_drinks": ["Old Fashioned", "'Ice-Cream Cosmopolitan'", "'Asphalt-Green'", "'The Met'", "Manhatten" ], 
        "drink_price": "14",
        "neighborhood": "Upper East Side", 
        "seating_config": ["Booths", "Table service"]
        },
    
} 


def search(term):
    term = term.lower()
    print("searching for: ", term)

    term = term.strip()
    
    lower = deepcopy(data)

    for id in range(1,len(data)+1):
        for k,v in data[str(id)].items():
            if isinstance(v, list):
                arr = []
                for i in v:
                    arr.append(i.lower())
                lower[str(id)][k.lower()] = arr
            else:
                lower[str(id)][k.lower()] = v.lower()
    
    foundNames = []
    for s in range(1,len(data)+1):
        if term in lower[str(s)]["name"]:
            foundNames.append(data[str(s)])
    
    foundDrinks = []
    for s in range(1,len(data)+1):
        for d in range(len(lower[str(s)]["popular_drinks"])):
            if term in lower[str(s)]["popular_drinks"][d]:
                # append tuples of (popular drink, name of bar, id)
                foundDrinks.append((data[str(s)]["popular_drinks"][d],data[str(s)]["name"],data[str(s)]["id"] ))
        
    foundHoods = []
    for s in range(1,len(data)+1):
        if term in lower[str(s)]["neighborhood"]:
            foundHoods.append(data[str(s)])

    return foundNames, foundDrinks, foundHoods

# ROUTES

@app.route('/')
def home():
   return render_template('home.html', data = data)

@app.route('/add')
def add():
   return render_template('add.html', data = data)   


@app.route('/result/<search_term>')
def result(search_term=None):
    foundNames, foundDrinks, foundHoods = search(search_term)
    return render_template('result.html', search_term = search_term ,data=data, foundNames=foundNames, foundDrinks =foundDrinks, foundHoods = foundHoods ) 



@app.route('/view/<idx>')
def view(data=data, idx = None):
    return render_template('view.html', data=data, idx = idx)

@app.route('/edit/<idx>')
def edit(data=data, idx = None):
    return render_template('edit.html', data=data, idx = idx)  


@app.route('/add_bar', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id 

    json_data = request.get_json()   

    drinks = json_data[7]["popular_drinks"]
    new_drinks = drinks.split(',')
    for s in new_drinks:
        s = s.strip()
    
    seating = json_data[8]["seating_config"]
    new_seating = seating.split(',')
    for c in new_seating:
        c = c.strip() 
    
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "id":  str(current_id),
        "name": json_data[0]["name"],
        "image": json_data[1]["image"],
        "address": json_data[2]["address"],
        "about": json_data[3]["about"],
        "rating": json_data[4]["rating"],
        "drink_price": json_data[5]["price"],
        "neighborhood": json_data[6]["neighborhood"],
        "popular_drinks": new_drinks,
        "seating_config": new_seating
    }
    data[str(current_id)] = new_name_entry

    #send back the id of the new listing
    return jsonify(data = str(current_id))

@app.route('/update_bar', methods=['POST'])
def update_name():
    global data 
    global current_id 
    json_data = request.get_json()   

    drinks = json_data[8]["popular_drinks"]
    new_drinks = drinks.split(',')
    for s in new_drinks:
        s = s.strip()

    seating = json_data[9]["seating_config"]
    new_seating = seating.split(',')
    for c in new_seating:
        c = c.strip() 
    
    # add new entry to array with 
    new_name_entry = {
        "id":  json_data[0]["id"],
        "name": json_data[1]["name"],
        "image": json_data[2]["image"],
        "address": json_data[3]["address"],
        "about": json_data[4]["about"],
        "rating": str(json_data[5]["rating"]),
        "drink_price": str(json_data[6]["price"]),
        "neighborhood": json_data[7]["neighborhood"],
        "popular_drinks": new_drinks,
        "seating_config": new_seating
    }
    data[json_data[0]["id"]] = new_name_entry

    #send back the id of the new listing
    return jsonify(data = json_data[0]["id"] )


if __name__ == '__main__':
   app.run(debug = True)




