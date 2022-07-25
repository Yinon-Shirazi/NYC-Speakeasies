function display_list(data){
    $("#popular").empty()
    
    list_item = wrap(data,data['2']["name"], '2');
    $("#card1").append(list_item);

    list_item = wrap(data,data['5']["name"], '5');
    $("#card2").append(list_item);

    list_item = wrap(data, data['9']["name"], '9');
    $("#card3").append(list_item);
}
        

function wrap(data, name, idx){


    card = '<img class="card-img-top" src='+data[idx]["image"]+' alt="'+name+' Card">' +
    '<div class="card-body" alt="'+name+' Card">' +
      '<h4 class="card-title" alt="'+name+' image">'+name+'</h4>' +
      '<p class="card-text" alt="'+name+' image">Rating: '+data[idx]["rating"]+' Stars</p>' +
      '<a href="/view/'+idx+'" class="btn stretched-link buttn" style="position: static" alt="'+name+' image" >See Profile</a>' + '</div>';

    return card
}
$(document).ready(function(){
    display_list(data)
    $("#search_input").focus();
  
})