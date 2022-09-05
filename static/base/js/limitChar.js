function limitcarc(e, tipo) {
  var chr = String.fromCharCode(e.which);
  if (tipo == 'letr_acent'){
      if ("áéíóúâêîôûãõ qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM".indexOf(chr) < 0)
        return false;
  }else if (tipo == 'num') {
      if ("0123456789".indexOf(chr) < 0)
        return false;
  }else if (tipo == 'letr'){
      if ("qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM".indexOf(chr) < 0)
        return false;
  } else if (tipo == 'letr_acent_num'){
      if ("áéíóúâêîôûãõ qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM0123456789-,:;/|".indexOf(chr) < 0)
        return false;
  }
}
