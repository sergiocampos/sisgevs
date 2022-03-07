var nome_confere = false;
var email_confere = false;
var cpf_confere = false;
var celular_confere = false;
var login_confere = false;
var perfil_confere = false;
var municipio_confere = false;
var gerencia_regional_confere = false;
var gerencia_operacional_confere = false;
var nucleo_confere = false;
var area_tecnica_confere = false;
var gerencia_regional

$(document).ready(function () {
    $('#cpf').mask('000.000.000-00')
    $('#celular').mask('(00)0.0000-0000')
    options = document.getElementsByClassName('option');
    $(options).each(function () {
        if (this.selected) {
            gerencia_regional = this.text
        }
    });
});

// Alterando campo gerencia.
$("#municipio").change(function () {
    municipio = this.value;
    options = document.getElementsByClassName('option');
    $(options).each(function () {
        if (this.value == municipio) {
            $(this).prop('selected', true)
            gerencia_regional = this.text
        }
    });
});

// Limitando caracteres
function limitcarc(e, tipo) {
    var chr = String.fromCharCode(e.which);
    if (tipo == 'letr_acent') {
        if ("áéíóúâêîôûãõ qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM".indexOf(chr) < 0)
            return false;
    } else if (tipo == 'num') {
        if ("0123456789".indexOf(chr) < 0)
            return false;
    } else if (tipo == 'letr') {
        if ("qwertyuioplkjhgfdsazxcvbnm QWERTYUIOPLKJHGFDSAZXCVBNM".indexOf(chr) < 0)
            return false;
    }
}

// Validação de email
function validacaoEmail() {
    email = document.getElementById('email').value;
    var re = /\S+@\S+\.\S+/;
    email_confere = re.test(email);
    
    if (email_confere){
        $('#email_check').prop('hidden', false);
        verificarCampos();
    } else{
        $('#email_check').prop('hidden', true);
        verificarCampos();
    }
};

$("#login").on('keyup', function () {
    login = document.getElementById('login').value

    if (login.length > 4) {
        data = { 'login': login }
        $.ajax({
            url: '/checar_login_ajax/',
            data: data,
            success: function (data) {
                if (data['data'] == 0) {
                    $('#login_uncheck').prop('hidden', true);
                    $('#login_check').prop('hidden', false);
                    login_confere = true;
                } else {
                    $('#login_uncheck').prop('hidden', false);
                    $('#login_check').prop('hidden', true);
                    $("#cadastrar").prop('disabled', true).removeClass('btn-success').addClass('btn-secondary')
                    login_confere = false;
                }
            }
        })
        $('#login_uncheck').prop('hidden', true);
        verificarCampos()
    } else {
        $('#login_check').prop('hidden', true);
        $('#login_uncheck').prop('hidden', true);
        $("#cadastrar").prop('disabled', true).removeClass('btn-success').addClass('btn-secondary')
    }
});

function verificarCampos() {
    nome = document.getElementById('nome').value;
    cpf = document.getElementById('cpf').value;
    celular = document.getElementById('celular').value;

    if (nome.length > 10) { $('#nome_check').prop('hidden', false); nome_confere = true } else { $('#nome_check').prop('hidden', true); nome_confere = false };
    if (cpf.length == 14) { $('#cpf_check').prop('hidden', false); cpf_confere = true } else { $('#cpf_check').prop('hidden', true); cpf_confere = false };
    if (celular.length == 15) { $('#celular_check').prop('hidden', false); celular_confere = true } else { $('#celular_check').prop('hidden', true); celular_confere = false };

    campos = [nome_confere, email_confere, cpf_confere, celular_confere, login_confere];

    itens_vazios = 0;
    $(campos).each(function () {
        if (this == false) {
            itens_vazios++;
        }
    });
    if (itens_vazios == 0) {
        $("#cadastrar").prop('disabled', false).removeClass('btn-secondary').addClass('btn-success')
    } else { $("#cadastrar").prop('disabled', true).removeClass('btn-success').addClass('btn-secondary') }
};

$('#cadastrar').on('click', function () {
    nome = document.getElementById('nome');
    email = document.getElementById('email');
    cpf = document.getElementById('cpf');
    celular = document.getElementById('celular');
    login = document.getElementById('login');
    perfil = document.getElementById('perfil');
    municipio = document.getElementById('municipio');
    gerencia_operacional = document.getElementById('gerencia_operacional');
    nucleo = document.getElementById('nucleo');
    area_tecnica = document.getElementById('area_tecnica');

    data = {
        'nome': nome.value,
        'email': email.value,
        'cpf': cpf.value,
        'login': login.value,
        'telefone': celular.value,
        'perfil': perfil.value,
        'municipio': municipio.value,
        'gerencia_regional': gerencia_regional,
        'gerencia_operacional': gerencia_operacional.value,
        'nucleo': nucleo.value,
        'area_tecnica': area_tecnica.value,
    }

    $.ajax({
        url: '/criar_perfil_municipal/',
        data: data,
        success: function (data) {
            $(nome).val('')
            $(email).val('')
            $(cpf).val('')
            $(login).val('')
            $('#response_login').val(data['login'])
            $('#response_senha').val(data['senha'])
            $('.success').prop('hidden', false)
        }
    });
});