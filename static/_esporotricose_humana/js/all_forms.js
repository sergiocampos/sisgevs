function exibeConteudo(agravo) {
    if (agravo == "Esporotricose Humana") {
        $("#options").removeClass('d-none');
    } else {
        $("#options").addClass('d-none');
    }
}

window.onbeforeunload = (event) => {
    event.preventDefault()
}