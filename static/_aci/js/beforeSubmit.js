$('form').on('submit', function(e){
  e.preventDefault();

  var validInputs = true;
  var validRadios = true;
  var validSelects = true;

  var cols = $('form').find('.col')

  cols.each(function(){  
    if($(this).children('label').children('spam').text() == '*'){
      let field = $(this).children()[1]
      if ($(field).hasClass('form-control-sm')){
        if (!field.value){
          validInputs = false;
        }        
      } else if ($(field).hasClass('select-model')){
        if (!field.value){
          validSelects = false;
        }        
      } else if ($(field).hasClass('radio-container')){
        if (!$(field).find('input:checked').val()){
          validRadios = false
        }
      }
    }    
  })
  if (validInputs && validRadios && validSelects){
    this.submit()
  }
})
