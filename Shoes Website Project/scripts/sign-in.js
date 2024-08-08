document.querySelector('.js-log-in-button').addEventListener('click',()=>{
  const user_text = document.querySelector('.js-user-input').value;
  const pass_text = document.querySelector('.js-pass-input').value;
  if(user_text === '' || pass_text === ''){
    alert('Please enter username or password');
  }
  else{
  window.location.href = 'shoes.html';
  }
});

document.querySelector('.js-create-acc-button').addEventListener('click', () => {
  document.querySelector('.box').innerHTML = `
    <p>Create Account</p>
    <div class="text">Username</div>
    <input class="input js-user-input">
    <br>
    <div class="text">Password</div>
    <input class="input js-pass-input">
    <br>
    <button class="create-acc-button js-submit-acc-button">Create Account</button>`;
});

document.addEventListener('click', (event) => {
  if (event.target && event.target.classList.contains('js-submit-acc-button')) {
    const user_text = document.querySelector('.js-user-input').value;
    const pass_text = document.querySelector('.js-pass-input').value;
    if(user_text === '' || pass_text === ''){
      alert('Please enter username or password');
    }
    else{
      alert(`Account created your username: ${user_text} and password: ${pass_text}`);
      window.location.href = 'shoes.html';
    }
  }
});