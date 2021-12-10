function apagarUsuario(id) {
  return $.ajax(
    {
      url: "/api/v1/usuarios/" + id,
      method: "DELETE",
      contentType: "application/json",
      data: JSON.stringify({})
    }
  )
}

function apagarAluno(id) {
  return $.ajax(
    {
      url: "/api/v1/alunos/" + id,
      method: "DELETE",
      contentType: "application/json",
      data: JSON.stringify({})
    }
  )
}