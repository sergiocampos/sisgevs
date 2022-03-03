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