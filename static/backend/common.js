$(document).ready({

});

$.showNotification = function showNotification(title,msg){
    $.gritter.add({
            title: title,
            text: msg,
            sticky: false,
            time: 5000,
            class_name: 'my-sticky-class'
    });
}