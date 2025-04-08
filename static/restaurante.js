const modalCadastro = new bootstrap.Modal(document.getElementById('modalcadastro'));

function alterar(idrestaurante) {
    fetch("http://127.0.0.1:5000/restaurante/" + idrestaurante)
    .then(response => response.json())
    .then(dados => {
        document.getElementById('nome').value = dados.nome;
        document.getElementById('telefone').value = dados.telefone;
        document.getElementById('endereco').value = dados.endereco;
        document.getElementById('tipo_cozinha').value = dados.tipo_cozinha;
        document.getElementById('avaliacao').value = dados.avaliacao;
        document.getElementById('idrestaurante').value = dados.idrestaurante;
        modalCadastro.show();
    });
}

function excluir(idrestaurante) {
    fetch("http://127.0.0.1:5000/restaurante/" + idrestaurante, {
        method: "DELETE",
    }).then(function () {
        listar();
    });
}

function salvar() {
    let idrestaurante = document.getElementById('idrestaurante').value;
    let nome = document.getElementById('nome').value;
    let telefone = document.getElementById('telefone').value;
    let endereco = document.getElementById('endereco').value;
    let tipo_cozinha = document.getElementById('tipo_cozinha').value;
    let avaliacao = document.getElementById('avaliacao').value;

    let restaurante = { nome, telefone, endereco, tipo_cozinha, avaliacao };

    let metodo = "POST";
    let url = "http://127.0.0.1:5000/restaurante";

    if (idrestaurante) {
        restaurante.idrestaurante = idrestaurante;
        metodo = "PUT";
    }

    fetch(url, {
        method: metodo,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(restaurante)
    }).then(() => {
        listar();
        modalCadastro.hide();
    });
}

function novo() {
    document.getElementById('idrestaurante').value = '';
    document.getElementById('nome').value = '';
    document.getElementById('telefone').value = '';
    document.getElementById('endereco').value = '';
    document.getElementById('tipo_cozinha').value = '';
    document.getElementById('avaliacao').value = '';
    modalCadastro.show();
}

function listar() {
    const lista = document.getElementById('lista');
    lista.innerHTML = "<tr><td colspan='6'>Carregando...</td></tr>";

    fetch("http://127.0.0.1:5000/restaurante")
     .then(response => response.json())
     .then(dados => mostrar(dados));
}

function mostrar(dados){
    const lista = document.getElementById('lista');
    lista.innerHTML = "";
    for (let r in dados) {
        lista.innerHTML += "<tr>"
                + "<td>" + dados[r].idrestaurante + "</td>"
                + "<td>" + dados[r].nome + "</td>"
                + "<td>" + dados[r].telefone + "</td>"
                + "<td>" + dados[r].endereco + "</td>"
                + "<td>" + dados[r].tipo_cozinha + "</td>"
                + "<td>" + dados[r].avaliacao + "</td>"
                + "<td>"
                + "<button type='button' class='btn btn-primary' onclick='alterar(" + dados[r].idrestaurante + ")'>Editar</button> "
                + "<button type='button' class='btn btn-danger' onclick='excluir(" + dados[r].idrestaurante + ")'>Excluir</button>"
                + "</td>"
                + "</tr>";
    }
}
