/*

    Validando todos os campos antes de enviar o formulário,
    caso esteja tudo ok, envia o formulário.

    Caso contrário ativa a classe 'was-validated' 
    para indicar ao usuário onde está a falha.

*/
$('#btn-submit').on('click', function(e){
  e.preventDefault();

  var validForm = true;
  var cols = $('form').find('.col')

  cols.each(function(){  
    if($(this).children('label').children('spam').text() == '*'){
      let field = $(this).children()[1]
      if ($(field).hasClass('form-control-sm')){
        if (!field.value){
          validForm = false;
        }        
      } else if ($(field).hasClass('select-model')){
        if (!field.value || field.value == ''){
          validForm = false;
        }        
      } else if ($(field).hasClass('radio-container')){
        if (!$(field).find('input:checked').val()){
          validForm = false
        }
      }
    }    
  })

  let form = document.getElementsByTagName('form')[0]
  $(form).addClass('was-validated')
  
  if (validForm && form.checkValidity()){
    form.submit()
  } else {
    window.scrollTo(0,0);
    $('#incomplete_form_alert').removeClass('d-none');
    setTimeout(() => {
      $('#incomplete_form_alert').addClass('d-none');
    }, 10000)

  }
})


/* 

    Adicionando um eventlistener em todos
    os campos para remover ou adicionar
    os asteriscos " * " de alerta.

*/
$(window).ready(function(){
  $('form').find('.col').each(function(){
    let label = $(this).children('label')
    let target = $(this).children()[1]
        
    if ($(target).hasClass('form-control-sm')){ // Tipo Input
      let alert = label.find('spam')
      $(target).on('change', function(e){

        if (e.target.value && alert){
          alert.text('')
        } else if (!e.target.value && alert) {
          alert.text('*')
        }
      })

    } else if ($(target).hasClass('select-model')){ // Tipo Select
      let alert = label.find('spam')
      $(target).on('change', function(e){
        
        if (typeof(e.target.value) == "string"){
          if (e.target.value && alert){
            alert.text('')
          } else if (!e.target.value && alert && e.target.id != "numeros_vitimas_fatais_envolvidas_acidente" && e.target.id != 'qual_hospital') {
            alert.text('*')
          }
        } else {
          if (this.value.length && alert.text() == "*"){
            alert.text('')
          } else if (!this.value.length && alert.text() == "") {
            alert.text('*')
          }
        }
      })


    } else if ($(target).hasClass('radio-container')){ // Tipo Box      
      let alert = label.find('spam')
      let radioBoxs = $(target).find('input')
      $(radioBoxs).on('change', function(e){        
        if($(`input[name="${this.name}"]:checked`)){
          alert.text('')
        } else {
          alert.text('*')
        }
      })

    }
    
  })
})
