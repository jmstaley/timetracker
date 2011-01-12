function setupUi(){
  // hide elements
  $('.hide').hide();
  setupAddTaskToggle();
}

function setupAddTaskToggle(){
  $('#addlink').click(function(){
    $('#addtaskform').slideToggle('slow');
    return false;
  });
}
