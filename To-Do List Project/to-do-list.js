let todoList = [];
function renderTodoList(){
  let todoListHTML = '';
  todoList.forEach((todoObject, index) => {
    const name = todoObject.name;
    const dueDate = todoObject.dueDate;
    const html = `<div>${name}</div> <div>${dueDate}</div> 
    <button class="delete-todo-button js-delete-todo-button">Delete</button>`
    todoListHTML += html;
  });
  document.querySelector(".js-todo-list").innerHTML = todoListHTML;
  document.querySelectorAll('.js-delete-todo-button').forEach((deleteButton, index) =>{
    deleteButton.addEventListener('click',() =>{
      todoList.splice(index, 1);
      renderTodoList();
    })
  });
}
document.querySelector('.js-add-todo-button').addEventListener('click', ()=>{addTodo();});
function addTodo(){
  let inputElement = document.querySelector('.js-name-input');
  const name = inputElement.value;
  const dateInputElement = document.querySelector('.js-due-date-input');
  const dueDate = dateInputElement.value;
  todoList.push({name: name, dueDate: dueDate});
  inputElement.value = '';
  renderTodoList();
}
