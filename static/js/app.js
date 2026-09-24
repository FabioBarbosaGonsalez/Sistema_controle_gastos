// Abre os modais (novo lançamento, excluir e limpar)
document.querySelectorAll("[data-abrir-modal]").forEach((botao) => {
    botao.addEventListener("click", () => {
        const modal = document.getElementById(botao.dataset.abrirModal);
        modal.showModal();
        const primeiroCampo = modal.querySelector("input:not([type=hidden]):not([type=radio])");
        if (primeiroCampo) primeiroCampo.focus();
    });
});

// Fecha o modal pelo botão "Cancelar" ou clicando fora dele
document.querySelectorAll("dialog.modal").forEach((modal) => {
    modal.querySelectorAll("[data-fechar-modal]").forEach((botao) => {
        botao.addEventListener("click", () => {
            modal.querySelector("form").reset();
            modal.close();
        });
    });
    modal.addEventListener("click", (evento) => {
        if (evento.target === modal) modal.close();
    });
});

// Pede confirmação antes de excluir um lançamento direto pelo extrato
document.querySelectorAll("form[data-confirmar]").forEach((formulario) => {
    formulario.addEventListener("submit", (evento) => {
        if (!confirm(formulario.dataset.confirmar)) evento.preventDefault();
    });
});

// Fecha as mensagens de retorno
document.querySelectorAll("[data-fechar-mensagem]").forEach((botao) => {
    botao.addEventListener("click", () => botao.closest(".mensagem").remove());
});
