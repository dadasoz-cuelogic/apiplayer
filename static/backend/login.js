$(document).ready(function(){
    alert("CCCCC");
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
            document.location = "/dev/"
        } else if(data.message == "org"){
            document.location = "/org/dashboard/"
        } else {
            document.location = "/"
        }
    })
});