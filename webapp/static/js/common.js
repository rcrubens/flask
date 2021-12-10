function getAlert(type, title, message) {
  alertBox = $("<div>")
    .addClass("alert alert-dismissable fade show")
    .addClass("alert-" + type)
    .attr("role", "alert")
    .attr("title", title)

  alertMessage = $("<pre>" + message + "</pre>")

  alertBox.append(alertMessage)

  alertBox.dialog({
    modal: true,
    buttons: {
      Ok: function() {
        $( this ).dialog( "close" );
      }
    }
  });
}
