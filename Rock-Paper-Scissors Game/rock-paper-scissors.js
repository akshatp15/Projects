let score = JSON.parse(localStorage.getItem('score')) || {
  wins: 0,
  losses: 0,
  ties: 0,
};
updateScoreElement();
/*
if(!score){
  score = {
    wins: 0,
    losses: 0,
    ties: 0,
  };
}*/
let isAutoPlaying = false;
let intervalid;
function autoplay(){
  if(!isAutoPlaying){
    intervalid = setInterval(() => {
      const playerMove = pickComputerMove();
      playgame(playerMove);
    }, 1000);
    isAutoPlaying = true;
  }
  else{
    clearInterval(intervalid);
    isAutoPlaying = false;
  }
}
document.querySelector('.js-rock-button').addEventListener('click', () => {
  playgame('rock');
});
document.querySelector('.js-paper-button').addEventListener('click', () => {
  playgame('paper');
});
document.querySelector('.js-scissors-button').addEventListener('click', () => {
  playgame('scissors');
});
document.body.addEventListener('keydown',(event)=>{
  if(event.key === 'r'){
    playgame('rock');
  }
  else if(event.key === 'p')
  {
    playgame('paper');
  }
  else if(event.key === 's'){
    playgame('scissors');
  }
}
)
function playgame(playerMove){
  const computerMove = pickComputerMove();
  let result = '';
  if(playerMove === 'scissors'){
    if(computerMove === 'scissors'){
    result = 'Tie';
    }
    else if(computerMove === 'rock'){
    result = 'You Lose';
    }
    else{
      result = 'You Win';
    }
  }
  else if(playerMove === 'paper'){
    if(computerMove === 'paper'){
    result = 'Tie';
    }
    else if(computerMove === 'scissors'){
      result = 'You Lose';
    }
    else{
      result = 'You Win';
    }
  }
  else{
    if(computerMove === 'rock'){
      result = 'Tie';
    }
    else if(computerMove === 'paper'){
      result = 'You Lose';
    }
    else{
      result = 'You Win';
    }
  }
  if(result === 'You Win'){
    score.wins += 1;
  }
  else if(result === 'You Lose'){
    score.losses += 1;
  }
  else{
    score.ties += 1;
  }
  localStorage.setItem('score', JSON.stringify(score));
  updateScoreElement();
  document.querySelector('.js-result').innerHTML = result;
  document.querySelector('.js-moves').innerHTML = `You <img src="images/${playerMove}-emoji.png" class="move-icon"> Computer <img src="images/${computerMove}-emoji.png" class="move-icon">`
  /*
  alert(`You picked ${playerMove}. Computer picked ${computerMove}. ${result}
Wins ${score.wins}, Losses ${score.losses}, Ties ${score.ties}`);*/
}
function updateScoreElement(){
  document.querySelector('.js-score').innerHTML = `Wins ${score.wins}, Losses ${score.losses}, Ties ${score.ties}`;
}
function pickComputerMove(){
  let computerMove;
  const randomNumber = Math.random();
  if(randomNumber >= 0 &&randomNumber < 1/3 ){
    computerMove = 'rock';
  }
  else if(randomNumber >= 1/3 &&randomNumber < 2/3){
    computerMove = 'paper';
  }
  else{
    computerMove = 'scissors';
  }
return computerMove;
 }