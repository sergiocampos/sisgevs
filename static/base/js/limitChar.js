/*
 
  Função para limitar os caracteres pelo PATTERN do html
  Procura dentro do form todos os inputs do tipo texto que possuem o atributo "pattern"
  Em seguida ele valida a tecla que está sendo pressionada e só libera se estiver de acordo 

*/
$('form').find('input[type="text"]').filter('.form-control').each(function(){
  $(this).on('keydown', function(e){
    if (this.pattern){
      let re = new RegExp(this.pattern.split('{')[0]+'{0,}$')
      if(!re.test(e.key)){
        return false;
      }    
    }        
  })
})