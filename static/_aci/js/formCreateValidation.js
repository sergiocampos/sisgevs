// Mascáras
$('#contato_telefonico').mask('(00)00000-0000')
$('#contato_notificador').mask('(00)00000-0000')
$('#cpf_paciente').mask('000.000.000-00')
$('#cns_paciente').mask('000.0000.0000.0000')

// Limitando datas max e min
$('input[type="date"]').attr('max', new Date().toISOString().split("T")[0]).attr('min', '1850-12-01').on('focusout', function(){
   if ((this.value > new Date().toISOString().split("T")[0]) || (this.value < '1850-12-01')){
    $(this).parent().find('spam').text('*')
    $('#que_dia_semana_ocorreu_acidente').val('')
    return this.value = ''
   }   
})

// Alterando o dia da semana 
$('#data_acidente').on('change', function(){
  let arraySemana = ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo']
  let diaSemana = new Date(this.value).getDay()
  $('#que_dia_semana_ocorreu_acidente').val(arraySemana[diaSemana])
})

// Checando se houve vitima fatal e ativando ou desativando os campos
$('input[name="houve_vitimas_fatais"]').on('click', function(){
  let alerta = $('label[for="numeros_vitimas_fatais_envolvidas_acidente"]').find('spam')
  if(this.value == 'Sim'){
    $('#numeros_vitimas_fatais_envolvidas_acidente').attr('disabled', false).attr('required', true)
    $('input[name="caso_obito"]').attr('disabled', false)
    alerta.text('*')
  } else {
    alerta.text('')
    $('#numeros_vitimas_fatais_envolvidas_acidente').attr('disabled', true).attr('required', false)[0].reset()
    $('input[name="caso_obito"]').attr('disabled', true)
    if($('input[name="caso_obito"]:checked')[0]){$('input[name="caso_obito"]:checked')[0].checked = false;}
  }
})

// Calculando idade
$('#data_nascimento').on('change', function(){
  let ano_nascimento = this.value.split('-')[0]
  let ano_atual = new Date().toISOString().split("T")[0].split('-')[0]
  $('#idade_paciente').val(ano_atual-ano_nascimento)
})

// Checando se o paciente foi transferido para outro hospital
$('input[name="paciente_foi_referenciado_para_outro_hospital"]').on('click', function(){
  if(this.value == 'Sim'){
    $('#qual_hospital').attr('disabled', false)
  } else {
    $('#qual_hospital').attr('disabled', true)
  }
})


// Função que ativa e desativa o campo outros na aba "Unidade Notirificadora"
$('#nome_instituicao_hospital').on('change', function(){
  let row_outros = $('#outros-un')
  let outros_input = row_outros.find('input')
  let outros_alert = row_outros.find('spam')

  if(this.value == 'Outro'){
    row_outros.removeClass('d-none')
    outros_input.attr('required', true).val('')
    outros_alert.text('*')
  } else {
    row_outros.addClass('d-none')
    outros_input.attr('required', false).val('')
    outros_alert.text('')
  }
})
