// Efeitos visuais dinâmicos solicitados no projeto
$(document).ready(function() {

    // Alerta dinâmico ao clicar em comprar
    $(".btn-comprar").click(function() {
        alert("Item adicionado ao carrinho de compras!");
    });

    // Rolagem suave para o topo
    $("#btnVoltarTopo").click(function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop: 0}, '300');
    });

    // Interação simples no link de cadastro
    $("#btnCadastro").click(function(e) {
        e.preventDefault();
        alert("Funcionalidade de cadastro será implementada no Back-End em breve!");
    });
});
