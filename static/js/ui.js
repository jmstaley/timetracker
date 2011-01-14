function setupUi(){
  setupAddToggle();
  $('#tasktable').tablesorter({sortList: [[2,0],]});
}

function setupAddToggle(){
  if($('#addtaskform')){
    addToggle('#addlink', '#addtaskform');
  }

  if($('#addworkform')){
    addToggle('#addlink', '#addworkform');
  }
}

function addToggle(link, form){
  $(link).click(function(){
    $(form).slideToggle('slow');
    return false;
  });
}

