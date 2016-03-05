$(document).ready(function(){
});

$(document).on('click', ".btn-login", function(){
    username = $("#inputEmail3").val();
    password = $("#inputPassword3").val();
    data = {
        "username" : username,
        "password" : password
    }
    $.post("/authenticate/", data, function(data){
        if(data.user == "admin"){
            document.location = "/admin/"
        } else if(data.user == "dev"){
            document.location = "/dev/dashboard/"
        } else if(data.user == "org"){
            document.location = "/org/dashboard/"
        } else {
            document.location = "/"
        }
    })
});