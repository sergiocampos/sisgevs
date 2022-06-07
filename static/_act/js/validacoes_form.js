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
// Número de vítimas fatais envolvidas no acidente

// Número de Feridos envolvidos no Acidente

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


// ----------------------------------- EQUIPE ACIONADA PARA O LOCAL DO ACIDENTE ------------------------------- //

// Quem foi responsável por prestar apoio no local: *


// ------------------------------------------- INFORMACÕES DO PACIENTE ---------------------------------------- //

// Nome do Paciente *

// Idade do Paciente: *

// Sexo: *

// Nome da Mãe: *

// Endereço do Paciente: *

// Contato Telefônico: *


// ------------------------------------- OUTRAS INFORMAÇÕES SOBRE O PACIENTE ---------------------------------- //

// O Paciente Envolvido no Acidente *


// -------------------------------------------- UNIDADE NOTIFICADORA ------------------------------------------ //

// Nome da Instituição *

// Nome do Secretário(a) Municipal de Saúde *

// Cargo ou Função do Notificador *

// Contato do Notificador *

