  $(document).ready(function() {
    //Botao apagar Usuario
    $(".console-button-apagar").click(
      function(event) {
        event.stopPropagation()
        var eventRow = $(this).closest("tr.console-row-event")
        var action = $(this).prop("value")
  
        apagarUsuario(eventRow.prop("id"), action).done(
          function() {
            eventRow.hide()
          }
          ).fail(
          function(e) {
              getAlert("danger", "Error! 😞", e.responseJSON.erro)
          }
        )
      }
    );

    //Botao apagar Aluno
    $(".console-button-apagar-aluno").click(
          function(event) {
            event.stopPropagation()
            var eventRow = $(this).closest("tr.console-row-event")
            var action = $(this).prop("value")
      
            apagarAluno(eventRow.prop("id"), action).done(
              function() {
                eventRow.hide()
              }
              ).fail(
              function(e) {
                  getAlert("danger", "Error! 😞", e.responseJSON.erro)
              }
            )
          }
        );
  });
