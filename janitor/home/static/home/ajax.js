
function AJAX_action()
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "ajax_info.txt", true);
    xmlhttp.send();
}