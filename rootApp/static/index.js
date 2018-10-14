$(document).ready(function(){
     const DEFAULTTHEME = "navbar navbar-expand-lg navbar-dark bg-dark";
     let attr = localStorage.getItem('attr') || DEFAULTTHEME;
     document.getElementById('navbar').setAttribute("class", attr);


    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });


    $('tbody').on('click', 'a[id^=delete]',function(event) {
        let id = this.id.replace(/\D/g,'');
        $.ajax({
             url: '/conspect_delete',
             type: 'POST',
             data: {'id': id},
             dataType: 'json',
             success: function(response){
                 if(response){

                    $('table tbody').html('').load('conspect_entries');
                 }
             }
        });
    });


    function getCookie(c_name) {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

});

function changeTheme(theme){
    if(theme){
        let navbar = document.getElementById('navbar');
        if(theme === "M"){
            attr = "navbar navbar-expand-lg navbar-dark bg-dark";
            localStorage.setItem('attr', attr);
            navbar.setAttribute("class", attr);
        }
        else{
            attr = "navbar navbar-expand-lg navbar-dark bg-warning";
            localStorage.setItem('attr', attr);
            navbar.setAttribute("class", attr);
        }
    }
}