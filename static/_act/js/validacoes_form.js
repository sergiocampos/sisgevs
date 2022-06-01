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

// Período do dia *

// Em que dia da semana ocorreu o acidente *

// O Acidente ocorreu em dia de feriado *

// Município de Ocorrência do Acidente *

// Endereço do local do Acidente: *

// Tipo de Acidente: *

// Tipo de veiculos envolvidos no acidente: *

// O Paciente envolvido no acidente era: *

// A vítima apresenta sinais de embriagues e/ou cosumo de bebidas alcoolicas: *


// -------------------------------- SEVERIDADE DO ACIDENTE E QUANTIDADE DE VÍTIMAS ---------------------------- //

// Houve vítimas fatais

// Número de vítimas fatais envolvidas no acidente

// Número de Feridos envolvidos no Acidente


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

