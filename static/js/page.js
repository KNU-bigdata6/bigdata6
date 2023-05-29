function handleSubmit() {

  var textInput = document.getElementById('text');
  
  if (textInput.value.trim() == '') {
    alert('등록하시려는 댓글을 입력해주세요.');
    return false;
  }

  return true;
}