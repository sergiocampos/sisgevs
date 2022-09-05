$('#btn-submit').on('click', function(){

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
        if (!field.value){
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
  }  
})
