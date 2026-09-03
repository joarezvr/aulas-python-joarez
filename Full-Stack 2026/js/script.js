// Validação básica nativa e mensagens de interação
document.addEventListener("DOMContentLoaded", function() {
    const formLogin = document.getElementById("formLogin");

    if (formLogin) {
        formLogin.addEventListener("submit", function(event) {
            event.preventDefault();
            const usuario = document.getElementById("usuario").value;

            if (usuario.trim() === "") {
                alert("Por favor, preencha o campo de usuário.");
            } else {
                alert("Bem-vindo, " + usuario + "! Login realizado com sucesso.");
                window.location.href = "index.html";
            }
        });
    }
});
