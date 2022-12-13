// Mascáras
$('#contato_telefonico').mask('(00)00000-0000')
$('#contato_notificador').mask('(00)00000-0000')
$('#cpf_paciente').mask('000.000.000-00')
$('#cns_paciente').mask('000.0000.0000.0000')
$('#busca_cep_local_acidente').mask('00000-000')

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
    $('#numeros_vitimas_fatais_envolvidas_acidente').parent().removeClass('d-none')
    $('#numeros_vitimas_fatais_envolvidas_acidente').attr('disabled', false).attr('required', true)
    $('input[name="caso_obito"]').attr('disabled', false)
    alerta.text('*')
  } else {
    alerta.text('')
    $('#numeros_vitimas_fatais_envolvidas_acidente').parent().addClass('d-none')
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
    $('#qual_hosp_label').find('spam').text('*')
    $('#qual_hospital').attr('required', true)
    $('#col_qual_hospital').removeClass('d-none')
  } else {
    $('#qual_hosp_label').find('spam').text('')
    $('#qual_hospital')[0].reset()
    $('#qual_hospital').attr('required', false)
    $('#col_qual_hospital').addClass('d-none')
  }
})

// Adicionando campos para a opção Outros (Tipo do Sinistro; Tipos de Veículos Envolvidos no Sinistro)
$('#tipo_acidente, #tipos_veiculos_envolvidos_acidente').on('change', function(){
  let parentElement = this.id === 'tipo_acidente' ? $('#tipo_sinistro_outro') : $('#tipo_veiculo_outro');

  if (this.value === 'outros' || this.value.includes('outros')) {
    parentElement.attr('required', true);
    parentElement.parent().removeClass('d-none')
    parentElement.parent().find('spam').text('*')
  } else {
    parentElement.attr('required', false);
    parentElement.parent().addClass('d-none')
    parentElement.parent().find('spam').text('')
    parentElement.val('')
  }

})

$('#quem_foi_responsavel_por_prestar_apoio_local').on('change', function(){
  let outros = $('#responsavel_prestar_apoio_outro')
  if (this.value.includes('Outros')){
    outros.attr('required', true)
    outros.parent().removeClass('d-none')
    outros.parent().find('spam').text('*')
    
  } else {
    outros.attr('required', false)
    outros.parent().addClass('d-none')
    outros.parent().find('spam').text('')
    outros.val('')
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

// Função que ativa e desativa o campo outros na aba "Outras Informações Sobre o Acidente"
$('#qual_hospital').on('change', function(){
  let col_outros = $('#outros-info-acid')
  let outros_input = col_outros.find('input')
  let outros_alert = col_outros.find('spam')
  if (this.value == 'Outro'){
    col_outros.removeClass('d-none')
    outros_input.attr('required', true).val('')
    outros_alert.text('*')
  } else {
    col_outros.addClass('d-none')
    outros_input.attr('required', false).val('')
    outros_alert.text('')
  }
})


// Busca CEP
$('#busca_cep_local_acidente').on('input', function(){
  const municipio = $('#municipio_ocorrencia_acidente')
  const endereco = $('#endereco_local_acidente')
  const bairro = $('#bairro_local_acidente')
  const cep = this.value.replace('-','');  

  if (cep.length === 8) {
    const url = `https://viacep.com.br/ws/${cep}/json/?callback=?"`

    municipio[0].reset()
    endereco.val('...')
    bairro.val('...')

    $.ajax({
      url: url,
      success: res => {
        res = JSON.parse(res.replace('?','').replaceAll('"(','').replaceAll(');',''))
        if (!res.erro) {
          bairro.val(res.bairro);
          endereco.val(res.logradouro);
          municipio[0].setValue(res.localidade);
          bairro.parent().find('spam').text("");
          this.value = '';

        } else {
          
          bairro.parent().find('spam').text("*");
          bairro.val("Não Encontrado");
          endereco.val("Não Encontrado");

        }        

      },
      error: err => {
        console.error(err)
      }
    })
  }
})
