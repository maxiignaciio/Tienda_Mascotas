// http://worldtimeapi.org/api/ip

$("#btn-actualizar").click(function (event) {
    event.preventDefault();
   
    var url = "http://worldtimeapi.org/api/ip";
   
      fetch(url)
          .then(response => response.json())
          .then(data => 
              {
                  var $date_time = $('<h1>').text(datetime);

                  $("#info").empty();
                  $('#info')
                      .append($date_time)

   
              })
          .catch(error => console.error(error));
   
  });
  