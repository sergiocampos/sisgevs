// Ativa e desativa o hospital de referencia
function active_hospital(){
    var opt=document.getElementById('hospital_transferencia');
    var radio_sim = document.getElementById("radio_sim");

    if (radio_sim.checked) {
        opt.removeAttribute("class","d-none");

    } else{
        opt.setAttribute("class","d-none")
    }
}
// VALIDAÇÕES
// --------------------------------------------- INFORMAÇÕES GERAIS ------------------------------------------- //

// Data do Acidente
var dateAcidente = document.getElementById('date_acidente');
dateAcidente.max = new Date().toISOString().split("T")[0];

// Período do dia *

var valide_periodo = false;
var alert_periodo_dia = document.getElementById('alert_periodo_dia');
function verificaPeriodoDia(){
    valide_periodo = true;
    if (valide_periodo) {
        alert_periodo_dia.setAttribute('hidden', true)
    } else {
        alert_periodo_dia.setAttribute('hidden', false)
    }
}

// Em que dia da semana ocorreu o acidente *
var diaSemanaValid = false;
var alert_dia_semana = document.getElementById('alert_dia_semana');
function verificadiaSemana(){
    diaSemanaValid = true;
    if (diaSemanaValid) {
        alert_dia_semana.setAttribute('hidden', true)
    } else {
        alert_dia_semana.setAttribute('hidden', false)
    }
}

// O Acidente ocorreu em dia de feriado *

var acidenteDiaFeriado = false;
var alert_acidente_dia_feriado = document.getElementById('alert_acidente_dia_feriado');
function verificaAcidenteDiaFeriado(){
    acidenteDiaFeriado = true;
    if (acidenteDiaFeriado) {
        alert_acidente_dia_feriado.setAttribute('hidden', true)
    } else {
        alert_acidente_dia_feriado.removeAttribute('hidden')
    }
}


// Município de Ocorrência do Acidente *

function validarMunicipio(valorMunicipio){
    var alert_municipio = document.getElementById("alert_municipio");

    if (valorMunicipio != ""){
        alert_municipio.setAttribute('hidden', true)
    } else {
        alert_municipio.removeAttribute('hidden')
    }
}


// Endereço do local do Acidente: *

var alert_endereco_acidente = false;
var alert_endereco_acidente = document.getElementById('alert_endereco_acidente');
var alert_front = document.getElementById('alert_front')
function verificaEndrecoLocalAcidente(valor_campo_endereco){
    var endereco_acidente = false;
    let re = /^[a-z .*,A-Z0-9\u00C0-\u00FF]{15,}$/

    if (re.test(valor_campo_endereco)) {
        alert_endereco_acidente.setAttribute('hidden', true)
        endereco_acidente = true

    } else {
        alert_endereco_acidente.removeAttribute('hidden')
        endereco_acidente = false
    }
}







// Tipo de Acidente: *

var tipoAcidente = false;
var alert_tipo_acidente = document.getElementById('alert_tipo_acidente');
function verificatipoAcidente(){
    tipoAcidente = true;
    if (tipoAcidente) {
        alert_tipo_acidente.setAttribute('hidden', true)
    } else {
        alert_tipo_acidente.removeAttribute('hidden')
    }
}


// Tipo de veiculos envolvidos no acidente: *


var tipoVeiculo = false;
var alert_tipo_veiculo = document.getElementById('alert_tipo_veiculo');
function verificatipoVeiculo(){
    tipoVeiculo = true;
    if (tipoVeiculo) {
        alert_tipo_veiculo.setAttribute('hidden', true)
    } else {
        alert_tipo_veiculo.removeAttribute('hidden')
    }
}



// O Paciente envolvido no acidente era: *


var tipoCondutor = false;
var alert_tipo_condutor = document.getElementById('alert_paciente_envolvido');
function verificatipoPaciente(){
    tipoCondutor = true;
    if (tipoCondutor) {
        alert_paciente_envolvido.setAttribute('hidden', true)
    } else {
        alert_paciente_envolvido.removeAttribute('hidden')
    }
}

// A vítima apresenta sinais de embriagues e/ou cosumo de bebidas alcoolicas: *

var sinalAcoolico = false;
var alert_sinal_alcoolico = document.getElementById('alert_sinal_alcoolico');
function verificatipoEmbriagues(){
    sinalAcoolico = true;
    if (sinalAcoolico) {
        alert_sinal_alcoolico.setAttribute('hidden', true)
    } else {
        alert_sinal_alcoolico.removeAttribute('hidden')
    }
}

// -------------------------------- SEVERIDADE DO ACIDENTE E QUANTIDADE DE VÍTIMAS ---------------------------- //
// H. Vítimas fatais

var vitimaFatal = false;
var alert_houve_vitimas_fatais = document.getElementById('alert_houve_vitimas_fatais');
function verificaVitimaFatal(){
    vitimaFatal = true;
    if (vitimaFatal) {
        alert_houve_vitimas_fatais.setAttribute('hidden', true)
    } else {
        alert_houve_vitimas_fatais.removeAttribute('hidden')
    }
}
// Número de vítimas fatais envolvidas no acidente e Feridos

var envolvidoFeridos = false;
var alert_envolvidos_feridos = document.getElementById('alert_envolvidos_feridos');

var envolvidoFatal = false;
var alert_qtd_vitima_fatal = document.getElementById('alert_qtd_vitima_fatal');

function verificaNumeros(elemento, campo){

    if (elemento.value > 100){
        elemento.value = 100
    }else if(elemento.value < 0){
        elemento.value = 0
    }

    if(elemento.value != ''){
        if(campo == 'vitimasFatais') {
            alert_qtd_vitima_fatal.setAttribute('hidden', true)
            envolvidoFatal = true
        }else if(campo == 'vitimasFeridas'){
            alert_envolvidos_feridos.setAttribute('hidden', true)
            envolvidoFeridos = true
        }
    }else{
        if(campo == 'vitimasFatais') {
            alert_qtd_vitima_fatal.removeAttribute('hidden')
            envolvidoFatal = false
        }else if(campo == 'vitimasFeridas'){
            alert_envolvidos_feridos.removeAttribute('hidden')
            envolvidoFeridos = false
        }
    }
}

//Quadro lesões

var lesoes = false;
var quadroLesoes = document.getElementById('quadroLesoes');
function verificalesoes(){
    lesoes = true;
    if (lesoes) {
        quadroLesoes.setAttribute('hidden', true)
    } else {
        quadroLesoes.removeAttribute('hidden')
    }
}



//Em caso de obito

var casoObito = false;
var alert_obito = document.getElementById('alert_obito');
function verificaObito(){
    casoObito = true;
    if (casoObito) {
        alert_obito.setAttribute('hidden', true)
    } else {
        alert_obito.removeAttribute('hidden')
    }
}




// ----------------------------------- EQUIPE ACIONADA PARA O LOCAL DO ACIDENTE ------------------------------- //

// Quem foi responsável por prestar apoio no local: *
var responsavelApoio = false
var alert_responsavel_apoio = document.getElementById('alert_responsavel_apoio')
var equipe_acionada = document.getElementById('equipe-acionada')
$('.reponsaveis-prestar-socorro').on('change',function () {
    var cbx = document.getElementsByClassName('reponsaveis-prestar-socorro')
    for (var i in cbx){
        if (cbx[i].checked){
            responsavelApoio = true
            break
        }
        var responsavelApoio = false
    }

    if(responsavelApoio){
        alert_responsavel_apoio.setAttribute('hidden', true)
        equipe_acionada.setAttribute('hidden',true)

    }else{
        alert_responsavel_apoio.removeAttribute('hidden')
        equipe_acionada.removeAttribute('hidden')

    }
})

// ------------------------------------------- INFORMACÕES DO PACIENTE ---------------------------------------- //

// Nome do Paciente *
var nomePaciente = false


$('#nome_paciente').on('keyup', function () {

    var re = /^[a-z .*,A-Z.*\u00C0-\u00FF]{10,}$/

    if(re.test(this.value)) {
        nomePaciente = true
        $('#alert_nome_paciente').attr('hidden', true)
    }else{
        nomePaciente = false
        $('#alert_nome_paciente').attr('hidden', false)
    }
})
// Idade do Paciente: *

var dn = document.getElementById('dn');
dn.max = new Date().toISOString().split("T")[0];

$('#dn').on('focusout', function () {
    if(this.value != ''){
        nascimento = this.value.split('-')[0]
        var today = new Date().toISOString().split('T')[0].split('-')[0]
        $('#idade').val(today-nascimento)
        $('#alert_data_nascimento').attr('hidden',true)
    }else{
        $('#alert_data_nascimento').attr('hidden',false)
        $('#idade').val('')

    }

})

// Sexo: *


var tipoSexo = false;
var alertSexo = document.getElementById('alert_sexo');
function verificasexo(){
    tipoSexo = true;
    if (tipoSexo) {
        alert_sexo.setAttribute('hidden', true)
    } else {
        alert_sexo.removeAttribute('hidden')
    }
}




// Nome da Mãe: *

var nomeMae = false


$('#nome_mae').on('keyup', function () {

    var re = /^[a-z .*,A-Z.*\u00C0-\u00FF]{10,}$/

    if(re.test(this.value)) {
        nomeMae = true
        $('#alert_nome_mae').attr('hidden', true)
    }else{
        nomeMae = false
        $('#alert_nome_mae').attr('hidden', false)
    }
})


// Endereço do Paciente: *

var enderecoPaciente = false

$('#endereco_paciente').on('keyup', function () {

    var re = /^[a-z .*,A-Z.*, 0-9\u00C0-\u00FF]{10,}$/

    if(re.test(this.value)) {
        enderecoPaciente = true
        $('#alert_endereco_paciente').attr('hidden', true)
    }else{
        enderecoPaciente = false
        $('#alert_endereco_paciente').attr('hidden', false)
    }
})




// Contato Telefônico: *



var contatoTel = false
$('#tel').mask('(00) 00000-0000')
$('#tel').on ('keyup', function () {

    var re = /^[0-9 ()-]{15}$/

    if(re.test(this.value)) {
        contatoTel = true
        $('#alert_tel').attr('hidden', true)
    }else{
        contatoTel = false
        $('#alert_tel').attr('hidden', false)
    }
})

// ------------------------------------- OUTRAS INFORMAÇÕES SOBRE O PACIENTE ---------------------------------- //

// O Paciente Envolvido no Acidente *


var hospitalTransferencia = false;
var alert_hospital_transferencia = document.getElementById('alert_hospital_transferencia');
function verificaHospital(){
    hospitalTransferencia = true;
    if (hospitalTransferencia) {
        alert_hospital_transferencia.setAttribute('hidden', true)
    } else {
        alert_hospital_transferencia.removeAttribute('hidden')
    }
}


// informações complementares(texto area)


// -------------------------------------------- UNIDADE NOTIFICADORA ------------------------------------------ //

// Nome da Instituição *

var nomeInstituicao = false


$('#nome_instituicao').on('keyup', function () {

    var re = /^[a-zA-Z\u00C0-\u00FF]{4,}(?: [a-zA-Z]+){0,6}$/


    if(re.test(this.value)) {
        nomeInstituicao = true
        $('#alert_instituicao').attr('hidden', true)
    }else{
        nomeInstituicao = false
        $('#alert_instituicao').attr('hidden', false)
    }
})







// Nome do Secretário(a) Municipal de Saúde *

var nomeSecretario = false


$('#nome_secretario').on('keyup', function () {

    var re = /^[a-z .*,A-Z.*\u00C0-\u00FF]{10,}$/


    if(re.test(this.value)) {
        nomeSecretario = true
        $('#alert_nome_secretario').attr('hidden', true)
    }else{
        nomeSecretario = false
        $('#alert_nome_secretario').attr('hidden', false)
    }
})


// Cargo ou Função do Notificador *


var funcaoNotificador = false


$('#funcao_notificador').on('keyup', function () {

    var re = /^[a-zA-Z\u00C0-\u00FF]{4,}(?: [a-zA-Z]+){0,6}$/
    if(re.test(this.value)) {
        funcaoNotificador = true
        $('#alert_funcao_notificador').attr('hidden', true)
    }else{
        funcaoNotificador = false
        $('#alert_funcao_notificador').attr('hidden', false)
    }
})





// Contato do Notificador *


var contatoNotificador = false

$('#contato_notificador').mask('(00) 00000-0000')
$('#contato_notificador').on ('keyup', function () {

    var re = /^[0-9 ()-]{16}$/

    if(re.test(this.value)) {
        contatoNotificador = true
        $('#alert_contato_notificador').attr('hidden', true)
    }else{
        contatoNotificador = false
        $('#alert_contato_notificador').attr('hidden', false)
    }
})
