// ui/app.js

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search');
    const suggestionsList = document.getElementById('suggestions');
  
    // Debounce user input to avoid flooding API
    let timeout = null;
    searchInput.addEventListener('input', () => {
      clearTimeout(timeout);
      const query = searchInput.value.trim();
      if (query.length < 2) {
        suggestionsList.innerHTML = '';
        return;
      }
  
      timeout = setTimeout(() => {
        fetch(`http://localhost:5000/suggest?q=${encodeURIComponent(query)}`)
          .then(response => response.json())
          .then(data => {
            suggestionsList.innerHTML = '';
            data.suggestions.forEach(suggestion => {
              const li = document.createElement('li');
              li.textContent = suggestion;
              li.onclick = () => alert(`You selected: ${suggestion}`);
              suggestionsList.appendChild(li);
            });
          })
          .catch(error => {
            console.error('Error fetching suggestions:', error);
          });
      }, 300); // debounce delay
    });
  });
  