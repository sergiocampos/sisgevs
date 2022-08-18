// Scroll UP Button
window.addEventListener('scroll', function() {
    scrollBtn = $('#scrollUp')
    return window.scrollY > 300 ? scrollBtn.removeClass('d-none') : scrollBtn.addClass('d-none')  
})

//FUNÇÃO GERAL DE ATIVAÇÃO DO BOTAO DE ENVIO DE DADOS

function ativarButtonUnidadeNotificadora() {
    if(
        uniNotifi == true &&
        infogeral == true &&
        servAcidente == true &&
        equipAcionada == true &&
        infPaciente == true &&
        hospitalTransferencia == true &&
        validPacientEnvolvido == true

   // console.log('enviar')
    ){
        $('#btn_submit_id').prop('disabled',false)

        return false
    } else{
        $('#btn_submit_id').prop('disabled',true)

        return true

    }
}





//Act_validacoes



// --------------------------------------------- INFORMAÇÕES GERAIS ------------------------------------------- //

//Validação da pagina informções gerais
function validInforGerais (){
    if(
        dataacidenteValid == true &&
        valide_periodo == true &&
        acidenteDiaFeriado == true &&
        valorMunicipioValid == true &&
        enderecoAcidenteValid == true &&
        valorTipAcidente == true &&
        tipoVeiculoValid == true &&
        tipoCondutorValid == true
        // valorBairroValid == true

    ){
        $('#alert_informacoes_gerais').attr('hidden',true)
        infogeral = true


    } else{
        $('#alert_informacoes_gerais').attr('hidden',false)
        infogeral = false


    }ativarButtonUnidadeNotificadora()
}

//FUNÇÃO PARA ATIVAR RADIO OUTROS



function activeOutros(){

    var tipoAcident = document.getElementById('outros');
    var radioOutro = document.getElementById("radio_outros");

    if (radioOutro.checked) {
        tipoAcident.removeAttribute("class","d-none");

       descrevaOutro = false;

    } else{
        descrevaOutro = true;

        radioOutro.setAttribute("class","d-none");


    }verificatipoAcidente()
}


// Data do Acidente
var dataacidenteValid = false;

$('#date_acidente').on('change', function () {
    var arraySemana = ['Domingo','Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado']
    var data = this.value.split('-')
    var diaSemana = new Date(data[2],data[1],data[0]).getDay()


    $('#dia_semana').val(arraySemana[diaSemana])

    if(this.value != ''){
        dataacidenteValid=true
        $('#alert_data_acidente').attr('hidden',true)
        $('#alert_dia_semana').attr('hidden',true)
    }else{
        dataacidenteValid=false
        $('#alert_data_acidente').attr('hidden',false)
        $('#alert_dia_semana').attr('hidden',false)
    }
    validInforGerais()
})

// Período do dia *

var valide_periodo = false;
var alert_periodo_dia = document.getElementById('alert_periodo_dia');
function verificaPeriodoDia(){
    valide_periodo = true

    if (valide_periodo) {
         alert_periodo_dia.setAttribute('hidden', true)
        valide_periodo = true

    } else {
        alert_periodo_dia.removeAttribute('hidden', false)
        valide_periodo = false
    }
    validInforGerais()
}

// Em que dia da semana ocorreu o acidente *

var diaSemanaValid = false;
var alert_dia_semana = document.getElementById('alert_dia_semana');
function verificadiaSemana(){
    diaSemanaValid = true;

    if (diaSemanaValid) {
        diaSemanaValid = true;

        alert_dia_semana.setAttribute('hidden', true)
    } else {
        diaSemanaValid = false;

        alert_dia_semana.removeAttribute('hidden')
    }validInforGerais()
}

// O Acidente ocorreu em dia de feriado *

var acidenteDiaFeriado = false;
var alert_acidente_dia_feriado = document.getElementById('alert_acidente_dia_feriado');
function verificaAcidenteDiaFeriado(){
    acidenteDiaFeriado = true;

    if (acidenteDiaFeriado) {
        acidenteDiaFeriado = true;
        alert_acidente_dia_feriado.setAttribute('hidden', true)
    } else {
        acidenteDiaFeriado = false;
        alert_acidente_dia_feriado.removeAttribute('hidden')
    }
    validInforGerais()
}


// Município de Ocorrência do Acidente *

var valorMunicipioValid = false
function validarMunicipio(valorMunicipio){

    var alertMunicipio = document.getElementById("alert_municipio");

    if (valorMunicipio != ""){
        valorMunicipioValid=true
        alertMunicipio.setAttribute('hidden', true)
    } else {
        valorMunicipioValid=false
        alertMunicipio.removeAttribute('hidden')
    }
    validInforGerais()
}


// Endereço do local do Acidente: *

var enderecoAcidenteValid = false;
var alert_endereco_acidente = document.getElementById('alert_endereco_acidente');
var alert_front = document.getElementById('alert_front')
function verificaEndrecoLocalAcidente(valor_campo_endereco){
    var endereco_acidente = false;
    let re = /^[a-z .*,A-Z0-9\u00C0-\u00FF]{15,}$/

    if (re.test(valor_campo_endereco)) {
        alert_endereco_acidente.setAttribute('hidden', true)
        enderecoAcidenteValid = true

    } else {
        alert_endereco_acidente.removeAttribute('hidden')
        enderecoAcidenteValid = false
    }
    validInforGerais()
}

// BAIRRO *

var valorBairroValid = false
function validarBairro(valorBairro){

   var alertBairro = document.getElementById("");

    if (valorBairro != ""){
        valorBairroValid=true

    } else {
        valorBairroValid=false

    }
    validInforGerais()
}





// Tipo de Acidente: select

var valorTipAcidente = false

function verificatipoAcidente(tipAcidente){

    var alertTipAcidente = document.getElementById("alert_tipo_acidente");
    var textAcidente = document.getElementById("text-acidente");
    var inputAcidentOutro = document.getElementById("select_outro").value;

    if (tipAcidente != "" && tipAcidente != "Outros"){
        if(!$(textAcidente).hasClass('d-none')){
            $(textAcidente).addClass('d-none')
        }
        valorTipAcidente=true
        alert_tipo_acidente.setAttribute('hidden', true)
    } else if (tipAcidente == "Outros"){
        textAcidente.removeAttribute('class','d-none')
        var re = /^[a-z \u00C0-\u00FFA-Z]{1,30}$/

        valorTipAcidente
        if(re.test(inputAcidentOutro)){
            valorTipAcidente=true


            alert_tipo_acidente.setAttribute('hidden', true)

        } else {

            valorTipAcidente=false
            alert_tipo_acidente.removeAttribute('hidden')
        }

    }else {
        valorTipAcidente=false
        alert_tipo_acidente.removeAttribute('hidden')
    }
    validInforGerais()
}



// Tipo de veiculos envolvidos: 2

var tipoVeiculoValid = false

function verificatipoVeiculo(tipVeiculo){

    var alert_tipo_veiculo = document.getElementById("alert_tipo_veiculo");
    var textVeiculo = document.getElementById("text-veiculo");
    var inputOutrosVeiculos = document.getElementById("comment").value;

    if (tipVeiculo != "" && tipVeiculo != "Outros"){
        if(!$(textVeiculo).hasClass('d-none')){
            $(textVeiculo).addClass('d-none')
        }
        tipoVeiculoValid=true
        alert_tipo_veiculo.setAttribute('hidden', true)
    } else if (tipVeiculo == "Outros"){
        textVeiculo.removeAttribute('class','d-none')
        var re = /^[a-z \u00C0-\u00FFA-Z]{1,30}$/


        if(re.test(inputOutrosVeiculos)){
            tipoVeiculoValid=true

            alert_tipo_veiculo.setAttribute('hidden', true)

        } else {

            tipoVeiculoValid=false
            alert_tipo_veiculo.removeAttribute('hidden')
        }

    }else {
        tipoVeiculoValid=false
        alert_tipo_veiculo.removeAttribute('hidden')
    }
    validInforGerais()
}









// O Paciente envolvido no acidente era: *


var tipoCondutorValid = false;
var alert_tipo_condutor = document.getElementById('alert_paciente_envolvido');
function verificatipoPaciente(){
    tipoCondutorValid = true

    if (tipoCondutorValid) {
        tipoCondutorValid = true
        alert_paciente_envolvido.setAttribute('hidden', true)
    } else {
        tipoCondutorValid = false
        alert_paciente_envolvido.removeAttribute('hidden')
    }
    validInforGerais()
}

// A vítima apresenta sinais de embriagues e/ou cosumo de bebidas alcoolicas: *

var sinalAcoolicoValid = false;
var alert_sinal_alcoolico = document.getElementById('alert_sinal_alcoolico');
function verificatipoEmbriagues(){
    sinalAcoolicoValid = true;

    if (sinalAcoolicoValid) {
        sinalAcoolicoValid = true;
        alert_sinal_alcoolico.setAttribute('hidden', true)
    } else {
        sinalAcoolicoValid = false;
        alert_sinal_alcoolico.removeAttribute('hidden')
    }
    validInforGerais()
}

// -------------------------------- SEVERIDADE DO ACIDENTE E QUANTIDADE DE VÍTIMAS ---------------------------- //

//Validação da pagina Severidade
function validSeverAcident (){
    if(
        vitimaFatal == true &&
        envolvidoFeridos == true &&
        envolvidoFatal == true &&
        //lesoes == true &&
        casoObito == true

    ){
        $('#alert_severidade').attr('hidden',true)
        servAcidente = true
    } else{
        $('#alert_severidade').attr('hidden',false)
        servAcidente = false

    }ativarButtonUnidadeNotificadora()
}





// H. Vítimas fatais

var vitimaFatal = false;
var alert_houve_vitimas_fatais = document.getElementById('alert_houve_vitimas_fatais');
function verificaVitimaFatal(){
    vitimaFatal = true;
    if (vitimaFatal) {
        vitimaFatal = true;
        alert_houve_vitimas_fatais.setAttribute('hidden', true)
    } else {
        vitimaFatal = false;
        alert_houve_vitimas_fatais.removeAttribute('hidden')
    }
    validSeverAcident ()
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
    validSeverAcident ()
}

//Quadro lesões

var lesoes = false;
var quadroLesoes = document.getElementById('quadroLesoes');
function verificalesoes(){
    lesoes = true;
    if (lesoes) {
        lesoes = true;
      //  quadroLesoes.setAttribute('hidden', true)
    } else {
        lesoes = false;
      //  quadroLesoes.removeAttribute('hidden')
    }
    validSeverAcident ()
}



//Em caso de obito

var casoObito = false;
var alert_obito = document.getElementById('alert_obito');
function verificaObito(){
    casoObito = true;
    if (casoObito) {
        casoObito = true;
        alert_obito.setAttribute('hidden', true)
    } else {
        casoObito = false;
        alert_obito.removeAttribute('hidden')
    }
    validSeverAcident ()
}




// ----------------------------------- EQUIPE ACIONADA PARA O LOCAL DO ACIDENTE ------------------------------- //


// Quem foi responsável por prestar apoio no local: *

//var responsavelApoio = false
var alert_responsavel_apoio = document.getElementById('alert_responsavel_apoio')
var equipe_acionada = document.getElementById('equipe-acionada')
$('.reponsaveis-prestar-socorro').on('change',function () {
    var cbx = document.getElementsByClassName('reponsaveis-prestar-socorro')

    for (var i in cbx){
        if (cbx[i].checked){
            if(cbx[i].value == "outros"){
                $('#outros_row').removeClass('d-none')
            }else{
                $('#outros_row').addClass('d-none')
            }
            responsavelApoio = true
            break
        }
        var responsavelApoio = false

    }

    if(responsavelApoio){
        alert_responsavel_apoio.setAttribute('hidden', true)
        equipe_acionada.setAttribute('hidden',true)
        equipAcionada = true

    }else{
        alert_responsavel_apoio.removeAttribute('hidden')
        equipe_acionada.removeAttribute('hidden')
        equipAcionada = false

    }ativarButtonUnidadeNotificadora()
})



// Quem foi responsável por prestar apoio no local: *(opção outros)

function toLimit(string = ""){
    string.value = string.value.substring(0,300);
}







// ------------------------------------------- INFORMACÕES DO PACIENTE ---------------------------------------- //
//Validação da pagina Informacoes do Paciente
function validinfoPaciente() {
    if(
        nomePaciente == true &&
        idadPaciente  == true &&
        tipoSexo == true &&
        nomeMae == true &&
        enderecoPaciente == true &&
        contatoTel == true


    ){
        $('#alert_informacoes_paciente').attr('hidden',true)
        infPaciente = true

    } else{
        $('#alert_informacoes_paciente').attr('hidden',false)
        infPaciente = false


    }ativarButtonUnidadeNotificadora()
}


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
    validinfoPaciente()
})

// Idade do Paciente: *

idadPaciente  = false
var dn = document.getElementById('dn');
dn.max = new Date().toISOString().split("T")[0];

$('#dn').on('change', function () {
    if(this.value != ''){
       nascimento = this.value.split('-')[0]
       diaAtual = new Date().toISOString().split('T')[0].split('-')[0]

        $('#idade').val(diaAtual-nascimento)


        $('#alert_data_nascimento').attr('hidden',true)
        idadPaciente  = true

    }else{
        idadPaciente  = false

        $('#alert_data_nascimento').attr('hidden',false)
        $('#idade').val('')

    }
    validinfoPaciente()

})

// Sexo: *


var tipoSexo = false;
var alertSexo = document.getElementById('alert_sexo');
function verificasexo(){
    tipoSexo = true;
    if (tipoSexo) {
        tipoSexo = true;

        alert_sexo.setAttribute('hidden', true)
    } else {
        tipoSexo = false;

        alert_sexo.removeAttribute('hidden')
    }
    validinfoPaciente()
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
    validinfoPaciente()
})


// Endereço do Paciente: *

var enderecoPaciente = false

$('#endereco_paciente').on('keyup', function () {

    var re = /^[a-z .*,A-Z.*, 0-9\u00C0-\u00FF]{10,}$/

    if(re.test(this.value)) {
        enderecoPaciente = true;
        $('#alert_endereco_paciente').attr('hidden', true)
    }else{
        enderecoPaciente = false;
        $('#alert_endereco_paciente').attr('hidden', false)
    }
    validinfoPaciente()
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
    validinfoPaciente()
})

// CPF:

var infoPacienteCpf = false
$('#cpf').mask('000.000.000-00')
$('#cpf').on ('keyup', function () {

    var re = /^\d{3}.\d{3}.\d{3}-?\d{2}$/

    if(re.test(this.value)) {
        infoPacienteCpf = true

    }else{
        infoPacienteCpf = false

    }

})

// CNS:

var infoPacienteCns = false
$('#cns').mask('000.0000.0000-0000')
$('#cns').on ('keyup', function () {

    var re = /^\d{3}.\d{4}.\d{4}-?\d{4}$/

    if(re.test(this.value)) {
        infoPacienteCns = true

    }else{
        infoPacienteCns = false

    }

})










// ------------------------------------- OUTRAS INFORMAÇÕES SOBRE O PACIENTE ---------------------------------- //

// O Paciente Envolvido no Acidente *
var validPacientEnvolvido = false;
var hospitalTransferencia = false;

var alert_outros_paciente = document.getElementById('alert_outros_paciente');
var alert_hospital_transferencia = document.getElementById('alert_hospital_transferencia');
var alert_pac_envolvido = document.getElementById('alert_pac_envolvido');

function verificaHospital(elemento){

    hospitalTransferencia = true;
    
    if (elemento.value) {
        hospitalTransferencia = true;
        validPacientEnvolvido = true;
        alert_hospital_transferencia.setAttribute('hidden', true)
        alert_pac_envolvido.setAttribute('hidden', true)
        alert_outros_paciente.setAttribute('hidden', true)

    } else {
        validPacientEnvolvido = false
        hospitalTransferencia = false;
        alert_hospital_transferencia.removeAttribute('hidden')
        alert_outros_paciente.removeAttribute('hidden')
        alert_pac_envolvido.removeAttribute('hidden')
    }ativarButtonUnidadeNotificadora()
}

// Ativa e desativa o hospital de referencia

function active_hospital(){

    var opt=document.getElementById('hospital_transferencia');
    var radioSim = document.getElementById("radio_sim");
    alert_pac_envolvido.setAttribute('hidden', true)
    
    if (radioSim.checked) {
        opt.removeAttribute("class","d-none");
        alert_pac_envolvido.removeAttribute('hidden');        
        alert_outros_paciente.removeAttribute('hidden')
        validPacientEnvolvido = false;

    } else{
        validPacientEnvolvido = true;
        opt.setAttribute("class","d-none");
        document.getElementById('hospital').value=''
        alert_hospital_transferencia.removeAttribute('hidden')
        alert_outros_paciente.setAttribute('hidden', true)
    }
}

// informações complementares(texto area)






// -------------------------------------------- UNIDADE NOTIFICADORA ------------------------------------------ //

//Validação da pagina Unidade Notificadora, alert


var uniNotifi = false;
function validinfoUnidadeNotificadora() {
    if(
        nomeInstituicao == true &&
        nomeSecretario == true &&
        funcaoNotificador == true &&
        contatoNotificador == true

    ){
        $('#alert_unidade_notificadora').attr('hidden',true)
        uniNotifi = true

    } else{
        $('#alert_unidade_notificadora').attr('hidden',false)
        uniNotifi = false



    }ativarButtonUnidadeNotificadora()
}




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
    validinfoUnidadeNotificadora()


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
    }validinfoUnidadeNotificadora()

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
    validinfoUnidadeNotificadora()


})





// Contato do Notificador *


var contatoNotificador = false

$('#contato_notificador').mask('(00) 00000-0000')
$('#contato_notificador').on ('keyup', function () {

    var re = /^[0-9 ()-]{15}$/

    if(re.test(this.value)) {
        contatoNotificador = true
        $('#alert_contato_notificador').attr('hidden', true)
    }else{
        contatoNotificador = false
        $('#alert_contato_notificador').attr('hidden', false)
    }
    validinfoUnidadeNotificadora()


})






