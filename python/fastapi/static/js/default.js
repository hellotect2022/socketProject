function signUp(){
    $.ajax({
        url: "http://hellotect2022.synology.me:9380/api/",
        context: document.body
      }).done(function() {
        $( this ).addClass( "done" );
      });
    return 
}