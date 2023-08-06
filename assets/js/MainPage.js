document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('input-form');
  const userInput = document.getElementById('user-input');

  function handleSubmit(event) {
    event.preventDefault();

    const inputText = userInput.value;

    axios.post('/processInput', { cube: inputText })
      .then(response => {
        displayResult(response.data.result);
      })
      .catch(error => {
        console.error(error);
      });
  }

  function displayResult(result) {
    const resultContainer = document.createElement('div');
    resultContainer.textContent = result;

    document.body.appendChild(resultContainer);
  }

  form.addEventListener('submit', handleSubmit);
});



