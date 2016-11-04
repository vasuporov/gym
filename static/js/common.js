$(document).ready(function(){
    //$(".customAlert").fadeOut("slow");
});



function showLoader(message){
    $(".loader").show();
    $(".loader-message").text(message);
}
function hideLoader(){
    $(".loader").hide();
}

function showAlert(alert_type, message){
    $(".alert").removeClass("hide alert-warning alert-success alert-danger alert-info").addClass("alert-" + alert_type);
    $(".alert_message").text(message);
}

function removeAlertClasses(){
    $(".alert").removeClass("hide")
}