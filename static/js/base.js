function goBack() {
    window.history.back();
}

$(document).ready(function () {
    $(".telefone").mask("(00) 00000-0000")
    $(".cpf").mask("000.000.000-00")
})

$(document).ready(function () {
    $("#pesquisar-registros").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#table-registros tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});
function cancelar_revalidar(url, id) {
    var data = {
        'id': id,
        'url_redirect': url
    }
    $.ajax({
        url: '/cancelar_caso_esporotricose',
        data: data,
        success: (data) => {
            document.location.href = url
        }
    })
}