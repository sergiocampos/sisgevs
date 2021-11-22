////////////////////////////////////////////////////////////////////////////////////////////////////////////
// JQuery - Data máxima = dia de hoje.

var today = new Date().toISOString().split('T')[0];
$(".data").attr('max', today);



////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Calculando idade

function idade(id, idInput){
    var today = new Date();
    var data_nascimento = new Date(idInput.value);
    var idade = parseInt((today - data_nascimento) / (24 * 3600 * 1000)/365);
    document.getElementById(id).value = idade;  
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Mascaras no input

$(document).ready(function($){
    $("#fone").mask("(00)00000-0000");
    $("#cep").mask("00000-000");
    $("#numero_casa").mask("0000000000");
    $("#idade").mask("000");
    $("#uf").mask("AA");
});


////////////////////////////////////////////////////////////////////////////////////////////////////////////
// JS viacep 

$(document).ready(function () {
function limpa_formulário_cep() {
    // Limpa valores do formulário de cep.
    $("#rua").val("");
    $("#bairro").val("");
    $("#cidade").val("");
    $("#uf").val("");
    $("#ibge").val("");
}

//Quando o campo cep perde o foco.
$("#cep").blur(function () {
    //Nova variável "cep" somente com dígitos.
    var cep = $(this).val().replace(/\D/g, "");

    //Verifica se campo cep possui valor informado.
    if (cep != "") {
    //Expressão regular para validar o CEP.
    var validacep = /^[0-9]{8}$/;

    //Valida o formato do CEP.
    if (validacep.test(cep)) {
        //Preenche os campos com "..." enquanto consulta webservice.
        $("#rua").val("...");
        $("#bairro").val("...");
        $("#cidade").val("...");
        $("#uf").val("...");
        $("#ibge").val("...");

        //Consulta o webservice viacep.com.br/
        $.getJSON(
        "https://viacep.com.br/ws/" + cep + "/json/?callback=?",
        function (dados) {
            if (!("erro" in dados)) {
            //Atualiza os campos com os valores da consulta.
            $("#rua").val(dados.logradouro);
            $("#bairro").val(dados.bairro);
            $("#cidade").val(dados.localidade);
            $("#uf").val(dados.uf);
            $("#ibge").val(dados.ibge);
            } //end if.
            else {
            //CEP pesquisado não foi encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
            }
        }
        );
    } //end if.
    else {
        //cep é inválido.
        limpa_formulário_cep();
        alert("Formato de CEP inválido.");
    }
    } //end if.
    else {
    //cep sem valor, limpa formulário.
    limpa_formulário_cep();
    }
});
});


////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Função para impedir que o usuário digite um valor indesejado.
//Para usar, basta importar este arquivo no Html e adicionar um |onkeypress = "return limitcarc(event, TIPO)"| ao input desejado.
//O parâmetro TIPO deve ser preenchido com:

//letr_acent - Para letras com acentos
//num - Para números
//letr - Para letras sem acentos

function limitcarc(e, tipo) {
    var chr = String.fromCharCode(e.which);
    if (tipo == 'letr_acent'){
        if ("áéíóúâêîôûãõ qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM".indexOf(chr) < 0)
          return false;
    }else if (tipo == 'num') {
        if ("0123456789".indexOf(chr) < 0)
          return false;
    }else if (tipo == 'letr'){
        if ("qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM".indexOf(chr) < 0)
          return false;
    }
}