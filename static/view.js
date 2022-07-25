function display(data, idx){

    title = "<h1> "+ data[idx]["name"] + "</h1>";
    $("#name").append(title);

    edit = '<a href="/edit/'+idx+'"+ class="btn edit" >&#10001; Edit</a>'
    $("#edit").append(edit);

    img = "<img src= '"+ data[idx]["image"]+"' alt='"+data[idx]["name"]+" interior' class='pic' >"
    $("#image").append(img);

    rating = "<span class= 'miniHeader'> Rating: </span> "+ data[idx]["rating"] + " Stars ";
    $("#rating").append(rating);

    price = "<span class= 'miniHeader'> Average Drink Price:</span> $" + data[idx]["drink_price"];
    $("#price").append(price);
    
    about =  data[idx]["about"]
    $("#about").append(about);

    get_drinks(data, idx);

    neighborhood = '<a href="/result/'+data[idx]["neighborhood"]+'" >'+data[idx]["neighborhood"]+'</a>';
    $("#neighborhood").append(neighborhood)

    get_seating(data,idx)

    address =data[idx]["address"]
    $("#address").append(address);

}

function get_drinks(data, idx){
    for(let i = 0; i < data[idx]["popular_drinks"].length; i++){
        drink = data[idx]["popular_drinks"][i]
        wrapped = '<a href="/result/'+drink+'" class="btn buttn drink" >'+drink+'</a>';
        $("#popular_drinks").append(wrapped);
    }
}

function get_seating(data,idx){
    for(let i = 0; i < data[idx]["seating_config"].length; i++){
        seat = data[idx]["seating_config"][i]
        if (i != data[idx]["seating_config"].length -1){
            seat += ", "
        }
        $("#seating_config").append(seat);
    }
}


$(document).ready(function(){
    display(data, idx)
})