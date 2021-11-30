$(function(){
    // Primeiro Grafico
    $('#container').highcharts({
      chart: {
        type: 'pie'
        },
        title: {
          text: ''
        },
        subtitle: {
          text: 'Clique no gráfico para mais detalhes.'
        },

        accessibility: {
          announceNewData: {
            enabled: true
          },
          point: {
            valueSuffix: '%'
          }
        },

        plotOptions: {
          series: {
            dataLabels: {
              enabled: true,
              format: '{point.name}: {point.y:.1f}%'
            }
          }
        },

        tooltip: {
          headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
          pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
        },

        series: [
          {
            name: "Doenças",
            colorByPoint: true,
            data: [
              {
                name: "Dengue",
                y: 25,
                drilldown: "Dengue"
              },
              {
                name: "Chikungonha",
                y: 37,
                drilldown: "Chikungonha"
              },
              {
                name: "Zika",
                y: 38,
                drilldown: "Zika"
              }]
          }],
        drilldown: { 
          series: [
              {
                name: "Dengue",
                id: "Dengue",
                data: [["João Pessoa", 56.5],["Campina Grande", 35.4],["Cabedelo", 10.2],["Bayeux", 7.58], ["Santa Rita", 9.42], ["Mamanguape", 5.52]]
              },{
                name: "Zika",
                id: "Zika",
                data: [["João Pessoa", 56.5],["Campina Grande", 35.4],["Cabedelo", 10.2],["Bayeux", 7.58], ["Santa Rita", 9.42], ["Mamanguape", 5.52]]
              },{
                name: "Chikungonha",
                id: "Chikungonha",
                data: [["João Pessoa", 36.5],["Campina Grande", 35.4],["Cabedelo", 10.2],["Bayeux", 7.58], ["Santa Rita", 9.42], ["Mamanguape", 5.52]]
              },
        ]}
    });
    // Segundo Grafico
    $('#container2').highcharts({
        title: {
            text: ''
        },
        xAxis: {
            categories: ['Notificado', 'Confirmado','Em Análise', 'Descartados', 'Pendências']
        },
        series: [{
            type: 'column',
            name: 'Dengue',
            data: [3, 2, 1, 3, 4]
        }, {
            type: 'column',
            name: 'Chikungonha',
            data: [2, 3, 5, 7, 6]
        }, {
            type: 'column',
            name: 'Zika',
            data: [4, 3, 3, 9, 0]
        }]
    });

  });  

  var dados = {
    paciente1: {
      "id":1,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente2: {
      "id":2,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente3: {
      "id":3,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente4: {
      "id":4,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente5: {
      "id":5,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente6: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente7: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente8: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente9: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente10: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },paciente11: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente12: {
      "id":2,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente13: {
      "id":3,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente14: {
      "id":4,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente15: {
      "id":5,
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente16: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente17: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente18: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente19: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
    paciente20: {
      "id":"id",
      "doenca":"doenca",
      "idade_paciente":"idade_paciente",
      "municipio":"municipio",
      "data_notificacao":"data_notificacao",
    },
  };
$(document).ready(function(){
  $("#dados-click").hide();
  //console.log(Object.keys(dados).length);
  for (dado in dados){
    $("table > tbody:last-child").append(`
        <tr>
          <td>dado.id</td>
          <td>dado.doenca</td>
          <td>dado.idade_paciente</td>
          <td>dado.municipio</td>
          <td>dado.data_notificacao</td>
        </tr>
      `);
  }
});
$("#btn-transparencia").on('click', function(){
  var atributo = document.getElementById('btn-transparencia');
  if (atributo.getAttribute('clicked') == "false") {
    $("#dados-click").show();
    $("#btn-transparencia").attr('clicked', true);
        
  } else if (atributo.getAttribute('clicked') == "true") {
    $("#dados-click").hide();
    $("#btn-transparencia").attr('clicked', false);  
  }
  
  // console.log(atributo.getAttribute('clicked'));
  
  //$("#btn-transparencia").attr('clicked', true);
  //$("#dados-click").show();
  //console.log(atributo.getAttribute('clicked'));
});

