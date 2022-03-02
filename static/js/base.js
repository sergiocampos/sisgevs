function goBack() {
    window.history.back();
}

$(document).ready(function(){
    $(".telefone").mask("(00) 0000-0000")
    $(".cpf").mask("000.000.000-00")
})