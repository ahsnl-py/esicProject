$(document).ready(function() {
    document.getElementById('mainJs').innerHTML = activeLinkControl()

});

function activeLinkControl() {
    $(".nav .nav-link").click(function () {
        //remove activate class from any nav-item
        $('.nav').find(".active").removeClass("active")
        // add active class to clicked item 
        $(this).addClass('active')
    })
}